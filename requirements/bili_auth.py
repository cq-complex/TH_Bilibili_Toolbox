"""Bilibili Web sign-in and opt-in local cookie storage."""

import os
import time
from copy import copy
from http.cookiejar import MozillaCookieJar
from pathlib import Path
from tempfile import NamedTemporaryFile

from .bili_api import APIError, api_data


APP_DIR = Path(os.environ.get("LOCALAPPDATA") or Path.home() / ".local" / "share")
LOGIN_FILE = APP_DIR / "TH-Bilibili-Toolbox" / "login.cookies"
AUTH_NAMES = {"SESSDATA", "bili_jct", "DedeUserID", "DedeUserID__ckMd5"}
QR_ENDPOINT = "https://passport.bilibili.com/x/passport-login/web/qrcode/"
NAV_ENDPOINT = "https://api.bilibili.com/x/web-interface/nav"


def auth_cookies(jar):
    return [
        cookie for cookie in jar
        if cookie.name in AUTH_NAMES and cookie.domain.lstrip(".") == "bilibili.com"
        and cookie.path == "/" and cookie.value and not cookie.is_expired()
    ]


def apply_login(session, cookies):
    for cookie in list(session.cookies):
        if cookie.name in AUTH_NAMES and (
            cookie.domain == "" or cookie.domain.lstrip(".") == "bilibili.com"
            or cookie.domain.endswith(".bilibili.com")
        ):
            session.cookies.clear(cookie.domain, cookie.path, cookie.name)
    for cookie in cookies:
        secure_cookie = copy(cookie)
        secure_cookie.secure = True
        session.cookies.set_cookie(secure_cookie)


def load_login(session):
    jar = MozillaCookieJar(str(LOGIN_FILE))
    try:
        jar.load(ignore_discard=True)
    except (OSError, ValueError):
        return
    cookies = auth_cookies(jar)
    if any(cookie.name == "SESSDATA" for cookie in cookies):
        apply_login(session, cookies)


def save_login(cookies):
    LOGIN_FILE.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    jar = MozillaCookieJar()
    for cookie in cookies:
        jar.set_cookie(cookie)
    with NamedTemporaryFile(dir=LOGIN_FILE.parent, delete=False) as file:
        temp_path = Path(file.name)
    try:
        jar.save(str(temp_path), ignore_discard=True)
        temp_path.replace(LOGIN_FILE)
    finally:
        if temp_path.exists():
            temp_path.unlink()


def run_qr_login(session, headers, events, cancelled):
    """Run network calls off the Tk thread. The queue carries only UI events."""
    try:
        data = api_data(session.get(QR_ENDPOINT + "generate", headers=headers, timeout=8))
        key, url = data["qrcode_key"], data["url"]
        if not url or not key:
            raise APIError("Missing QR code")
        events.put(("qr", url))
        deadline = time.monotonic() + 180
        while time.monotonic() < deadline and not cancelled.wait(2):
            data = api_data(session.get(
                QR_ENDPOINT + "poll", params={"qrcode_key": key}, headers=headers, timeout=8,
            ))
            code = data.get("code")
            if code == 0:
                cookies = auth_cookies(session.cookies)
                if not any(cookie.name == "SESSDATA" for cookie in cookies):
                    raise APIError("No login cookie received")
                events.put(("success", cookies))
                return
            if code == 86038:
                break
            if code not in (86090, 86101):
                raise APIError("Unexpected QR login status")
            events.put(("scanned" if code == 86090 else "waiting", None))
        if not cancelled.is_set():
            events.put(("expired", None))
    except (OSError, ValueError, KeyError, TypeError):
        if not cancelled.is_set():
            events.put(("error", None))
