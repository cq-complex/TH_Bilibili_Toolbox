"""Tk dialogs for the Bilibili Web login methods."""

import threading
import tkinter as tk
from queue import Empty, Queue
from tkinter import messagebox, simpledialog

from .bili_auth import (
    APIError, LOGIN_FILE, NAV_ENDPOINT, api_data, apply_login, auth_cookies,
    run_qr_login, save_login,
)


def dialog_text(language, cn, en, tc):
    return cn if language == 0 else tc if language == 2 else en


def open_qr_login(parent, session, new_session, headers, title, language, font, dpi_scale):
    def tr(cn, en, tc):
        return dialog_text(language, cn, en, tc)

    try:
        import qrcode
    except ImportError:
        messagebox.showwarning(title, tr(
            "请先运行 python -m pip install qrcode。",
            "Install qrcode with python -m pip install qrcode.",
            "請先執行 python -m pip install qrcode。",
        ), parent=parent)
        return

    window = tk.Toplevel(parent)
    window.title(title)
    window.transient(parent)
    window.resizable(False, False)
    window.grab_set()
    cancelled = threading.Event()
    events = Queue()
    remember = tk.BooleanVar(window, value=False)
    status = tk.StringVar(window, tr("正在获取二维码…", "Loading QR code…", "正在取得 QR Code…"))
    canvas = tk.Canvas(window, width=1, height=1, bg="white", highlightthickness=0)
    canvas.pack(padx=12, pady=8)
    tk.Label(window, textvariable=status, font=font).pack(padx=12)
    checkbox = tk.Checkbutton(window, variable=remember, font=font, text=tr(
        "在此设备保存登录状态", "Remember login on this device", "在此裝置儲存登入狀態",
    ))
    checkbox.pack(pady=6)

    def close():
        cancelled.set()
        window.destroy()

    window.bind("<Destroy>", lambda event: cancelled.set() if event.widget == window else None)

    def forget():
        try:
            LOGIN_FILE.unlink(missing_ok=True)
        except OSError:
            messagebox.showwarning(title, tr(
                "无法清除本地登录。", "Could not clear saved login.", "無法清除本機登入。",
            ), parent=window)
            return
        apply_login(session, [])
        close()

    forget_button = tk.Button(window, command=forget, font=font, text=tr(
        "退出并清除已保存的登录", "Sign out and clear saved login", "登出並清除已儲存的登入",
    ))
    if auth_cookies(session.cookies) or LOGIN_FILE.is_file():
        forget_button.pack(pady=4)
    tk.Button(window, command=close, font=font, text=tr("关闭", "Close", "關閉")).pack(pady=4)
    window.protocol("WM_DELETE_WINDOW", close)
    window.bind("<Escape>", lambda event: close())

    messages = {
        "waiting": tr("请用哔哩哔哩 App 扫码并确认。", "Scan and confirm in the Bilibili app.", "請用嗶哩嗶哩 App 掃碼並確認。"),
        "scanned": tr("已扫码，请在手机上确认。", "Scanned. Confirm on your phone.", "已掃碼，請在手機上確認。"),
        "expired": tr("二维码已过期，请关闭窗口后重试。", "QR code expired. Close and reopen this window.", "QR Code 已過期，請關閉視窗後重試。"),
        "error": tr("扫码登录失败，请关闭窗口后重试。", "QR login failed. Close and reopen this window.", "掃碼登入失敗，請關閉視窗後重試。"),
        "success": tr("登录成功。", "Signed in.", "登入成功。"),
    }

    def handle_events():
        try:
            while True:
                event, value = events.get_nowait()
                if event == "qr":
                    qr = qrcode.QRCode(border=4)
                    qr.add_data(value)
                    matrix = qr.get_matrix()
                    scale = max(3, round(4 * dpi_scale))
                    side = len(matrix) * scale
                    canvas.configure(width=side, height=side)
                    for y, row in enumerate(matrix):
                        for x, dark in enumerate(row):
                            if dark:
                                canvas.create_rectangle(
                                    x * scale, y * scale, (x + 1) * scale, (y + 1) * scale,
                                    fill="black", width=0,
                                )
                    status.set(messages["waiting"])
                elif event in ("waiting", "scanned"):
                    status.set(messages[event])
                else:
                    canvas.pack_forget()
                    checkbox.configure(state=tk.DISABLED)
                    status.set(messages[event])
                    if event == "success":
                        apply_login(session, value)
                        forget_button.pack(pady=4)
                        if remember.get():
                            try:
                                save_login(value)
                            except OSError:
                                messagebox.showwarning(title, tr(
                                    "已登录，但无法在本地保存。",
                                    "Signed in, but the login could not be saved.",
                                    "已登入，但無法儲存在本機。",
                                ), parent=window)
                    return
        except Empty:
            window.after(100, handle_events)

    def worker():
        with new_session() as login_session:
            run_qr_login(login_session, headers, events, cancelled)

    threading.Thread(target=worker, daemon=True).start()
    handle_events()


def prompt_cookie_login(parent, session, new_session, headers, title, language):
    cookie = simpledialog.askstring(title, dialog_text(language,
        "请输入 B 站 Cookie 中的 SESSDATA 字段。",
        "Enter the SESSDATA value from your Bilibili cookies.",
        "請輸入 B 站 Cookie 中的 SESSDATA 欄位。",
    ), show="*", parent=parent)
    if not cookie or not cookie.strip():
        return
    cookie = cookie.strip()
    try:
        if any(char in cookie for char in ";\r\n"):
            raise APIError("Invalid SESSDATA")
        with new_session() as login_session:
            login_session.cookies.set("SESSDATA", cookie, domain=".bilibili.com", path="/", secure=True)
            account = api_data(login_session.get(NAV_ENDPOINT, headers=headers, timeout=8))
            if not account.get("isLogin"):
                raise APIError("Not signed in")
            cookies = auth_cookies(login_session.cookies)
    except (OSError, ValueError):
        messagebox.showwarning(title, dialog_text(language,
            "登录失败。", "Sign-in failed.", "登入失敗。",
        ), parent=parent)
        return
    apply_login(session, cookies)
    messagebox.showinfo(title, dialog_text(language,
        "登录成功。", "Signed in.", "登入成功。",
    ), parent=parent)
