# 当前代码总行数：9099
import tkinter.messagebox  # TK消息框
import tkinter.simpledialog  # TK输入框
import tkinter.font
import tkinter.ttk
import sys
import logging
import ctypes
import locale


def configure_dpi_awareness() -> None:
    """在创建 Tk 窗口前启用 Windows 的高 DPI 感知。"""
    if sys.platform != "win32":
        return
    try:
        # Per-monitor v2：窗口移动到不同缩放率的显示器时也能保持清晰。
        ctypes.windll.user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))
    except Exception:
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        except Exception:
            try:
                ctypes.windll.user32.SetProcessDPIAware()
            except Exception:
                pass


def detect_system_language() -> int:
    """将系统区域语言映射为工具箱支持的语言编号。"""
    language_map = {
        "en": LANG_EN if "LANG_EN" in globals() else 1,
        "ja": 3, "de": 4, "fr": 5, "th": 6, "ko": 7,
        "ru": 8, "vi": 9, "pt": 10, "es": 11, "id": 12,
    }
    candidates = []
    try:
        locale_name = ctypes.create_unicode_buffer(85)
        if ctypes.windll.kernel32.GetUserDefaultLocaleName(locale_name, len(locale_name)):
            candidates.append(locale_name.value)
    except Exception:
        pass
    try:
        candidates.append(locale.getlocale()[0])
    except Exception:
        pass
    candidates.extend((os.environ.get("LANG"), os.environ.get("LANGUAGE")) if "os" in globals() else ())
    for candidate in candidates:
        normalized = (candidate or "").lower().replace("-", "_")
        if normalized.startswith("zh"):
            return LANG_TC if any(marker in normalized for marker in ("tw", "hk", "mo", "hant")) else LANG_CN
        code = normalized.split("_")[0]
        if code in language_map:
            return language_map[code]
    return LANG_EN if "LANG_EN" in globals() else 1


configure_dpi_awareness()


class BilibiliError(Exception):
    pass


class NicknameError(BilibiliError):
    pass


class SignError(BilibiliError):
    pass


class THBiliTools:
    def __init__(self, mode=1) -> None: ...


icon_file = ".\\requirements\\icon.ico"
loading_window = tkinter.Tk()
loading_window.resizable(False, False)
try:
    dpi_scale = loading_window.winfo_fpixels("1i") / 96.0
    loading_window.tk.call("tk", "scaling", 96.0 * dpi_scale / 72.0)
except Exception:
    dpi_scale = 1.0
version = "v0.14.2"  # 版本号

# Language constants
LANG_CN = 0      # Simplified Chinese
LANG_EN = 1      # English
LANG_TC = 2      # Traditional Chinese
LANG_JP = 3      # Japanese
LANG_DE = 4      # German
LANG_FR = 5      # French
LANG_TH = 6      # Thai
LANG_KO = 7      # Korean
LANG_RU = 8      # Russian
LANG_VI = 9      # Vietnamese
LANG_PT = 10     # Portuguese
LANG_ES = 11     # Spanish
LANG_ID = 12     # Indonesian

# Font sizes
FONT_SIZE_SMALL = 9
FONT_SIZE_MEDIUM = 10
FONT_SIZE_LARGE = 11
FONT_SIZE_XLARGE = 14

# Window dimensions
WINDOW_WIDE_WIDTH = 140
WINDOW_NARROW_WIDTH = 25
OUTPUT_WINDOW_HEIGHT = 40
OUTPUT_WINDOW_WIDTH = 140
LABEL_WINDOW_HEIGHT = 200
LABEL_WINDOW_WIDTH = 1200

# Text widget dimensions
TEXT_INPUT_WIDTH = 70
TEXT_OUTPUT_WIDTH = 70
TEXT_HEIGHT = 50

# Grid layout
MENU_START_ROW = 3
MENU_COLUMN_BREAK_ROW = 12
MENU_COLUMN_PAD = 20
window_title = "氚氢B站工具箱 " + version  # 标题
showinfo = tkinter.messagebox.showinfo
showwarning = tkinter.messagebox.showwarning
showerror = tkinter.messagebox.showerror
askokcancel = tkinter.messagebox.askokcancel
askstring = tkinter.simpledialog.askstring
Font = tkinter.font.Font
askinteger = tkinter.simpledialog.askinteger
askfloat = tkinter.simpledialog.askfloat
Button = tkinter.Button
INSERT = tkinter.INSERT
DISABLED = tkinter.DISABLED
NORMAL = tkinter.NORMAL
MAX_RETRIES = 2
opencc_available = 1
try:
    import requirements.trans as trans
except Exception:
    opencc_available = 0
try:
    to_traditional = trans.OpenCC("s2twp").convert if opencc_available else lambda a: a
    to_traditional("测试")
except Exception:
    opencc_available = 0
    to_traditional = lambda a: a
use_pygame = True
avbv_available = True
import os

requests_available = True
try:
    import requests as rq  # requests
except Exception:
    requests_available = False
import time

egg_available = True
try:
    import requirements.UsersEgg as UsersEgg  # 彩蛋插件
except Exception:
    egg_available = False
import threading

foreign_available = True
try:
    import requirements.foreign as foreign  # 多语言插件
except Exception:
    foreign_available = False
    showerror(
        title=window_title,
        message='foreign.py丢失，程序将无法正常使用！\n"foreign.py" has been lost. The program will not run properly!',
    )
from pathlib import Path
from webbrowser import open as wopen

try:
    from requirements.avbv import *  # AVBV互转插件
except Exception:
    avbv_available = False
if requests_available:
    requests = rq.session()
else:
    showerror(
        title=window_title,
        message="requests模块未安装，程序将无法正常使用！\nRequests module is not installed. The program will not run properly!",
    )
Label = tkinter.Label
try:
    from requirements.lognew import *  # 更新日志
except Exception:
    log_error = 1
else:
    log_error = 0
from requirements.bili_api import (
    APIError, api_code, api_data, api_message, read_api_response, require_api_success,
)
from requirements.bili_auth import load_login
from requirements.bili_qr_ui import open_qr_login, prompt_cookie_login

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}
if requests_available:
    load_login(requests)
font_family = "HarmonyOS Sans SC"
default_font = (font_family, 9)  # 默认中文字体
loading_window.iconbitmap(icon_file)
topic_image = tkinter.PhotoImage(file="requirements\\Topic.png")  # 主题图片
image_label = tkinter.Label(loading_window, image=topic_image)
image_label.grid(row=0, column=1)
version_suffixes = ["" for i in range(13)]
status_labels = [
    f"终结版{version_suffixes[0]}\n版本号：",
    f"Final  Version{version_suffixes[1]}\nVersion: ",
    f"最終版{version_suffixes[2]}\n版本號：",
    f"最終テストバージョン{version_suffixes[3]}\nバージョン番号: ",
    f"Endversion des Tests{version_suffixes[4]}\nVersionsnummer: ",
    f"Version finale de test{version_suffixes[5]}\nNuméro de version : ",
    f"รุ่นทดสอบสุดท้าย{version_suffixes[6]}\nหมายเลขเวอร์ชัน: ",
    f"최종 테스트 버전{version_suffixes[7]}\n버전 번호: ",
    f"Окончательная тестовая версия{version_suffixes[8]}\nНомер версии: ",
    f"Phiên bản thử nghiệm cuối cùng{version_suffixes[9]}\nSố phiên bản: ",
    f"Versão final de teste{version_suffixes[10]}\nNúmero da versão: ",
    f"Versión final de prueba{version_suffixes[11]}\nNúmero de versión: ",
    f"Versi Uji Akhir{version_suffixes[12]}\nNomor versi: ",
]
status_labels = [
    "维护版\n版本号：",
    "Maintenance Version\nVersion: ",
    "維護版\n版本號：",
    "メンテナンス版\nバージョン番号: ",
    "Wartungsversion\nVersionsnummer: ",
    "Version de maintenance\nNuméro de version : ",
    "รุ่นบำรุงรักษา\nหมายเลขเวอร์ชัน: ",
    "유지보수 버전\n버전 번호: ",
    "Версия обслуживания\nНомер версии: ",
    "Phiên bản bảo trì\nSố phiên bản: ",
    "Versão de manutenção\nNúmero de versão: ",
    "Versión de mantenimiento\nNúmero de versión: ",
    "Versi pemeliharaan\nNomor versi: ",
]
Label()
LANG_DESCRIPTION = """
0：简体中文
1：English (Default)
2：繁體中文
3：日本語
4：Deutsch
5：Français
6：ไทย
7：한국어
8：Русский
9：Tiếng Việt
10：Português (em desenvolvimento)
11：Español (en desarrollo)
12：Bahasa Indonesia (dalam pengembangan)"""
lang = detect_system_language()
font_variant = 0
if not use_pygame:
    font_variant = 1
init_file_exists = False
try:
    # 初始化文件只保存初始字体；界面语言始终由系统区域自动识别。
    with open("./requirements/initialize.txt", "r", encoding="utf-8") as init_file:
        for line in init_file:
            key, separator, value = line.partition("=")
            if key.strip().lower() == "font" and separator:
                font_variant = int(value.strip())
    init_file_exists = True
except (OSError, ValueError):
    pass

if not 0 <= lang < len(status_labels):
    lang = LANG_EN
if not 0 <= font_variant < 4:
    font_variant = 0

def get_font_family(language, variant) -> str:
    """从语言插件读取字体，并兼容旧版插件使用的 ``fonts`` 名称。"""
    if not foreign_available:
        return "Simsun"
    font_sets = getattr(foreign, "font_family", getattr(foreign, "fonts", ()))
    try:
        return font_sets[language][variant]
    except (IndexError, KeyError, TypeError):
        return "Simsun"


font_family = get_font_family(lang, font_variant)
status_label = Label(loading_window, text=status_labels[lang] + version, font=(font_family, 14), fg="#626020")
status_label.grid(row=1, column=1)
# status_label.config(text=status_labels[lang]+version,font=(foreign.font_family[lang][font_variant],11))
default_font = (font_family, 9)

window_titles = [
    i + version
    for i in [
        "氚氢B站工具箱 ",
        "TH Bilibili Toolbox ",
        "氚氫B站工具箱 ",
        "TH Bilibiliツールボックス ",
        "TH Bilibili Werkzeugkasten ",
        "Boîte à outils TH bilibili ",
        "กล่องเครื่องมือ TH Bilibili ",
        "TH Bilibili 도구 상자 ",
        "Набор инструментов TH Bilibili ",
        "Hộp công cụ TH Bilibili ",
        "Caixa de Ferramentas TH Bilibili ",
        "La Caja de herramientas TH bilibili ",
        "TH Bilibili Kotak Alat ",
    ]
]
ok_button_labels = [
    "确定",
    "OK",
    "確定",
    "確かですか",
    "Okay",
    "D’accord",
    "ตกลง",
    "그래",
    "Хорошо",
    "Ok",
    "Ok",
    "De acuerdo",
    "OK",
]

window_title = window_titles[lang]


def request_api(url, *, timeout=8, **kwargs):
    if not requests_available:
        raise APIError("缺少 requests 依赖 / The requests package is required")
    return requests.get(url, timeout=timeout, **kwargs)


def translated_api_message(code, fallback):
    if lang and foreign_available:
        translations = foreign.lang1.get(code)
        if translations and lang <= len(translations):
            return translations[lang - 1]
    return fallback


def report_callback_error(exc_type, error, traceback):
    if isinstance(error, (APIError, BilibiliError)):
        message = str(error)
    elif requests_available and isinstance(error, rq.exceptions.RequestException):
        response = error.response
        if response is not None:
            message = f"请求失败 / Request failed (HTTP {response.status_code})"
        else:
            message = "连接失败或请求超时 / Could not connect or the request timed out"
    elif isinstance(error, (KeyError, IndexError, TypeError)):
        tkinter.Tk.report_callback_exception(loading_window, exc_type, error, traceback)
        message = "功能遇到缺失或不兼容的数据 / Feature received missing or incompatible data"
    else:
        tkinter.Tk.report_callback_exception(loading_window, exc_type, error, traceback)
        return
    showwarning(title=window_title, message=message, parent=loading_window)


loading_window.report_callback_exception = report_callback_error


def outpt(ht=OUTPUT_WINDOW_HEIGHT, wd=OUTPUT_WINDOW_WIDTH) -> None:  # 大窗口
    global output_window
    output_window = tkinter.Toplevel(loading_window)
    output_window.title(window_title)
    output_window.iconbitmap(icon_file)
    global output_text
    scrollbar_v = tkinter.Scrollbar(output_window)
    scrollbar_v.pack(side="right", fill="y")
    output_text = tkinter.Text(
        output_window, height=ht, width=wd, yscrollcommand=scrollbar_v.set, font=default_font
    )
    output_text.pack()
    scrollbar_v.config(command=output_text.yview)
    bcanc = Button(output_window, text=ok_button_labels[lang], command=output_window.destroy, font=default_font)
    bcanc.pack()
    """def close(ev):
        output_window.destroy()
    output_window.bind('<Escape>',close)"""


outsmall = lambda: outpt(20, 140)


def write_to_file(filename, content):
    """将内容写入文件（追加模式）"""
    with open(filename, 'a', buffering=1) as f:  # buffering=1 启用行缓冲
        f.write(content + '\n')  # 写入内容并添加换行符


def outlabel(ht=200, wd=1200) -> None:  # 标签窗口
    global output_window
    output_window = tkinter.Toplevel(loading_window)
    output_window.title(window_title)
    output_window.iconbitmap(icon_file)
    output_window.geometry(f"{wd}x{ht}")


def time_convert(ts: float, mode=1) -> str:
    ymd = [0, 2, 3, 7]
    mdy = [1, 9]
    dmy = [4, 5, 6, 8, 10, 11, 12]
    if mode == 1:
        if lang in ymd:
            birthday = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
        elif lang in mdy:
            birthday = time.strftime("%m-%d-%Y %H:%M:%S", time.localtime(ts))
        elif lang in dmy:
            birthday = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(ts))
    elif mode == 2:
        if lang in ymd:
            birthday = time.strftime("%Y-%m-%d", time.localtime(ts))
        elif lang in mdy:
            birthday = time.strftime("%m-%d-%Y", time.localtime(ts))
        elif lang in dmy:
            birthday = time.strftime("%d-%m-%Y", time.localtime(ts))
    return birthday


def req(url: str, tries=MAX_RETRIES, headers=headers) -> tuple:
    for t in range(1, tries + 1):
        try:
            page = request_api(url, headers=headers)
        except Exception as e:
            if t < tries:
                pass
            else:
                error_text = str(e)
                error_msgs = [
                    f"请求尝试{t}次后仍然发生错误：{error_text}",
                    f"The request still failed after {t} attempts: {error_text}",
                    f"請求嘗試{t}次後仍然發生錯誤：{error_text}",
                    f"要求を {t} 回試行した後もエラーが発生しました： {error_text}",
                    f"Nach {t} Versuchen an der Anforderung trat immer noch ein Fehler auf: {error_text}",
                    f"Une erreur se produisait encore après {t} tentatives de requête : {error_text}",
                    f"ข้อผิดพลาดยังคงเกิดขึ้นหลังจาก {t} ครั้งของความพยายามที่คําขอ: {error_text}",
                    f"요청을 {t}번 시도한 후에도 오류가 계속 발생했습니다: {error_text}",
                    f"Ошибка по-прежнему возникала после {t} попыток выполнения запроса: {error_text}",
                    f"Vẫn xảy ra lỗi sau {t} lần thử yêu cầu: {error_text}",
                    f"Ainda ocorreu um erro após {t} vezes de tentativas na solicitação: {error_text}",
                    f"Todavía se ha producido un error después de {t} veces de intentos en la solicitud: {error_text}",
                    f"Kesalahan masih terjadi setelah {t} kali upaya permintaan: {error_text}",
                ]
                showwarning(title=window_title, message=error_msgs[lang])
                raise e
        else:
            return (read_api_response(page), t)


def query_user_info() -> None:  # 查询用户信息
    uid_prompt = [
        "输入B站UID...",
        "Input Bilibili User ID...",
        "輸入B站UID...",
        "BilibiliユーザーIDを入力...",
        "Bitte geben Sie die Bilibili-Benutzer-ID ein...",
        "Entrez l’ID utilisateur Bilibili...",
        "ใส่ ID ผู้ใช้ Bilibili...",
        "Bilibili 사용자 ID 입력...",
        "Введите идентификатор пользователя...",
        "Nhập ID người dùng Bilibili...",
        "Input Bilibili User ID...",
        "Input Bilibili User ID...",
        "Input Bilibili User ID...",
    ]
    user_id = askinteger(title=window_title, prompt=uid_prompt[lang], minvalue=1)
    if user_id is None:
        return
    url = f"https://space.bilibili.com/{user_id}"
    try:
        result = api_data(request_api(
            "https://api.bilibili.com/x/web-interface/card",
            params={"mid": user_id}, headers={**headers, "Referer": url + "/"}, timeout=8,
        ))
        card = result.get("card")
        if not isinstance(card, dict) or not card.get("name"):
            raise APIError("No user card returned")
    except (OSError, ValueError) as error:
        showwarning(title=window_title, message=str(error))
        return

    def localize(value):
        translations = foreign.lang1.get(value) if foreign_available and lang else None
        return translations[lang - 1] if translations and len(translations) >= lang else value

    t = 1
    nickname = card["name"]
    gender = localize(card.get("sex") or "—")
    signature = card.get("sign") or card.get("signature") or ""
    if lang == LANG_TC:
        signature = to_traditional(signature)
    lv = (card.get("level_info") or {}).get("current_level", "—")
    birthday = card.get("birthday") or "—"
    fans = result.get("follower", card.get("fans", "—"))
    follow = card.get("friend", card.get("attention", "—"))
    vip = card.get("vip") or {}
    vip_label = vip.get("label") or vip.get("Label") or {}
    vip_status = localize(vip_label.get("text") or {0: "未开通或已过期", 1: "Active"}.get(vip.get("vipStatus"), "—"))
    official = card.get("Official") or card.get("official") or {}
    verification_status = official.get("title") or localize("未认证")
    states = {0: "正常", -2: "被封禁"} if lang in (LANG_CN, LANG_TC) else {0: "Normal", -2: "Banned"}
    account_status = states.get(card.get("spacesta"), "—")
    if lang == 0:
        output_message = (
            f"请求共尝试了{t}次。"
            + f"\n昵称：\t\t{nickname}"
            + f"\nUID：\t\t{user_id}"
            + f"\n性别：\t\t{gender}"
            + f"\n大会员状态：\t\t{vip_status}"
            + f"\n认证状态：\t\t{verification_status}"
            + f"\n账号状态：\t\t{account_status}"
            + f"\n粉丝数：\t\t{fans}"
            + f"\n关注数：\t\t{follow}"
            + f"\n签名：\n{signature}"
            + f"\n等级：\t\t{lv}"
            + f"\n生日：\t\t{birthday}"
            + f"\nB站空间：\t\t{url}"
        )
    elif lang == 1:
        output_message = (
            f"The request was attempted {t} time(s)."
            + f"\nNickname:\t\t\t{nickname}"
            + f"\nUID:\t\t\t{user_id}"
            + f"\nGender:\t\t\t{gender}"
            + f"\nBig Member status:\t\t\t{vip_status}"
            + f"\nCertification status:\t\t\t{verification_status}"
            + f"\nAccount Status:\t\t\t{account_status}"
            + f"\nFans count:\t\t\t{fans}"
            + f"\nFollow count:\t\t\t{follow}"
            + f"\nSign:\n{signature}"
            + f"\nLevel:\t\t\t{lv}"
            + f"\nBirthday: \t\t\t{birthday}"
            + f"\nBilibili space link:\t\t\t{url}"
        )
    elif lang == 2:
        output_message = (
            f"請求共嘗試了{t}次。"
            + f"\n暱稱：\t\t{nickname}"
            + f"\nUID：\t\t{user_id}"
            + f"\n性別：\t\t{gender}"
            + f"\n大會員狀態：\t\t{vip_status}"
            + f"\n認證狀態：\t\t{verification_status}"
            + f"\n賬號狀態：\t\t{account_status}"
            + f"\n粉絲數：\t\t{fans}"
            + f"\n關注數：\t\t{follow}"
            + f"\n簽名：\n{signature}"
            + f"\n等級：\t\t{lv}"
            + f"\n生日：\t\t{birthday}"
            + f"\nB站空間：\t\t{url}"
        )
    elif lang == 3:
        output_message = (
            f"The request was attempted {t} times."
            + f"\nユーザー名：\t\t{nickname}"
            + f"\nUID：\t\t{user_id}"
            + f"\nジェンダー：\t\t{gender}"
            + f"\nビッグメンバーのステータス：\t\t{vip_status}"
            + f"\n認証取得状況：\t\t{verification_status}"
            + f"\nアカウントステータス：\t\t{account_status}"
            + f"\nファン数：\t\t{fans}"
            + f"\nフォローするユーザーの数：\t\t{follow}"
            + f"\n署名：\n{signature}"
            + f"\n等級：\t\t{lv}"
            + f"\n誕生日：\t\t{birthday}"
            + f"\n空間リンク：\t\t{url}"
        )
    elif lang == 4:
        output_message = (
            f"Die Anfrage wurde {t} Mal versucht."
            + f"\nNutzername:\t\t\t{nickname}"
            + f"\nUID:\t\t\t{user_id}"
            + f"\nGeschlecht:\t\t\t{gender}"
            + f"\nBig-Member-Status:\t\t\t{vip_status}"
            + f"\nStatus der Zertifizierung:\t\t\t{verification_status}"
            + f"\nKontostatus:\t\t\t{account_status}"
            + f"\nAnzahl der Follower:\t\t\t{fans}"
            + f"\nAnzahl der gefolgten Konten:\t\t\t{follow}"
            + f"\nSignatur:\n{signature}"
            + f"\nNiveau:\t\t\t{lv}"
            + f"\nGeburtstag: \t\t\t{birthday}"
            + f"\nLink des Bilibili-Raums:\t\t\t{url}"
        )
    elif lang == 5:
        output_message = (
            f"The request was attempted {t} time(s)."
            + f"\nNom d’utilisateur:\t\t\t{nickname}"
            + f"\nUID:\t\t\t{user_id}"
            + f"\nGenre:\t\t\t{gender}"
            + f"\nStatut Big Member:\t\t\t{vip_status}"
            + f"\nStatut de la certification:\t\t\t{verification_status}"
            + f"\nStatut du compte:\t\t\t{account_status}"
            + f"\nNombre de fans:\t\t\t{fans}"
            + f"\nNombre d’abonnements:\t\t\t{follow}"
            + f"\nSignature :\n{signature}"
            + f"\nNiveau:\t\t\t{lv}"
            + f"\nAnniversaire: \t\t\t{birthday}"
            + f"\nLien de l’espace Bilibili:\t\t\t{url}"
        )
    elif lang == 6:
        output_message = (
            f"The request was attempted {t} time(s)."
            + f"\nชื่อผู้ใช้:\t\t\t{nickname}"
            + f"\nยูไอดี:\t\t\t{user_id}"
            + f"\nเพศ:\t\t\t{gender}"
            + f"\nสถานะสมาชิกขนาดใหญ่:\t\t\t{vip_status}"
            + f"\nสถานะการรับรอง:\t\t\t{verification_status}"
            + f"\nสถานะบัญชี:\t\t\t{account_status}"
            + f"\nจํานวนแฟนๆ:\t\t\t{fans}"
            + f"\nจํานวนเงินที่ติดตาม:\t\t\t{follow}"
            + f"\nสัญลักษณ์:\n{signature}"
            + f"\nระดับ:\t\t\t{lv}"
            + f"\nวันเกิด: \t\t\t{birthday}"
            + f"\nลิงก์พื้นที่ Bilibili:\t\t\t{url}"
        )
    elif lang == 7:
        output_message = (
            f"The request was attempted {t} time(s)."
            + f"\n사용자 이름:\t\t\t{nickname}"
            + f"\n사용자 ID:\t\t\t{user_id}"
            + f"\n성별:\t\t\t{gender}"
            + f"\n빅 회원 상태:\t\t\t{vip_status}"
            + f"\n인증현황:\t\t\t{verification_status}"
            + f"\n계정 상태:\t\t\t{account_status}"
            + f"\n팬 금액:\t\t\t{fans}"
            + f"\n팔로우 금액:\t\t\t{follow}"
            + f"\n기호:\n{signature}"
            + f"\n수준:\t\t\t{lv}"
            + f"\n생일: \t\t\t{birthday}"
            + f"\n빌리빌리 스페이스 링크:\t\t\t{url}"
        )
    elif lang == 8:
        output_message = (
            f"The request was attempted {t} time(s)."
            + f"\nNickname:\t\t\t{nickname}"
            + f"\nUID:\t\t\t{user_id}"
            + f"\nGender:\t\t\t{gender}"
            + f"\nBig Member status:\t\t\t{vip_status}"
            + f"\nCertification status:\t\t\t{verification_status}"
            + f"\nAccount Status:\t\t\t{account_status}"
            + f"\nFans count:\t\t\t{fans}"
            + f"\nFollow count:\t\t\t{follow}"
            + f"\nSign:\n{signature}"
            + f"\nLevel:\t\t\t{lv}"
            + f"\nBirthday: \t\t\t{birthday}"
            + f"\nBilibili space link:\t\t\t{url}"
        )
    elif lang == 9:
        output_message = (
            f"The request was attempted {t} time(s)."
            + f"\nTên đăng nhập:\t\t\t{nickname}"
            + f"\nUID:\t\t\t{user_id}"
            + f"\nGiống:\t\t\t{gender}"
            + f"\nTrạng thái thành viên lớn:\t\t\t{vip_status}"
            + f"\nTình trạng chứng nhận:\t\t\t{verification_status}"
            + f"\nTrạng thái tài khoản:\t\t\t{account_status}"
            + f"\nSố tiền người hâm mộ:\t\t\t{fans}"
            + f"\nTheo dõi số tiền:\t\t\t{follow}"
            + f"\nDấu:\n{signature}"
            + f"\nMức:\t\t\t{lv}"
            + f"\nSinh nhật: \t\t\t{birthday}"
            + f"\nLiên kết không gian Bilibili:\t\t\t{url}"
        )
    elif lang == 10:
        output_message = (
            f"The request was attempted {t} time(s)."
            + f"\nNickname:\t\t\t{nickname}"
            + f"\nUID:\t\t\t{user_id}"
            + f"\nGender:\t\t\t{gender}"
            + f"\nBig Member status:\t\t\t{vip_status}"
            + f"\nCertification status:\t\t\t{verification_status}"
            + f"\nAccount Status:\t\t\t{account_status}"
            + f"\nFans count:\t\t\t{fans}"
            + f"\nFollow count:\t\t\t{follow}"
            + f"\nSign:\n{signature}"
            + f"\nLevel:\t\t\t{lv}"
            + f"\nBirthday: \t\t\t{birthday}"
            + f"\nBilibili space link:\t\t\t{url}"
        )
    elif lang == 11:
        output_message = (
            f"The request was attempted {t} time(s)."
            + f"\nNickname:\t\t\t{nickname}"
            + f"\nUID:\t\t\t{user_id}"
            + f"\nGender:\t\t\t{gender}"
            + f"\nBig Member status:\t\t\t{vip_status}"
            + f"\nCertification status:\t\t\t{verification_status}"
            + f"\nAccount Status:\t\t\t{account_status}"
            + f"\nFans count:\t\t\t{fans}"
            + f"\nFollow count:\t\t\t{follow}"
            + f"\nSign:\n{signature}"
            + f"\nLevel:\t\t\t{lv}"
            + f"\nBirthday: \t\t\t{birthday}"
            + f"\nBilibili space link:\t\t\t{url}"
        )
    elif lang == 12:
        output_message = (
            f"Permintaan itu dicoba untuk {t} kali."
            + f"\nNickname:\t\t\t{nickname}"
            + f"\nUID:\t\t\t{user_id}"
            + f"\nGender:\t\t\t{gender}"
            + f"\nBig Member status:\t\t\t{vip_status}"
            + f"\nCertification status:\t\t\t{verification_status}"
            + f"\nAccount Status:\t\t\t{account_status}"
            + f"\nFans count:\t\t\t{fans}"
            + f"\nFollow count:\t\t\t{follow}"
            + f"\nSign:\n{signature}"
            + f"\nLevel:\t\t\t{lv}"
            + f"\nBirthday: \t\t\t{birthday}"
            + f"\nBilibili space link:\t\t\t{url}"
        )
    if lang == 0:
        try:
            output_message += "\n" + UsersEgg.eggd[int(user_id)]
        except Exception:
            pass
    outsmall()
    output_text.insert(INSERT, output_message)
    output_text.configure(state=DISABLED)


def check_nickname() -> None:  # 查询昵称是否可用
    notice=[
        "6月20日测试时，此功能所用api已经出现异常，无论如何都会显示昵称可注册。请等待后续版本修复。",
        "On June 20th, during testing, the API used for this feature had already encountered an exception, and regardless, it would display that the nickname can be registered. Please wait for future versions to fix.",
        "6月20日測試時，此功能所用api已經出現異常，無論如何都會顯示暱稱可註冊。請等待後續版本修復。",
        "On June 20th, during testing, the API used for this feature had already encountered an exception, and regardless, it would display that the nickname can be registered. Please wait for future versions to fix.",
        "On June 20th, during testing, the API used for this feature had already encountered an exception, and regardless, it would display that the nickname can be registered. Please wait for future versions to fix.",
        "On June 20th, during testing, the API used for this feature had already encountered an exception, and regardless, it would display that the nickname can be registered. Please wait for future versions to fix.",
        "On June 20th, during testing, the API used for this feature had already encountered an exception, and regardless, it would display that the nickname can be registered. Please wait for future versions to fix.",
        "On June 20th, during testing, the API used for this feature had already encountered an exception, and regardless, it would display that the nickname can be registered. Please wait for future versions to fix.",
        "On June 20th, during testing, the API used for this feature had already encountered an exception, and regardless, it would display that the nickname can be registered. Please wait for future versions to fix.",
        "On June 20th, during testing, the API used for this feature had already encountered an exception, and regardless, it would display that the nickname can be registered. Please wait for future versions to fix.",
        "On June 20th, during testing, the API used for this feature had already encountered an exception, and regardless, it would display that the nickname can be registered. Please wait for future versions to fix.",
        "On June 20th, during testing, the API used for this feature had already encountered an exception, and regardless, it would display that the nickname can be registered. Please wait for future versions to fix.",
        "On June 20th, during testing, the API used for this feature had already encountered an exception, and regardless, it would display that the nickname can be registered. Please wait for future versions to fix.",
    ]
    showwarning(title=window_title, message=notice[lang])
    nniptl = [
        "输入一个昵称检查可用性...",
        "Input a nickname to check if it can be used...",
        "輸入一個暱稱檢查是否可用...",
        "ニックネームを入力して、使用できるかどうかを確認します...",
        "Geben Sie einen Spitznamen ein, um zu prüfen, ob er verwendet werden kann...",
        "Entrez un pseudo pour vérifier s’il peut être utilisé...",
        "Input a nickname to check if it can be used...",
        "Input a nickname to check if it can be used...",
        "Input a nickname to check if it can be used...",
        "Input a nickname to check if it can be used...",
        "Input a nickname to check if it can be used...",
        "Input a nickname to check if it can be used...",
        "Input a nickname to check if it can be used...",
    ]
    name = askstring(title=window_title, prompt=nniptl[lang])
    if name == None:
        return None
    url = "https://passport.bilibili.com/web/generic/check/nickname?nickName=" + name
    for t in range(1, MAX_RETRIES + 1):
        try:
            pg = request_api(url, headers=headers)
        except Exception as e:
            if t < MAX_RETRIES:
                pass
            else:
                error_text = str(e)
                error_msgs = [
                    f"请求尝试{t}次后仍然发生错误：{error_text}",
                    f"The request still failed after {t} attempts: {error_text}",
                    f"請求嘗試{t}次後仍然發生錯誤：{error_text}",
                    f"要求を {t} 回試行した後もエラーが発生しました： {error_text}",
                    f"Nach {t} Versuchen an der Anforderung trat immer noch ein Fehler auf: {error_text}",
                    f"Une erreur se produisait encore après {t} tentatives de requête : {error_text}",
                    f"ข้อผิดพลาดยังคงเกิดขึ้นหลังจาก {t} ครั้งของความพยายามที่คําขอ: {error_text}",
                    f"요청을 {t}번 시도한 후에도 오류가 계속 발생했습니다: {error_text}",
                    f"Ошибка по-прежнему возникала после {t} попыток выполнения запроса: {error_text}",
                    f"Vẫn xảy ra lỗi sau {t} lần thử yêu cầu: {error_text}",
                    f"Ainda ocorreu um erro após {t} vezes de tentativas na solicitação: {error_text}",
                    f"Todavía se ha producido un error después de {t} veces de intentos en la solicitud: {error_text}",
                    f"Kesalahan masih terjadi setelah {t} kali upaya permintaan: {error_text}",
                ]
                showwarning(title=window_title, message=error_msgs[lang])
                return None
        else:
            break
    response_data = read_api_response(pg)
    codes = api_code(response_data)
    if codes == 0:
        available_list = [
            "昵称可用",
            "Nickname can be used",
            "暱稱可用",
            "ニックネームは使用できます",
            "Spitzname kann verwendet werden",
            "Le surnom peut être utilisé",
            "Nickname can be used",
            "Nickname can be used",
            "Nickname can be used",
            "Nickname can be used",
            "Nickname can be used",
            "Nickname can be used",
            "Nickname can be used",
        ]
        showinfo(title=window_title, message=available_list[lang])
    else:
        msg = api_message(response_data) if lang == 0 else translated_api_message(codes, api_message(response_data))
        unavailable = [
            f"昵称不可用\n原因：{msg}({codes})",
            f"Nickname cannot be used\nReason: {msg}({codes})",
            f"暱稱不可用\n原因：{msg}({codes})",
            f"ニックネームは使用できません\n理由：{msg}({codes})",
            f"Spitzname kann nicht verwendet werden\nGrund: {msg}({codes})",
            f"Le surnom ne peut pas être utilisé\nRaison: {msg}({codes})",
            f"Nickname cannot be used\nReason: {msg}({codes})",
            f"Nickname cannot be used\nReason: {msg}({codes})",
            f"Nickname cannot be used\nReason: {msg}({codes})",
            f"Nickname cannot be used\nReason: {msg}({codes})",
            f"Nickname cannot be used\nReason: {msg}({codes})",
            f"Nickname cannot be used\nReason: {msg}({codes})",
            f"Nickname cannot be used\nReason: {msg}({codes})",
        ]
        showerror(title=window_title, message=unavailable[lang])


def query_video_info() -> None:  # 查询视频信息
    inptl = [
        "输入B站视频av号或BV号或者链接（不加av或BV按av号算，链接目前只支持BV）...",
        "Input Bilibili video AVID, BVID, or link (Without AV or BV at the beginning of the ID, it will be treated as an AVID. Link only supports BVID)...",
        "輸入B站影片av號或BV號或者連結（不加av或BV按av號算，連結目前只支援BV）...",
        "Input Bilibili video AVID, BVID, or link (Without AV or BV at the beginning of the ID, it will be treated as an AVID. Link only supports BVID)...",
        "Input Bilibili video AVID, BVID, or link (Without AV or BV at the beginning of the ID, it will be treated as an AVID. Link only supports BVID)...",
        "Input Bilibili video AVID, BVID, or link (Without AV or BV at the beginning of the ID, it will be treated as an AVID. Link only supports BVID)...",
        "Input Bilibili video AVID, BVID, or link (Without AV or BV at the beginning of the ID, it will be treated as an AVID. Link only supports BVID)...",
        "Input Bilibili video AVID, BVID, or link (Without AV or BV at the beginning of the ID, it will be treated as an AVID. Link only supports BVID)...",
        "Input Bilibili video AVID, BVID, or link (Without AV or BV at the beginning of the ID, it will be treated as an AVID. Link only supports BVID)...",
        "Input Bilibili video AVID, BVID, or link (Without AV or BV at the beginning of the ID, it will be treated as an AVID. Link only supports BVID)...",
        "Input Bilibili video AVID, BVID, or link (Without AV or BV at the beginning of the ID, it will be treated as an AVID. Link only supports BVID)...",
        "Input Bilibili video AVID, BVID, or link (Without AV or BV at the beginning of the ID, it will be treated as an AVID. Link only supports BVID)...",
        "Input Bilibili video AVID, BVID, or link (Without AV or BV at the beginning of the ID, it will be treated as an AVID. Link only supports BVID)...",
    ]
    vid = askstring(title=window_title, prompt=inptl[lang])
    if vid == None:
        return None
    lvid2 = ["av", "BV", "bv"]
    if vid[:4] == "http":
        try:
            vid = vid[vid.index("BV") :][:12]
        except Exception:
            vid = "ytdb"
    while vid != None and vid[0:2] not in lvid2 and not vid.isnumeric():
        if lang == 0:
            showwarning(title=window_title, message="请重新输入")
            vid = askstring(
                title=window_title,
                prompt="输入B站视频av号或BV号或者链接（不加av或BV按av号算，链接目前只支持BV）...",
            )
        elif lang == 1:
            showwarning(title=window_title, message="Please reinput")
            vid = askstring(
                title=window_title,
                prompt="Input Bilibili video AVID, BVID, or link (Without AV or BV at the beginning of the ID, it will be treated as an AVID. Link only supports BVID)......",
            )
        if vid == None:
            return None
        if vid[:4] == "http":
            try:
                vid = vid[vid.index("BV") :][:12]
            except Exception:
                vid = "ytdb"
    else:
        if vid == None:
            return None
        if vid[0:2] == "av" or vid[0:2] == "BV" or vid[0:2] == "bv":
            url = "https://www.bilibili.com/video/" + vid
        elif vid[0:1] in lvid1:
            url = "https://www.bilibili.com/video/av" + vid
        if vid[0:2] == "av":
            avid = vid[2:]
            detail_url = "https://api.bilibili.com/x/web-interface/view?aid=" + avid
        elif vid[0:1] in lvid1:
            avid = vid
            detail_url = "https://api.bilibili.com/x/web-interface/view?aid=" + vid
        elif vid[0:2] == "BV" or vid[0:2] == "bv":
            detail_url = "https://api.bilibili.com/x/web-interface/view?bvid=" + vid
        else:
            detail_url = "https://api.bilibili.com/x/web-interface/view?aid=1145141919810899999999999"
        for t in range(1, MAX_RETRIES + 1):
            try:
                page2 = request_api(detail_url, headers=headers)
            except Exception as e:
                if t < MAX_RETRIES:
                    pass
                else:
                    error_text = str(e)
                    error_msgs = [
                        f"请求尝试{t}次后仍然发生错误：{error_text}",
                        f"The request still failed after {t} attempts: {error_text}",
                        f"請求嘗試{t}次後仍然發生錯誤：{error_text}",
                        f"要求を {t} 回試行した後もエラーが発生しました： {error_text}",
                        f"Nach {t} Versuchen an der Anforderung trat immer noch ein Fehler auf: {error_text}",
                        f"Une erreur se produisait encore après {t} tentatives de requête : {error_text}",
                        f"ข้อผิดพลาดยังคงเกิดขึ้นหลังจาก {t} ครั้งของความพยายามที่คําขอ: {error_text}",
                        f"요청을 {t}번 시도한 후에도 오류가 계속 발생했습니다: {error_text}",
                        f"Ошибка по-прежнему возникала после {t} попыток выполнения запроса: {error_text}",
                        f"Vẫn xảy ra lỗi sau {t} lần thử yêu cầu: {error_text}",
                        f"Ainda ocorreu um erro após {t} vezes de tentativas na solicitação: {error_text}",
                        f"Todavía se ha producido un error después de {t} veces de intentos en la solicitud: {error_text}",
                        f"Kesalahan masih terjadi setelah {t} kali upaya permintaan: {error_text}",
                    ]
                    showwarning(title=window_title, message=error_msgs[lang])
                    return None
            else:
                break
        soup2 = read_api_response(page2)
        status_code = api_code(soup2)
        if status_code != 0:
            msge = api_message(soup2)
            if lang != 0:
                msge = translated_api_message(status_code, msge)
            if msge == "啥都木有":
                if lang == 0:
                    msge = "视频不存在"
                elif lang == 1:
                    msge = "The video does not exist"
            showwarning(title=window_title, message=f"{msge} ({status_code})")
            return
        else:
            data2 = soup2["data"]
            vid = data2["bvid"]
            avid = data2["aid"]
            evaluate = data2["desc"]
            tit = data2["title"]
            dura = "%02d:%02d" % divmod(data2["duration"], 60)
            pubd = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data2["ctime"]))
            stat2 = data2["stat"]
            view, danmaku, reply, like, favo, coin, name, user_id = (
                stat2["view"],
                stat2["danmaku"],
                stat2["reply"],
                stat2["like"],
                stat2["favorite"],
                stat2["coin"],
                data2["owner"]["name"],
                data2["owner"]["mid"],
            )
            outsmall()
            attempt_msg = [
                f"请求共尝试了{t}次。\n",
                f"The request was attempted {t} time(s).\n",
                f"請求共嘗試了{t}次。\n",
                f"要求は {t} 回試行されました。\n",
                f"Die Anfrage wurde {t} Mal versucht.\n",
                f"La demande a été tentée {t} fois.\n",
                f"คําขอถูกพยายามเป็นเวลา {t} ครั้ง\n",
                f"요청이 {t}번 시도되었습니다.\n",
                f"Запрос был выполнен в течение {t} раз.\n",
                f"Yêu cầu đã được cố gắng cho {t} lần.\n",
                f"O pedido foi tentado por {t} vezes.\n",
                f"La solicitud se intentó {t} veces.\n",
                f"Permintaan itu dicoba untuk {t} kali.\n",
            ]
            output_text.insert(INSERT, attempt_msg[lang])
            if lang == 0:
                output_text.insert(
                    INSERT,
                    f"标题：\t\t{tit}"
                    + f"\nav号：\t\tav{avid}"
                    + f"\nBV号：\t\t{vid}"
                    + f"\n简介：\n{evaluate}"
                    + f"\n播放量：\t\t{view}"
                    + f"\n弹幕数量：\t\t{danmaku}"
                    + f"\n评论数量：\t\t{reply}"
                    + f"\n点赞数量：\t\t{like}"
                    + f"\n收藏数量：\t\t{favo}"
                    + f"\n投币数量：\t\t{coin}"
                    + f"\n视频总时长：\t\t{dura}"
                    + f"\n发布时间：\t\t{pubd}"
                    + f"\nUP主昵称：\t\t{name}"
                    + f"\nUP主UID：\t\t{user_id}"
                    + f"\n视频链接：\t\thttps://www.bilibili.com/video/av{avid}"
                    + f"\nUP主空间：\t\thttps://space.bilibili.com/{user_id}",
                )
            elif lang == 1:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{tit}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{vid}"
                    + f"\nIntroduction:\n{evaluate}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nDanmaku count:\t\t\t{danmaku}"
                    + f"\nComment count:\t\t\t{reply}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nVideo duration:\t\t\t{dura}"
                    + f"\nRelease time:\t\t\t{pubd}"
                    + f"\nUP master's nickname:\t\t\t{name}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{avid}"
                    + f"\nUP master's space link:\t\t\thttps://space.bilibili.com/{user_id}",
                )
            elif lang == 2:
                output_text.insert(
                    INSERT,
                    f"標題：\t\t{to_traditional(tit)}"
                    + f"\nav號：\t\tav{avid}"
                    + f"\nBV號：\t\t{vid}"
                    + f"\n簡介：\n{to_traditional(evaluate)}"
                    + f"\n播放量：\t\t{view}"
                    + f"\n彈幕數量：\t\t{danmaku}"
                    + f"\n評論數量：\t\t{reply}"
                    + f"\n點贊數量：\t\t{like}"
                    + f"\n收藏數量：\t\t{favo}"
                    + f"\n投幣數量：\t\t{coin}"
                    + f"\n影片總時長：\t\t{dura}"
                    + f"\n釋出時間：\t\t{pubd}"
                    + f"\nUP主暱稱：\t\t{name}"
                    + f"\nUP主UID：\t\t{user_id}"
                    + f"\n影片連結：\t\thttps://www.bilibili.com/video/av{avid}"
                    + f"\nUP主空間：\t\thttps://space.bilibili.com/{user_id}",
                )
            elif lang == 3:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{tit}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{vid}"
                    + f"\nIntroduction:\n{evaluate}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nDanmaku count:\t\t\t{danmaku}"
                    + f"\nComment count:\t\t\t{reply}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nVideo duration:\t\t\t{dura}"
                    + f"\nRelease time:\t\t\t{pubd}"
                    + f"\nUP master's nickname:\t\t\t{name}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{avid}"
                    + f"\nUP master's space link:\t\t\thttps://space.bilibili.com/{user_id}",
                )
            elif lang == 4:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{tit}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{vid}"
                    + f"\nIntroduction:\n{evaluate}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nDanmaku count:\t\t\t{danmaku}"
                    + f"\nComment count:\t\t\t{reply}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nVideo duration:\t\t\t{dura}"
                    + f"\nRelease time:\t\t\t{pubd}"
                    + f"\nUP master's nickname:\t\t\t{name}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{avid}"
                    + f"\nUP master's space link:\t\t\thttps://space.bilibili.com/{user_id}",
                )
            elif lang == 5:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{tit}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{vid}"
                    + f"\nIntroduction:\n{evaluate}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nDanmaku count:\t\t\t{danmaku}"
                    + f"\nComment count:\t\t\t{reply}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nVideo duration:\t\t\t{dura}"
                    + f"\nRelease time:\t\t\t{pubd}"
                    + f"\nUP master's nickname:\t\t\t{name}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{avid}"
                    + f"\nUP master's space link:\t\t\thttps://space.bilibili.com/{user_id}",
                )
            elif lang == 6:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{tit}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{vid}"
                    + f"\nIntroduction:\n{evaluate}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nDanmaku count:\t\t\t{danmaku}"
                    + f"\nComment count:\t\t\t{reply}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nVideo duration:\t\t\t{dura}"
                    + f"\nRelease time:\t\t\t{pubd}"
                    + f"\nUP master's nickname:\t\t\t{name}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{avid}"
                    + f"\nUP master's space link:\t\t\thttps://space.bilibili.com/{user_id}",
                )
            elif lang == 7:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{tit}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{vid}"
                    + f"\nIntroduction:\n{evaluate}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nDanmaku count:\t\t\t{danmaku}"
                    + f"\nComment count:\t\t\t{reply}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nVideo duration:\t\t\t{dura}"
                    + f"\nRelease time:\t\t\t{pubd}"
                    + f"\nUP master's nickname:\t\t\t{name}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{avid}"
                    + f"\nUP master's space link:\t\t\thttps://space.bilibili.com/{user_id}",
                )
            elif lang == 8:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{tit}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{vid}"
                    + f"\nIntroduction:\n{evaluate}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nDanmaku count:\t\t\t{danmaku}"
                    + f"\nComment count:\t\t\t{reply}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nVideo duration:\t\t\t{dura}"
                    + f"\nRelease time:\t\t\t{pubd}"
                    + f"\nUP master's nickname:\t\t\t{name}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{avid}"
                    + f"\nUP master's space link:\t\t\thttps://space.bilibili.com/{user_id}",
                )
            elif lang == 9:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{tit}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{vid}"
                    + f"\nIntroduction:\n{evaluate}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nDanmaku count:\t\t\t{danmaku}"
                    + f"\nComment count:\t\t\t{reply}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nVideo duration:\t\t\t{dura}"
                    + f"\nRelease time:\t\t\t{pubd}"
                    + f"\nUP master's nickname:\t\t\t{name}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{avid}"
                    + f"\nUP master's space link:\t\t\thttps://space.bilibili.com/{user_id}",
                )
            elif lang == 10:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{tit}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{vid}"
                    + f"\nIntroduction:\n{evaluate}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nDanmaku count:\t\t\t{danmaku}"
                    + f"\nComment count:\t\t\t{reply}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nVideo duration:\t\t\t{dura}"
                    + f"\nRelease time:\t\t\t{pubd}"
                    + f"\nUP master's nickname:\t\t\t{name}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{avid}"
                    + f"\nUP master's space link:\t\t\thttps://space.bilibili.com/{user_id}",
                )
            elif lang == 11:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{tit}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{vid}"
                    + f"\nIntroduction:\n{evaluate}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nDanmaku count:\t\t\t{danmaku}"
                    + f"\nComment count:\t\t\t{reply}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nVideo duration:\t\t\t{dura}"
                    + f"\nRelease time:\t\t\t{pubd}"
                    + f"\nUP master's nickname:\t\t\t{name}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{avid}"
                    + f"\nUP master's space link:\t\t\thttps://space.bilibili.com/{user_id}",
                )
            elif lang == 12:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{tit}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{vid}"
                    + f"\nIntroduction:\n{evaluate}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nDanmaku count:\t\t\t{danmaku}"
                    + f"\nComment count:\t\t\t{reply}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nVideo duration:\t\t\t{dura}"
                    + f"\nRelease time:\t\t\t{pubd}"
                    + f"\nUP master's nickname:\t\t\t{name}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{avid}"
                    + f"\nUP master's space link:\t\t\thttps://space.bilibili.com/{user_id}",
                )
            output_text.configure(state=DISABLED)


def query_column_info() -> None:  # 查询专栏信息
    iptl = [
        "输入B站专栏cv号（不加cv）...",
        'Input Bilibili column CVID (Do not add "cv" at the beginning)...',
        "輸入B站專欄cv號（不加cv）...",
        "BilibiliコラムのCV番号を入力（cvは不要）...",
        "Bilibili-Kolumnen-CVID eingeben (ohne „cv“)...",
        "Saisissez le CVID de la colonne Bilibili (sans « cv »)...",
        "ป้อนหมายเลข CVID ของคอลัมน์ Bilibili (ไม่ต้องใส่ cv)...",
        "Bilibili 칼럼 CVID 입력(cv 제외)...",
        "Введите CVID колонки Bilibili (без «cv»)...",
        "Nhập CVID của bài viết Bilibili (không cần nhập cv)...",
        "Introduza o CVID da coluna Bilibili (sem «cv»)...",
        "Introduce el CVID de la columna de Bilibili (sin «cv»)...",
        "Masukkan CVID kolom Bilibili (tanpa cv)...",
    ]
    cid = askinteger(title=window_title, prompt=iptl[lang])
    if cid == None:
        return None
    detail_url = f"https://api.bilibili.com/x/article/viewinfo?id={cid}"
    for t in range(1, MAX_RETRIES + 1):
        try:
            page2 = request_api(detail_url, headers=headers)
        except Exception as e:
            if t < MAX_RETRIES:
                pass
            else:
                error_text = str(e)
                error_msgs = [
                    f"请求尝试{t}次后仍然发生错误：{error_text}",
                    f"The request still failed after {t} attempts: {error_text}",
                    f"請求嘗試{t}次後仍然發生錯誤：{error_text}",
                    f"要求を {t} 回試行した後もエラーが発生しました： {error_text}",
                    f"Nach {t} Versuchen an der Anforderung trat immer noch ein Fehler auf: {error_text}",
                    f"Une erreur se produisait encore après {t} tentatives de requête : {error_text}",
                    f"ข้อผิดพลาดยังคงเกิดขึ้นหลังจาก {t} ครั้งของความพยายามที่คําขอ: {error_text}",
                    f"요청을 {t}번 시도한 후에도 오류가 계속 발생했습니다: {error_text}",
                    f"Ошибка по-прежнему возникала после {t} попыток выполнения запроса: {error_text}",
                    f"Vẫn xảy ra lỗi sau {t} lần thử yêu cầu: {error_text}",
                    f"Ainda ocorreu um erro após {t} vezes de tentativas na solicitação: {error_text}",
                    f"Todavía se ha producido un error después de {t} veces de intentos en la solicitud: {error_text}",
                    f"Kesalahan masih terjadi setelah {t} kali upaya permintaan: {error_text}",
                ]
                showwarning(title=window_title, message=error_msgs[lang])
                return None
        else:
            break
    soup2 = read_api_response(page2)
    status_code = api_code(soup2)
    if status_code != 0:
        msge = api_message(soup2)
        warnl = [
            f"由于 {msge}({status_code}) ，信息获取失败！",
            f"Due to {msge}({status_code}), failed to get information!",
            f"由於 {msge}({status_code}) ，資訊獲取失敗！",
            f"Due to {msge}({status_code}), failed to get information!",
            f"Due to {msge}({status_code}), failed to get information!",
            f"Due to {msge}({status_code}), failed to get information!",
            f"Due to {msge}({status_code}), failed to get information!",
            f"Due to {msge}({status_code}), failed to get information!",
            f"Due to {msge}({status_code}), failed to get information!",
            f"Due to {msge}({status_code}), failed to get information!",
            f"Due to {msge}({status_code}), failed to get information!",
            f"Due to {msge}({status_code}), failed to get information!",
            f"Due to {msge}({status_code}), failed to get information!",
        ]
        showwarning(title=window_title, message=warnl[lang])
    else:
        data = soup2["data"]
        stat = data["stats"]
        tit = data["title"]
        view = stat["view"]
        favo = stat["favorite"]
        like = stat["like"]
        authid = data["mid"]
        auth = data["author_name"]
        reply = stat["reply"]
        coin = stat["coin"]
        share = stat["share"]
        dyna = stat["dynamic"]
        article_types = {0: "文章", 2: "笔记"} if lang == LANG_CN else (
            {0: "文章", 2: "筆記"} if lang == LANG_TC else {0: "Article", 2: "Note"}
        )
        tpe = article_types.get(data.get("type"), "—")
        outsmall()
        attempt_msg = [
            f"请求共尝试了{t}次。\n",
            f"The request was attempted {t} time(s).\n",
            f"請求共嘗試了{t}次。\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"Permintaan itu dicoba untuk {t} kali.\n",
        ]
        output_text.insert(INSERT, attempt_msg[lang])
        if lang == 0:
            output_text.insert(
                INSERT,
                f"标题：\t\t{tit}"
                + f"\nCV号：\t\tcv{cid}"
                + f"\n阅读量：\t\t{view}"
                + f"\n评论数量：\t\t{reply}"
                + f"\n点赞数量：\t\t{like}"
                + f"\n投币数量：\t\t{coin}"
                + f"\n收藏数量：\t\t{favo}"
                + f"\n分享数量：\t\t{share}"
                + f"\n动态转发数量：\t\t{dyna}"
                + f"\n专栏类型：\t\t{tpe}"
                + f"\nUP主昵称：\t\t{auth}"
                + f"\nUP主UID：\t\t{authid}"
                + f"\n专栏网站：\t\thttps://www.bilibili.com/read/cv{cid}"
                + f"\nUP主空间：\t\thttps://space.bilibili.com/{authid}",
            )
        elif lang == 1:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{tit}"
                + f"\nCVID:\t\t\t\tcv{cid}"
                + f"\nView count:\t\t\t\t{view}"
                + f"\nComment count:\t\t\t\t{reply}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nShare count:\t\t\t\t{share}"
                + f"\nDynamic share count:\t\t\t\t{dyna}"
                + f"\nColumn type:\t\t\t\t{tpe}"
                + f"\nUP master's nickname:\t\t\t\t{auth}"
                + f"\nUP master's UID:\t\t\t\t{authid}"
                + f"\nColumn link:\t\t\t\thttps://www.bilibili.com/read/cv{cid}"
                + f"\nUP master's space:\t\t\t\thttps://space.bilibili.com/{authid}",
            )
        elif lang == 2:
            output_text.insert(
                INSERT,
                f"標題：\t\t{tit}"
                + f"\nCV號：\t\tcv{cid}"
                + f"\n閱讀量：\t\t{view}"
                + f"\n評論數量：\t\t{reply}"
                + f"\n點贊數量：\t\t{like}"
                + f"\n投幣數量：\t\t{coin}"
                + f"\n收藏數量：\t\t{favo}"
                + f"\n分享數量：\t\t{share}"
                + f"\n動態轉發數量：\t\t{dyna}"
                + f"\n專欄類型：\t\t{tpe}"
                + f"\nUP主暱稱：\t\t{auth}"
                + f"\nUP主UID：\t\t{authid}"
                + f"\n專欄網站：\t\thttps://www.bilibili.com/read/cv{cid}"
                + f"\nUP主空間：\t\thttps://space.bilibili.com/{authid}",
            )
        elif lang == 3:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{tit}"
                + f"\nCVID:\t\t\t\tcv{cid}"
                + f"\nView count:\t\t\t\t{view}"
                + f"\nComment count:\t\t\t\t{reply}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nShare count:\t\t\t\t{share}"
                + f"\nDynamic share count:\t\t\t\t{dyna}"
                + f"\nColumn type:\t\t\t\t{tpe}"
                + f"\nUP master's nickname:\t\t\t\t{auth}"
                + f"\nUP master's UID:\t\t\t\t{authid}"
                + f"\nColumn link:\t\t\t\thttps://www.bilibili.com/read/cv{cid}"
                + f"\nUP master's space:\t\t\t\thttps://space.bilibili.com/{authid}",
            )
        elif lang == 4:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{tit}"
                + f"\nCVID:\t\t\t\tcv{cid}"
                + f"\nView count:\t\t\t\t{view}"
                + f"\nComment count:\t\t\t\t{reply}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nShare count:\t\t\t\t{share}"
                + f"\nDynamic share count:\t\t\t\t{dyna}"
                + f"\nColumn type:\t\t\t\t{tpe}"
                + f"\nUP master's nickname:\t\t\t\t{auth}"
                + f"\nUP master's UID:\t\t\t\t{authid}"
                + f"\nColumn link:\t\t\t\thttps://www.bilibili.com/read/cv{cid}"
                + f"\nUP master's space:\t\t\t\thttps://space.bilibili.com/{authid}",
            )
        elif lang == 5:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{tit}"
                + f"\nCVID:\t\t\t\tcv{cid}"
                + f"\nView count:\t\t\t\t{view}"
                + f"\nComment count:\t\t\t\t{reply}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nShare count:\t\t\t\t{share}"
                + f"\nDynamic share count:\t\t\t\t{dyna}"
                + f"\nColumn type:\t\t\t\t{tpe}"
                + f"\nUP master's nickname:\t\t\t\t{auth}"
                + f"\nUP master's UID:\t\t\t\t{authid}"
                + f"\nColumn link:\t\t\t\thttps://www.bilibili.com/read/cv{cid}"
                + f"\nUP master's space:\t\t\t\thttps://space.bilibili.com/{authid}",
            )
        elif lang == 6:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{tit}"
                + f"\nCVID:\t\t\t\tcv{cid}"
                + f"\nView count:\t\t\t\t{view}"
                + f"\nComment count:\t\t\t\t{reply}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nShare count:\t\t\t\t{share}"
                + f"\nDynamic share count:\t\t\t\t{dyna}"
                + f"\nColumn type:\t\t\t\t{tpe}"
                + f"\nUP master's nickname:\t\t\t\t{auth}"
                + f"\nUP master's UID:\t\t\t\t{authid}"
                + f"\nColumn link:\t\t\t\thttps://www.bilibili.com/read/cv{cid}"
                + f"\nUP master's space:\t\t\t\thttps://space.bilibili.com/{authid}",
            )
        elif lang == 7:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{tit}"
                + f"\nCVID:\t\t\t\tcv{cid}"
                + f"\nView count:\t\t\t\t{view}"
                + f"\nComment count:\t\t\t\t{reply}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nShare count:\t\t\t\t{share}"
                + f"\nDynamic share count:\t\t\t\t{dyna}"
                + f"\nColumn type:\t\t\t\t{tpe}"
                + f"\nUP master's nickname:\t\t\t\t{auth}"
                + f"\nUP master's UID:\t\t\t\t{authid}"
                + f"\nColumn link:\t\t\t\thttps://www.bilibili.com/read/cv{cid}"
                + f"\nUP master's space:\t\t\t\thttps://space.bilibili.com/{authid}",
            )
        elif lang == 8:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{tit}"
                + f"\nCVID:\t\t\t\tcv{cid}"
                + f"\nView count:\t\t\t\t{view}"
                + f"\nComment count:\t\t\t\t{reply}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nShare count:\t\t\t\t{share}"
                + f"\nDynamic share count:\t\t\t\t{dyna}"
                + f"\nColumn type:\t\t\t\t{tpe}"
                + f"\nUP master's nickname:\t\t\t\t{auth}"
                + f"\nUP master's UID:\t\t\t\t{authid}"
                + f"\nColumn link:\t\t\t\thttps://www.bilibili.com/read/cv{cid}"
                + f"\nUP master's space:\t\t\t\thttps://space.bilibili.com/{authid}",
            )
        elif lang == 9:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{tit}"
                + f"\nCVID:\t\t\t\tcv{cid}"
                + f"\nView count:\t\t\t\t{view}"
                + f"\nComment count:\t\t\t\t{reply}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nShare count:\t\t\t\t{share}"
                + f"\nDynamic share count:\t\t\t\t{dyna}"
                + f"\nColumn type:\t\t\t\t{tpe}"
                + f"\nUP master's nickname:\t\t\t\t{auth}"
                + f"\nUP master's UID:\t\t\t\t{authid}"
                + f"\nColumn link:\t\t\t\thttps://www.bilibili.com/read/cv{cid}"
                + f"\nUP master's space:\t\t\t\thttps://space.bilibili.com/{authid}",
            )
        elif lang == 10:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{tit}"
                + f"\nCVID:\t\t\t\tcv{cid}"
                + f"\nView count:\t\t\t\t{view}"
                + f"\nComment count:\t\t\t\t{reply}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nShare count:\t\t\t\t{share}"
                + f"\nDynamic share count:\t\t\t\t{dyna}"
                + f"\nColumn type:\t\t\t\t{tpe}"
                + f"\nUP master's nickname:\t\t\t\t{auth}"
                + f"\nUP master's UID:\t\t\t\t{authid}"
                + f"\nColumn link:\t\t\t\thttps://www.bilibili.com/read/cv{cid}"
                + f"\nUP master's space:\t\t\t\thttps://space.bilibili.com/{authid}",
            )
        elif lang == 11:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{tit}"
                + f"\nCVID:\t\t\t\tcv{cid}"
                + f"\nView count:\t\t\t\t{view}"
                + f"\nComment count:\t\t\t\t{reply}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nShare count:\t\t\t\t{share}"
                + f"\nDynamic share count:\t\t\t\t{dyna}"
                + f"\nColumn type:\t\t\t\t{tpe}"
                + f"\nUP master's nickname:\t\t\t\t{auth}"
                + f"\nUP master's UID:\t\t\t\t{authid}"
                + f"\nColumn link:\t\t\t\thttps://www.bilibili.com/read/cv{cid}"
                + f"\nUP master's space:\t\t\t\thttps://space.bilibili.com/{authid}",
            )
        elif lang == 12:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{tit}"
                + f"\nCVID:\t\t\t\tcv{cid}"
                + f"\nView count:\t\t\t\t{view}"
                + f"\nComment count:\t\t\t\t{reply}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nShare count:\t\t\t\t{share}"
                + f"\nDynamic share count:\t\t\t\t{dyna}"
                + f"\nColumn type:\t\t\t\t{tpe}"
                + f"\nUP master's nickname:\t\t\t\t{auth}"
                + f"\nUP master's UID:\t\t\t\t{authid}"
                + f"\nColumn link:\t\t\t\thttps://www.bilibili.com/read/cv{cid}"
                + f"\nUP master's space:\t\t\t\thttps://space.bilibili.com/{authid}",
            )
        output_text.config(state=DISABLED)


def query_media_info() -> None:  # 查询影视信息
    bid = askstring(title=window_title, prompt="输入B站影视ss/ep/md代码（请加前缀用以区分）...")
    bid = bid.lower()
    bangumid = ["ss", "md", "ep"]
    while bid[0:2] not in bangumid and bid != None:
        showwarning(title=window_title, message="请重新输入")
        bid = askstring(title=window_title, prompt="输入B站影视ss/ep/md代码（请加前缀用以区分）...")
    if bid == None:
        return None
    else:
        bid = bid.lower()
        if bid[0:2] == "ss":
            bid = bid[2:]
            tpe = 1
            codm = 0
        elif bid[0:2] == "ep":
            bid = bid[2:]
            tpe = 2
            codm = 0
        elif bid[0:2] == "md":
            mid = bid[2:]
            url3 = "https://api.bilibili.com/pgc/review/user?media_id=" + mid
            page3 = request_api(url3, headers=headers)
            soup3 = read_api_response(page3)
            codm = api_code(soup3)
            if codm != 0:
                errt1 = api_message(soup3)
            else:
                resultm = soup3["result"]["media"]
                bid = resultm["season_id"]
                tpe = 1
        if codm != 0:
            showwarning(
                title=window_title,
                message="由于 " + errt1 + "(" + str(codm) + ") ，信息获取失败！",
            )
        else:
            if tpe == 1:
                detail_url = "https://api.bilibili.com/pgc/view/web/season?season_id=" + str(
                    bid
                )
            elif tpe == 2:
                detail_url = "https://api.bilibili.com/pgc/view/web/season?ep_id=" + str(bid)
            page2 = request_api(detail_url, headers=headers)
            soup2 = read_api_response(page2)
            status_code = api_code(soup2)
            msge = api_message(soup2)
            if status_code != 0:
                showwarning(
                    title=window_title,
                    message="由于 " + msge + "(" + str(status_code) + ") ，信息获取失败！",
                )
            else:
                resl = soup2["result"]
                eva = resl["evaluate"]
                tit = resl["title"]
                stat = resl["stat"]
                view = stat["views"]
                fav = stat["favorites"]
                coin = stat["coins"]
                dmk = stat["danmakus"]
                mid = resl["media_id"]
                styles = resl["styles"]
                style = ""
                for i in styles:
                    style += i + "  "
                actors = resl["actors"].replace("\n", "\n\t\t")
                try:
                    sc = resl["rating"]["score"]
                except Exception:
                    sc = "<暂无评分>"
                tot = resl["total"]
                region = resl["areas"][0]["name"]
                if tot == -1:
                    tot = "<未完结>"
                outpt()
                output_text.insert(
                    INSERT,
                    f"标题：\t\t{tit}"
                    + f"\nss号或对应集ep号：\t\t{bid}"
                    + f"\nmd号：\t\t{mid}"
                    + f"\n简介：\n{eva}"
                    + f"\n评分：\t\t{sc}"
                    + f"\n风格：\t\t{style}"
                    + f"\n配音演员列表：\t\t{actors}"
                    + f"\n地区：\t\t{region}"
                    + f"\n总集数：\t\t{tot}"
                    + f"\n播放量：\t\t{view}"
                    + f"\n弹幕数量：\t\t{dmk}"
                    + f"\n追番人数：\t\t{fav}"
                    + f"\n投币数量：\t\t{coin}",
                )
                output_text.config(state=DISABLED)


def convert_av_to_bv() -> None:  # AV号转BV号
    if not avbv_available:
        moduleloss = [
            "avbv.py插件缺失",
            "Missing plugin avbv.py",
            "avbv.py插件遺失",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
        ]
        showwarning(title=window_title, message=moduleloss[lang])
        return None
    infor = [
        "此功能摘自github的12345-mcpython，若有侵权请联系删除。",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "這個功能為github上的12345-mcpython所提供，若有侵權請聯繫刪除。",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
    ]
    vipt = [
        ("输入B站视频AV号（不加 av）...", "AV号非法！", "BV号：\n"),
        (
            "Input Bilibili video AV ID (Don't add AV at the beginning)...",
            "Invalid AV ID!",
            "BV ID:\n",
        ),
        ("輸入B站視頻AV號（不加 av）...", "AV號非法！", "BV號：\n"),
        (
            "Input Bilibili video AV ID (Don't add AV at the beginning)...",
            "Invalid AV ID!",
            "BV ID:\n",
        ),
        (
            "Input Bilibili video AV ID (Don't add AV at the beginning)...",
            "Invalid AV ID!",
            "BV ID:\n",
        ),
        (
            "Input Bilibili video AV ID (Don't add AV at the beginning)...",
            "Invalid AV ID!",
            "BV ID:\n",
        ),
        (
            "Input Bilibili video AV ID (Don't add AV at the beginning)...",
            "Invalid AV ID!",
            "BV ID:\n",
        ),
        (
            "Input Bilibili video AV ID (Don't add AV at the beginning)...",
            "Invalid AV ID!",
            "BV ID:\n",
        ),
        (
            "Input Bilibili video AV ID (Don't add AV at the beginning)...",
            "Invalid AV ID!",
            "BV ID:\n",
        ),
        (
            "Input Bilibili video AV ID (Don't add AV at the beginning)...",
            "Invalid AV ID!",
            "BV ID:\n",
        ),
        (
            "Input Bilibili video AV ID (Don't add AV at the beginning)...",
            "Invalid AV ID!",
            "BV ID:\n",
        ),
        (
            "Input Bilibili video AV ID (Don't add AV at the beginning)...",
            "Invalid AV ID!",
            "BV ID:\n",
        ),
        (
            "Input Bilibili video AV ID (Don't add AV at the beginning)...",
            "Invalid AV ID!",
            "BV ID:\n",
        ),
    ]
    showinfo(title=window_title, message=infor[lang])
    vid = askinteger(title=window_title, prompt=vipt[lang][0])
    if vid == None:
        return None
    try:
        bvid = av2bv(vid)
    except Exception:
        showwarning(title=window_title, message=vipt[lang][1])
    else:
        outpt(2, 25)
        output_text.insert(INSERT, vipt[lang][2] + str(bvid))
        output_text.config(state=DISABLED)


def convert_bv_to_av() -> None:  # BV号转AV号
    if not avbv_available:
        moduleloss = [
            "avbv.py插件缺失",
            "Missing plugin avbv.py",
            "avbv.py插件遺失",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
            "Missing plugin avbv.py",
        ]
        showwarning(title=window_title, message=moduleloss[lang])
        return None
    infor = [
        "此功能摘自github的12345-mcpython，若有侵权请联系删除。",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "這個功能為github上的12345-mcpython所提供，若有侵權請聯繫刪除。",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
        "This feature is taken from 12345-mcpython on Github. If there is any infringement, please contact to remove it.",
    ]
    vipt = [
        ("输入B站视频BV号（需以 BV 开头）...", "BV号需以 BV 开头，请重新输入", "BV号非法！", "av号：\n"),
        (
            "Input Bilibili video BV ID...",
            "Please reinput",
            "Invalid BV ID!",
            "AV ID:\n",
        ),
        ("輸入B站視頻BV號（需以 BV 開頭）...", "BV號需以 BV 開頭，請重新輸入", "BV號非法！", "av號：\n"),
        (
            "Input Bilibili video BV ID...",
            "Please reinput",
            "Invalid BV ID!",
            "AV ID:\n",
        ),
        (
            "Input Bilibili video BV ID...",
            "Please reinput",
            "Invalid BV ID!",
            "AV ID:\n",
        ),
        (
            "Input Bilibili video BV ID...",
            "Please reinput",
            "Invalid BV ID!",
            "AV ID:\n",
        ),
        (
            "Input Bilibili video BV ID...",
            "Please reinput",
            "Invalid BV ID!",
            "AV ID:\n",
        ),
        (
            "Input Bilibili video BV ID...",
            "Please reinput",
            "Invalid BV ID!",
            "AV ID:\n",
        ),
        (
            "Input Bilibili video BV ID...",
            "Please reinput",
            "Invalid BV ID!",
            "AV ID:\n",
        ),
        (
            "Input Bilibili video BV ID...",
            "Please reinput",
            "Invalid BV ID!",
            "AV ID:\n",
        ),
        (
            "Input Bilibili video BV ID...",
            "Please reinput",
            "Invalid BV ID!",
            "AV ID:\n",
        ),
        (
            "Input Bilibili video BV ID...",
            "Please reinput",
            "Invalid BV ID!",
            "AV ID:\n",
        ),
        (
            "Input Bilibili video BV ID...",
            "Please reinput",
            "Invalid BV ID!",
            "AV ID:\n",
        ),
    ]
    showinfo(title=window_title, message=infor[lang])
    vid = askstring(title=window_title, prompt=vipt[lang][0])
    if vid == None:
        return None
    lvid2 = ["BV", "bv"]
    while vid[0:2] not in lvid2:
        showwarning(title=window_title, message=vipt[lang][1])
        vid = askstring(title=window_title, prompt=vipt[lang][0])
        if vid == None:
            return None
    else:
        if vid == None:
            return None
        try:
            avid = bv2av(vid)
        except Exception:
            showwarning(title=window_title, message=vipt[lang][2])
        else:
            outpt(2, 25)
            output_text.insert(INSERT, vipt[lang][3] + str(avid))
            output_text.config(state=DISABLED)


def get_wallpaper() -> None:  # 获取APP首页壁纸
    # 此接口会拒绝普通浏览器请求（HTTP 412）；使用 APP 请求头并保留正确的 sign 参数。
    url = "https://app.bilibili.com/x/v2/splash/brand/list?appkey=1d8b6e7d45233436&ts=0&sign=78a89e153cd6231a4a4d55013aa063ce"
    wallpaper_headers = {
        "User-Agent": "Mozilla/5.0 BiliDroid/7.16.0 (bbcallen@gmail.com)",
        "Referer": "https://www.bilibili.com/",
    }
    try:
        page = request_api(url, headers=wallpaper_headers, timeout=10)
        ls = api_data(page).get("list") or []
    except Exception as error:
        showwarning(title=window_title, message=f"获取开屏壁纸失败：{error}")
        return None
    outpt()
    output_text.configure(tabs=(round(60 * dpi_scale), round(260 * dpi_scale)))
    output_text.tag_configure("wallpaper_link", foreground="#0a58ca", underline=True)

    def open_wallpaper_link(event) -> None:
        """在默认浏览器中打开被点击的壁纸链接。"""
        click_index = output_text.index(f"@{event.x},{event.y}")
        ranges = output_text.tag_ranges("wallpaper_link")
        for start, end in zip(ranges[0::2], ranges[1::2]):
            if output_text.compare(start, "<=", click_index) and output_text.compare(click_index, "<", end):
                wopen(output_text.get(start, end))
                break

    output_text.tag_bind("wallpaper_link", "<Button-1>", open_wallpaper_link)
    output_text.tag_bind("wallpaper_link", "<Enter>", lambda event: output_text.configure(cursor="hand2"))
    output_text.tag_bind("wallpaper_link", "<Leave>", lambda event: output_text.configure(cursor=""))
    output_text.insert(INSERT, "编号\t名称\t壁纸链接\n")
    output_text.insert(INSERT, "─" * 80 + "\n")
    for i in ls:
        ids = str(i.get("id", ""))
        thumb = str(i.get("thumb", ""))
        thumb_name = str(i.get("thumb_name", ""))
        if not thumb:
            continue
        output_text.insert(INSERT, f"{ids}\t{thumb_name}\t")
        output_text.insert(INSERT, thumb, ("wallpaper_link",))
        output_text.insert(INSERT, "\n")
    output_text.configure(state=DISABLED)


def query_video_comments(typeid=1) -> None:  # 查询视频评论
    vidl = [
        {
            1: "输入B站视频av号（不加av，BV号请转换后再输入）",
            12: "输入B站专栏cv号（不加cv）...",
            14: "输入B站音频au号（不加au）...",
            17: "输入B站文字动态代码...",
            11: "输入B站相簿（图片动态）代码...",
        },
        {
            1: "输入B站视频av号（不加av，BV号请转换后再输入）",
            12: "输入B站专栏cv号（不加cv）...",
            14: "输入B站音频au号（不加au）...",
            17: "输入B站文字动态代码...",
            11: "输入B站相簿（图片动态）代码...",
        },
        {
            1: "輸入B站影片av號（不加av，BV號請轉換後再輸入）",
            12: "輸入B站專欄cv號（不加cv）...",
            14: "輸入B站音訊au號（不加au）...",
            17: "輸入B站文字動態號碼...",
            11: "輸入B站相簿（圖片動態）號碼...",
        },
    ]
    vid = askinteger(title=window_title, prompt=vidl[lang][typeid])
    if vid == None:
        return None
    sor = askinteger(
        title=window_title,
        prompt="输入评论排序方式：\n0：按点赞数（默认）\n1：按回复数\n2：按时间",
        minvalue=0,
        maxvalue=2,
    )
    if sor == None:
        sor = 0
    pn = askinteger(title=window_title, prompt="输入评论页码数，每页固定15个评论(默认第一页)...", minvalue=1)
    if pn == None:
        pn = 1
    detail_url = "https://api.bilibili.com/x/v2/reply"
    params = {"type": typeid, "ps": 15, "pn": pn, "sort": {0: 1, 1: 2, 2: 0}[sor], "oid": vid}
    referer = f"https://www.bilibili.com/video/av{vid}" if typeid == 1 else "https://www.bilibili.com/"
    for t in range(1, MAX_RETRIES + 1):
        try:
            page2 = request_api(detail_url, params=params, headers={**headers, "Referer": referer})
        except Exception as e:
            if t < MAX_RETRIES:
                pass
            else:
                error_text = str(e)
                error_msgs = [
                    f"请求尝试{t}次后仍然发生错误：{error_text}",
                    f"The request still failed after {t} attempts: {error_text}",
                    f"請求嘗試{t}次後仍然發生錯誤：{error_text}",
                    f"要求を {t} 回試行した後もエラーが発生しました： {error_text}",
                    f"Nach {t} Versuchen an der Anforderung trat immer noch ein Fehler auf: {error_text}",
                    f"Une erreur se produisait encore après {t} tentatives de requête : {error_text}",
                    f"ข้อผิดพลาดยังคงเกิดขึ้นหลังจาก {t} ครั้งของความพยายามที่คําขอ: {error_text}",
                    f"요청을 {t}번 시도한 후에도 오류가 계속 발생했습니다: {error_text}",
                    f"Ошибка по-прежнему возникала после {t} попыток выполнения запроса: {error_text}",
                    f"Vẫn xảy ra lỗi sau {t} lần thử yêu cầu: {error_text}",
                    f"Ainda ocorreu um erro após {t} vezes de tentativas na solicitação: {error_text}",
                    f"Todavía se ha producido un error después de {t} veces de intentos en la solicitud: {error_text}",
                    f"Kesalahan masih terjadi setelah {t} kali upaya permintaan: {error_text}",
                ]
                showwarning(title=window_title, message=error_msgs[lang])
                return None
        else:
            break
    soup2 = read_api_response(page2)
    status_code = api_code(soup2)
    if status_code != 0:
        msge = api_message(soup2)
        showwarning(title=window_title, message="获取失败！原因：" + msge + "(" + str(status_code) + ")")
        return None
    outpt()
    attempt_msg = [
        f"请求共尝试了{t}次。\n",
        f"The request was attempted {t} time(s).\n",
        f"請求共嘗試了{t}次。\n",
        f"The request was attempted {t} times.\n",
        f"The request was attempted {t} times.\n",
        f"The request was attempted {t} times.\n",
        f"The request was attempted {t} times.\n",
        f"The request was attempted {t} times.\n",
        f"The request was attempted {t} times.\n",
        f"The request was attempted {t} times.\n",
        f"The request was attempted {t} times.\n",
        f"The request was attempted {t} times.\n",
        f"Permintaan itu dicoba untuk {t} kali.\n",
    ]
    output_text.insert(INSERT, attempt_msg[lang])
    rpls = (soup2.get("data") or {}).get("replies") or []
    if not rpls:
        output_text.insert(INSERT, "暂无评论" if lang == LANG_CN else "No comments")
    for i in rpls:
        mbe = i["member"]
        ct = i["content"]
        user_id = i["mid"]
        uname = mbe["uname"]
        sex = mbe.get("sex") or "—"
        signature = mbe.get("sign") or mbe.get("signature") or ""
        msg = ct["message"]
        rpl = i.get("replies") or []
        if lang == 0:
            output_text.insert(
                INSERT,
                f"评论者UID：\t\t{user_id}"
                + f"\n评论者昵称：\t\t{uname}"
                + f"\n评论者性别：\t\t{sex}"
                + f"\n评论者签名：\n{signature}"
                + f"\n评论内容：\n{msg}"
                + f"\n回复内容：",
            )
        elif lang == 1:
            output_text.insert(
                INSERT,
                f"Commentator's UID: \t\t\t{user_id}"
                + f"\nCommentator's nickname: \t\t\t{uname}"
                + f"\nCommentator's sex: \t\t\t{sex}"
                + f"\nCommentator's signature: \n{signature}"
                + f"\nComment content: \n{msg}"
                + f"\nReply content: ",
            )
        elif lang == 2:
            output_text.insert(
                INSERT,
                f"評論者UID：\t\t{user_id}"
                + f"\n評論者暱稱：\t\t{uname}"
                + f"\n評論者性別：\t\t{sex}"
                + f"\n評論者簽名：\n{to_traditional(signature)}"
                + f"\n評論內容：\n{to_traditional(msg)}"
                + f"\n回覆內容：",
            )
        elif lang == 3:
            output_text.insert(
                INSERT,
                f"Commentator's UID: \t\t\t{user_id}"
                + f"\nCommentator's nickname: \t\t\t{uname}"
                + f"\nCommentator's sex: \t\t\t{sex}"
                + f"\nCommentator's signature: \n{signature}"
                + f"\nComment content: \n{msg}"
                + f"\nReply content: ",
            )
        elif lang == 4:
            output_text.insert(
                INSERT,
                f"Commentator's UID: \t\t\t{user_id}"
                + f"\nCommentator's nickname: \t\t\t{uname}"
                + f"\nCommentator's sex: \t\t\t{sex}"
                + f"\nCommentator's signature: \n{signature}"
                + f"\nComment content: \n{msg}"
                + f"\nReply content: ",
            )
        elif lang == 5:
            output_text.insert(
                INSERT,
                f"Commentator's UID: \t\t\t{user_id}"
                + f"\nCommentator's nickname: \t\t\t{uname}"
                + f"\nCommentator's sex: \t\t\t{sex}"
                + f"\nCommentator's signature: \n{signature}"
                + f"\nComment content: \n{msg}"
                + f"\nReply content: ",
            )
        elif lang == 6:
            output_text.insert(
                INSERT,
                f"Commentator's UID: \t\t\t{user_id}"
                + f"\nCommentator's nickname: \t\t\t{uname}"
                + f"\nCommentator's sex: \t\t\t{sex}"
                + f"\nCommentator's signature: \n{signature}"
                + f"\nComment content: \n{msg}"
                + f"\nReply content: ",
            )
        elif lang == 7:
            output_text.insert(
                INSERT,
                f"Commentator's UID: \t\t\t{user_id}"
                + f"\nCommentator's nickname: \t\t\t{uname}"
                + f"\nCommentator's sex: \t\t\t{sex}"
                + f"\nCommentator's signature: \n{signature}"
                + f"\nComment content: \n{msg}"
                + f"\nReply content: ",
            )
        elif lang == 8:
            output_text.insert(
                INSERT,
                f"Commentator's UID: \t\t\t{user_id}"
                + f"\nCommentator's nickname: \t\t\t{uname}"
                + f"\nCommentator's sex: \t\t\t{sex}"
                + f"\nCommentator's signature: \n{signature}"
                + f"\nComment content: \n{msg}"
                + f"\nReply content: ",
            )
        elif lang == 9:
            output_text.insert(
                INSERT,
                f"Commentator's UID: \t\t\t{user_id}"
                + f"\nCommentator's nickname: \t\t\t{uname}"
                + f"\nCommentator's sex: \t\t\t{sex}"
                + f"\nCommentator's signature: \n{signature}"
                + f"\nComment content: \n{msg}"
                + f"\nReply content: ",
            )
        elif lang == 10:
            output_text.insert(
                INSERT,
                f"Commentator's UID: \t\t\t{user_id}"
                + f"\nCommentator's nickname: \t\t\t{uname}"
                + f"\nCommentator's sex: \t\t\t{sex}"
                + f"\nCommentator's signature: \n{signature}"
                + f"\nComment content: \n{msg}"
                + f"\nReply content: ",
            )
        elif lang == 11:
            output_text.insert(
                INSERT,
                f"Commentator's UID: \t\t\t{user_id}"
                + f"\nCommentator's nickname: \t\t\t{uname}"
                + f"\nCommentator's sex: \t\t\t{sex}"
                + f"\nCommentator's signature: \n{signature}"
                + f"\nComment content: \n{msg}"
                + f"\nReply content: ",
            )
        elif lang == 12:
            output_text.insert(
                INSERT,
                f"Commentator's UID: \t\t\t{user_id}"
                + f"\nCommentator's nickname: \t\t\t{uname}"
                + f"\nCommentator's sex: \t\t\t{sex}"
                + f"\nCommentator's signature: \n{signature}"
                + f"\nComment content: \n{msg}"
                + f"\nReply content: ",
            )
        if rpl != None:
            output_text.insert(INSERT, "\n****************")
            k = 0
            for n in rpl:
                k += 1
                mber = n["member"]
                user_id = n["mid"]
                uname = mber["uname"]
                sex = mber.get("sex") or "—"
                signature = mber.get("sign") or mber.get("signature") or ""
                ctr = n["content"]
                msg = ctr["message"]
                tme = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(n["ctime"]))
                if lang == 0:
                    output_text.insert(
                        INSERT,
                        f"回复者{k}"
                        + f"：\n回复者UID：\t\t{user_id}"
                        + f"\n回复者昵称：\t\t{uname}"
                        + f"\n回复者性别：\t\t{sex}"
                        + f"\n回复者签名：\n{signature}"
                        + f"\n回复内容：\n{msg}"
                        + f"\n回复发布时间：\t\t{tme}\n",
                    )
                elif lang == 1:
                    output_text.insert(
                        INSERT,
                        f"Respondent {k}"
                        + f": \nRespondent's UID: \t\t\t{user_id}"
                        + f"\nRespondent's nickname: \t\t\t{uname}"
                        + f"\nRespondent's sex: \t\t\t{sex}"
                        + f"\nRespondent's signature: \n{signature}"
                        + f"\nReply content: \n{msg}"
                        + f"\nReply release time: \t\t\t{tme}\n",
                    )
                elif lang == 2:
                    output_text.insert(
                        INSERT,
                        f"回覆者{k}"
                        + f"：\n回覆者UID：\t\t{user_id}"
                        + f"\n回覆者暱稱：\t\t{uname}"
                        + f"\n回覆者性別：\t\t{sex}"
                        + f"\n回覆者簽名：\n{to_traditional(signature)}"
                        + f"\n回覆內容：\n{to_traditional(msg)}"
                        + f"\n回覆釋出時間：\t\t{tme}\n",
                    )
                elif lang == 3:
                    output_text.insert(
                        INSERT,
                        f"Respondent {k}"
                        + f": \nRespondent's UID: \t\t\t{user_id}"
                        + f"\nRespondent's nickname: \t\t\t{uname}"
                        + f"\nRespondent's sex: \t\t\t{sex}"
                        + f"\nRespondent's signature: \n{signature}"
                        + f"\nReply content: \n{msg}"
                        + f"\nReply release time: \t\t\t{tme}\n",
                    )
                elif lang == 4:
                    output_text.insert(
                        INSERT,
                        f"Respondent {k}"
                        + f": \nRespondent's UID: \t\t\t{user_id}"
                        + f"\nRespondent's nickname: \t\t\t{uname}"
                        + f"\nRespondent's sex: \t\t\t{sex}"
                        + f"\nRespondent's signature: \n{signature}"
                        + f"\nReply content: \n{msg}"
                        + f"\nReply release time: \t\t\t{tme}\n",
                    )
                elif lang == 5:
                    output_text.insert(
                        INSERT,
                        f"Respondent {k}"
                        + f": \nRespondent's UID: \t\t\t{user_id}"
                        + f"\nRespondent's nickname: \t\t\t{uname}"
                        + f"\nRespondent's sex: \t\t\t{sex}"
                        + f"\nRespondent's signature: \n{signature}"
                        + f"\nReply content: \n{msg}"
                        + f"\nReply release time: \t\t\t{tme}\n",
                    )
                elif lang == 6:
                    output_text.insert(
                        INSERT,
                        f"Respondent {k}"
                        + f": \nRespondent's UID: \t\t\t{user_id}"
                        + f"\nRespondent's nickname: \t\t\t{uname}"
                        + f"\nRespondent's sex: \t\t\t{sex}"
                        + f"\nRespondent's signature: \n{signature}"
                        + f"\nReply content: \n{msg}"
                        + f"\nReply release time: \t\t\t{tme}\n",
                    )
                elif lang == 7:
                    output_text.insert(
                        INSERT,
                        f"Respondent {k}"
                        + f": \nRespondent's UID: \t\t\t{user_id}"
                        + f"\nRespondent's nickname: \t\t\t{uname}"
                        + f"\nRespondent's sex: \t\t\t{sex}"
                        + f"\nRespondent's signature: \n{signature}"
                        + f"\nReply content: \n{msg}"
                        + f"\nReply release time: \t\t\t{tme}\n",
                    )
                elif lang == 8:
                    output_text.insert(
                        INSERT,
                        f"Respondent {k}"
                        + f": \nRespondent's UID: \t\t\t{user_id}"
                        + f"\nRespondent's nickname: \t\t\t{uname}"
                        + f"\nRespondent's sex: \t\t\t{sex}"
                        + f"\nRespondent's signature: \n{signature}"
                        + f"\nReply content: \n{msg}"
                        + f"\nReply release time: \t\t\t{tme}\n",
                    )
                elif lang == 9:
                    output_text.insert(
                        INSERT,
                        f"Respondent {k}"
                        + f": \nRespondent's UID: \t\t\t{user_id}"
                        + f"\nRespondent's nickname: \t\t\t{uname}"
                        + f"\nRespondent's sex: \t\t\t{sex}"
                        + f"\nRespondent's signature: \n{signature}"
                        + f"\nReply content: \n{msg}"
                        + f"\nReply release time: \t\t\t{tme}\n",
                    )
                elif lang == 10:
                    output_text.insert(
                        INSERT,
                        f"Respondent {k}"
                        + f": \nRespondent's UID: \t\t\t{user_id}"
                        + f"\nRespondent's nickname: \t\t\t{uname}"
                        + f"\nRespondent's sex: \t\t\t{sex}"
                        + f"\nRespondent's signature: \n{signature}"
                        + f"\nReply content: \n{msg}"
                        + f"\nReply release time: \t\t\t{tme}\n",
                    )
                elif lang == 11:
                    output_text.insert(
                        INSERT,
                        f"Respondent {k}"
                        + f": \nRespondent's UID: \t\t\t{user_id}"
                        + f"\nRespondent's nickname: \t\t\t{uname}"
                        + f"\nRespondent's sex: \t\t\t{sex}"
                        + f"\nRespondent's signature: \n{signature}"
                        + f"\nReply content: \n{msg}"
                        + f"\nReply release time: \t\t\t{tme}\n",
                    )
                elif lang == 12:
                    output_text.insert(
                        INSERT,
                        f"Respondent {k}"
                        + f": \nRespondent's UID: \t\t\t{user_id}"
                        + f"\nRespondent's nickname: \t\t\t{uname}"
                        + f"\nRespondent's sex: \t\t\t{sex}"
                        + f"\nRespondent's signature: \n{signature}"
                        + f"\nReply content: \n{msg}"
                        + f"\nReply release time: \t\t\t{tme}\n",
                    )
                output_text.insert(INSERT, "////////////////")
        else:
            norp = [
                "暂无回复\n",
                "No replies\n",
                "暫無回覆\n",
                "No replies\n",
                "No replies\n",
                "No replies\n",
                "No replies\n",
                "No replies\n",
                "No replies\n",
                "No replies\n",
                "No replies\n",
                "No replies\n",
                "No replies\n",
            ]
            output_text.insert(INSERT, norp[lang])
        if lang in [0, 2, 3, 7]:
            tme = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i["ctime"]))
        elif lang in [1, 9]:
            tme = time.strftime("%m-%d-%Y %H:%M:%S", time.localtime(i["ctime"]))
        elif lang in [4, 5, 6, 8, 10, 11, 12]:
            tme = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(i["ctime"]))
        mainrelease = [
            f"主评论发布时间：\t\t{tme}",
            f"Main comment release time: \t\t\t{tme}",
            f"主評論釋出時間：\t\t{tme}",
            f"メインコメントの投稿時間：\t\t\t{tme}",
            f"Veröffentlichungszeit des Hauptkommentars：\t\t\t{tme}",
            f"Date de publication du commentaire principal :\t\t\t{tme}",
            f"เวลาโพสต์ความคิดเห็นหลัก：\t\t\t{tme}",
            f"주요 댓글 게시 시간：\t\t\t{tme}",
            f"Время публикации основного комментария：\t\t\t{tme}",
            f"Thời gian đăng bình luận chính：\t\t\t{tme}",
            f"Hora de publicação do comentário principal：\t\t\t{tme}",
            f"Hora de publicación del comentario principal：\t\t\t{tme}",
            f"Waktu posting komentar utama：\t\t\t{tme}",
        ]
        output_text.insert(INSERT, mainrelease[lang])
        output_text.insert(INSERT, "\n————————————————————\n")
    output_text.configure(state=DISABLED)


def query_other_comments() -> None:  # 查询其他评论
    sub_window = tkinter.Toplevel(loading_window)
    sub_window.title(window_title)
    sub_window.iconbitmap(icon_file)
    Label(sub_window, text=menu_items[lang][10][0], font=(font_family, 14), fg="purple").pack()
    tool_labels = [
        ("专栏评论", "音频评论", "动态评论", "相簿评论"),
        ("Column comments", "Audio comments", "Dynamic comments", "Album comments"),
        ("專欄評論", "音訊評論", "動態評論", "相簿評論"),
        ("Column comments", "Audio comments", "Dynamic comments", "Album comments"),
        ("Column comments", "Audio comments", "Dynamic comments", "Album comments"),
        ("Column comments", "Audio comments", "Dynamic comments", "Album comments"),
        ("Column comments", "Audio comments", "Dynamic comments", "Album comments"),
        ("Column comments", "Audio comments", "Dynamic comments", "Album comments"),
        ("Column comments", "Audio comments", "Dynamic comments", "Album comments"),
        ("Column comments", "Audio comments", "Dynamic comments", "Album comments"),
        ("Column comments", "Audio comments", "Dynamic comments", "Album comments"),
        ("Column comments", "Audio comments", "Dynamic comments", "Album comments"),
        ("Column comments", "Audio comments", "Dynamic comments", "Album comments"),
    ]
    col = lambda tpid=12: query_video_comments(tpid)
    aud = lambda: col(14)
    dyn = lambda: col(17)
    alb = lambda: col(11)
    bl = [
        Button(sub_window, text=tool_labels[lang][0], command=col, font=default_font),
        Button(sub_window, text=tool_labels[lang][1], command=aud, font=default_font),
        Button(sub_window, text=tool_labels[lang][2], command=dyn, font=default_font),
        Button(sub_window, text=tool_labels[lang][3], command=alb, font=default_font),
    ]
    for i in bl:
        i.pack(side="left")


def search_video() -> None:  # 搜索视频
    for t in range(1, MAX_RETRIES + 1):
        try:
            page = request_api(
                "https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword=114514",
                headers=headers,
            )
        except Exception as e:
            if t < MAX_RETRIES:
                pass
            else:
                error_text = str(e)
                error_msgs = [
                    f"请求尝试{t}次后仍然发生错误：{error_text}",
                    f"The request still failed after {t} attempts: {error_text}",
                    f"請求嘗試{t}次後仍然發生錯誤：{error_text}",
                    f"要求を {t} 回試行した後もエラーが発生しました： {error_text}",
                    f"Nach {t} Versuchen an der Anforderung trat immer noch ein Fehler auf: {error_text}",
                    f"Une erreur se produisait encore après {t} tentatives de requête : {error_text}",
                    f"ข้อผิดพลาดยังคงเกิดขึ้นหลังจาก {t} ครั้งของความพยายามที่คําขอ: {error_text}",
                    f"요청을 {t}번 시도한 후에도 오류가 계속 발생했습니다: {error_text}",
                    f"Ошибка по-прежнему возникала после {t} попыток выполнения запроса: {error_text}",
                    f"Vẫn xảy ra lỗi sau {t} lần thử yêu cầu: {error_text}",
                    f"Ainda ocorreu um erro após {t} vezes de tentativas na solicitação: {error_text}",
                    f"Todavía se ha producido un error después de {t} veces de intentos en la solicitud: {error_text}",
                    f"Kesalahan masih terjadi setelah {t} kali upaya permintaan: {error_text}",
                ]
                showwarning(title=window_title, message=error_msgs[lang])
                return None
        else:
            break
    response_data = read_api_response(page)
    if api_code(response_data) == -412:
        showwarning(title=window_title, message=api_message(response_data) + "，请先登录！")
    elif api_code(response_data) != 0:
        showwarning(
            title=window_title,
            message="出现错误：" + api_message(response_data) + "(" + str(api_code(response_data)) + ")",
        )
    else:
        searkey = askstring(title=window_title, prompt="输入你要搜索的内容...")
        if searkey == None:
            return None
        pge = askinteger(title=window_title, prompt="输入搜索内容页码（一页20个，默认第一页）...")
        if pge == None:
            pge = 1
        detail_url = f"https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword={searkey}&page={pge}"
        order_list = {
            0: "totalrank",
            1: "click",
            2: "pubdate",
            3: "dm",
            4: "stow",
            5: "scores",
            None: "totalrank",
        }
        odri = askinteger(
            title=window_title,
            prompt="输入排序方式：\n0:综合排序（默认）\n1:最多点击\n2:最新发布\n3:最多弹幕\n4:最多收藏\n5:最多评论",
        )
        try:
            order = order_list[odri]
        except Exception:
            order = order_list[0]
        dura = askinteger(
            title=window_title,
            prompt="输入视频时长：\n0:全部（默认）\n1:10min以下\n2:10-30min\n3:30-60min\n4:60min以上",
        )
        if dura == None or not 0 <= dura <= 4:
            dura = 0
        detail_url += f"&order={order}&duration={dura}"
        for t in range(1, MAX_RETRIES + 1):
            try:
                page2 = request_api(detail_url, headers=headers)
            except Exception as e:
                if t < MAX_RETRIES:
                    pass
                else:
                    error_text = str(e)
                    error_msgs = [
                        f"请求尝试{t}次后仍然发生错误：{error_text}",
                        f"The request still failed after {t} attempts: {error_text}",
                        f"請求嘗試{t}次後仍然發生錯誤：{error_text}",
                        f"要求を {t} 回試行した後もエラーが発生しました： {error_text}",
                        f"Nach {t} Versuchen an der Anforderung trat immer noch ein Fehler auf: {error_text}",
                        f"Une erreur se produisait encore après {t} tentatives de requête : {error_text}",
                        f"ข้อผิดพลาดยังคงเกิดขึ้นหลังจาก {t} ครั้งของความพยายามที่คําขอ: {error_text}",
                        f"요청을 {t}번 시도한 후에도 오류가 계속 발생했습니다: {error_text}",
                        f"Ошибка по-прежнему возникала после {t} попыток выполнения запроса: {error_text}",
                        f"Vẫn xảy ra lỗi sau {t} lần thử yêu cầu: {error_text}",
                        f"Ainda ocorreu um erro após {t} vezes de tentativas na solicitação: {error_text}",
                        f"Todavía se ha producido un error después de {t} veces de intentos en la solicitud: {error_text}",
                        f"Kesalahan masih terjadi setelah {t} kali upaya permintaan: {error_text}",
                    ]
                    showwarning(title=window_title, message=error_msgs[lang])
                    return None
            else:
                break
        soup2 = require_api_success(read_api_response(page2))
        try:
            resl = soup2["data"]["result"] or []
        except Exception:
            showwarning(title=window_title, message="无结果")
        else:
            outpt()
            attempt_msg = [
                f"请求共尝试了{t}次。\n",
                f"The request was attempted {t} time(s).\n",
                f"請求共嘗試了{t}次。\n",
                f"The request was attempted {t} times.\n",
                f"The request was attempted {t} times.\n",
                f"The request was attempted {t} times.\n",
                f"The request was attempted {t} times.\n",
                f"The request was attempted {t} times.\n",
                f"The request was attempted {t} times.\n",
                f"The request was attempted {t} times.\n",
                f"The request was attempted {t} times.\n",
                f"The request was attempted {t} times.\n",
                f"Permintaan itu dicoba untuk {t} kali.\n",
            ]
            output_text.insert(INSERT, attempt_msg[lang])
            for i in resl:
                uname = i["author"]
                user_id = i["mid"]
                title = i["title"].replace("&quot;", '"').replace("&amp;", "&")
                title = title.replace('<em class="keyword">', "[[[").replace(
                    "</em>", "]]]"
                )
                avid = i["aid"]
                bvid = i["bvid"]
                urls = "https://www.bilibili.com/video/" + bvid
                dura = i["duration"]
                tpn = i["typename"]
                tpid = i["typeid"]
                play = i["play"]
                like = i["like"]
                favo = i["favorites"]
                pubdate = time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime(i["pubdate"])
                )
                desc = i["description"]
                tag = i["tag"]
                if lang == 0:
                    output_text.insert(
                        INSERT,
                        f"视频标题：\t\t{title}"
                        + f"\n视频AV号：\t\tav{avid}"
                        + f"\n视频BV号：\t\t{bvid}"
                        + f"\n视频标签：\t\t{tag}"
                        + f"\n视频总时长：\t\t{dura}"
                        + f"\n视频发布时间：\t\t{pubdate}"
                        + f"\n视频分区：\t\t{tpn}（{tpid}）"
                        + f"\n视频简介：\n{desc}"
                        + f'\n合作视频：\t\t{"是" if i["is_union_video"] else "否"}'
                        + f"\n播放量：\t\t{play}"
                        + f"\n点赞量：\t\t{like}"
                        + f"\n收藏量：\t\t{favo}"
                        + f"\n视频链接：\t\t{urls}"
                        + f"\nUP主昵称 / UID：\t\t{uname} / {user_id}",
                    )
                elif lang == 1:
                    output_text.insert(
                        INSERT,
                        f"Title: \t\t\t{title}"
                        + f"\nAVID: \t\t\tav{avid}"
                        + f"\nBVID: \t\t\t{bvid}"
                        + f"\nVideo tag: \t\t\t{tag}"
                        + f"\nVideo duration: \t\t\t{dura}"
                        + f"\nRelease time: \t\t\t{pubdate}"
                        + f"\nVideo partition: \t\t\t{tpn} ({tpid})"
                        + f"\nVideo introduction: \n{desc}"
                        + f'\nUnion video: \t\t\t{"Yes" if i["is_union_video"] else "No"}'
                        + f"\nPlay count: \t\t\t{play}"
                        + f"\nLike count: \t\t\t{like}"
                        + f"\nFavorite count: \t\t\t{favo}"
                        + f"\nVideo link: \t\t\t{urls}"
                        + f"\nUP master's nickname / UID: \t\t\t{uname} / {user_id}",
                    )
                elif lang == 2:
                    output_text.insert(
                        INSERT,
                        f"影片標題：\t\t{to_traditional(title)}"
                        + f"\n影片AV號：\t\tav{avid}"
                        + f"\n影片BV號：\t\t{bvid}"
                        + f"\n影片標籤：\t\t{to_traditional(tag)}"
                        + f"\n影片總時長：\t\t{dura}"
                        + f"\n影片釋出時間：\t\t{pubdate}"
                        + f"\n影片分區：\t\t{to_traditional(tpn)}（{tpid}）"
                        + f"\n影片簡介：\n{to_traditional(desc)}"
                        + f'\n合作影片：\t\t{"是" if i["is_union_video"] else "否"}'
                        + f"\n播放量：\t\t{play}"
                        + f"\n點贊量：\t\t{like}"
                        + f"\n收藏量：\t\t{favo}"
                        + f"\n影片連結：\t\t{urls}"
                        + f"\nUP主暱稱 / UID：\t\t{uname} / {user_id}",
                    )
                elif lang == 3:
                    output_text.insert(
                        INSERT,
                        f"Title: \t\t\t{title}"
                        + f"\nAVID: \t\t\tav{avid}"
                        + f"\nBVID: \t\t\t{bvid}"
                        + f"\nVideo tag: \t\t\t{tag}"
                        + f"\nVideo duration: \t\t\t{dura}"
                        + f"\nRelease time: \t\t\t{pubdate}"
                        + f"\nVideo partition: \t\t\t{tpn} ({tpid})"
                        + f"\nVideo introduction: \n{desc}"
                        + f'\nUnion video: \t\t\t{"Yes" if i["is_union_video"] else "No"}'
                        + f"\nPlay count: \t\t\t{play}"
                        + f"\nLike count: \t\t\t{like}"
                        + f"\nFavorite count: \t\t\t{favo}"
                        + f"\nVideo link: \t\t\t{urls}"
                        + f"\nUP master's nickname / UID: \t\t\t{uname} / {user_id}",
                    )
                elif lang == 4:
                    output_text.insert(
                        INSERT,
                        f"Title: \t\t\t{title}"
                        + f"\nAVID: \t\t\tav{avid}"
                        + f"\nBVID: \t\t\t{bvid}"
                        + f"\nVideo tag: \t\t\t{tag}"
                        + f"\nVideo duration: \t\t\t{dura}"
                        + f"\nRelease time: \t\t\t{pubdate}"
                        + f"\nVideo partition: \t\t\t{tpn} ({tpid})"
                        + f"\nVideo introduction: \n{desc}"
                        + f'\nUnion video: \t\t\t{"Yes" if i["is_union_video"] else "No"}'
                        + f"\nPlay count: \t\t\t{play}"
                        + f"\nLike count: \t\t\t{like}"
                        + f"\nFavorite count: \t\t\t{favo}"
                        + f"\nVideo link: \t\t\t{urls}"
                        + f"\nUP master's nickname / UID: \t\t\t{uname} / {user_id}",
                    )
                elif lang == 5:
                    output_text.insert(
                        INSERT,
                        f"Title: \t\t\t{title}"
                        + f"\nAVID: \t\t\tav{avid}"
                        + f"\nBVID: \t\t\t{bvid}"
                        + f"\nVideo tag: \t\t\t{tag}"
                        + f"\nVideo duration: \t\t\t{dura}"
                        + f"\nRelease time: \t\t\t{pubdate}"
                        + f"\nVideo partition: \t\t\t{tpn} ({tpid})"
                        + f"\nVideo introduction: \n{desc}"
                        + f'\nUnion video: \t\t\t{"Yes" if i["is_union_video"] else "No"}'
                        + f"\nPlay count: \t\t\t{play}"
                        + f"\nLike count: \t\t\t{like}"
                        + f"\nFavorite count: \t\t\t{favo}"
                        + f"\nVideo link: \t\t\t{urls}"
                        + f"\nUP master's nickname / UID: \t\t\t{uname} / {user_id}",
                    )
                elif lang == 6:
                    output_text.insert(
                        INSERT,
                        f"Title: \t\t\t{title}"
                        + f"\nAVID: \t\t\tav{avid}"
                        + f"\nBVID: \t\t\t{bvid}"
                        + f"\nVideo tag: \t\t\t{tag}"
                        + f"\nVideo duration: \t\t\t{dura}"
                        + f"\nRelease time: \t\t\t{pubdate}"
                        + f"\nVideo partition: \t\t\t{tpn} ({tpid})"
                        + f"\nVideo introduction: \n{desc}"
                        + f'\nUnion video: \t\t\t{"Yes" if i["is_union_video"] else "No"}'
                        + f"\nPlay count: \t\t\t{play}"
                        + f"\nLike count: \t\t\t{like}"
                        + f"\nFavorite count: \t\t\t{favo}"
                        + f"\nVideo link: \t\t\t{urls}"
                        + f"\nUP master's nickname / UID: \t\t\t{uname} / {user_id}",
                    )
                elif lang == 7:
                    output_text.insert(
                        INSERT,
                        f"Title: \t\t\t{title}"
                        + f"\nAVID: \t\t\tav{avid}"
                        + f"\nBVID: \t\t\t{bvid}"
                        + f"\nVideo tag: \t\t\t{tag}"
                        + f"\nVideo duration: \t\t\t{dura}"
                        + f"\nRelease time: \t\t\t{pubdate}"
                        + f"\nVideo partition: \t\t\t{tpn} ({tpid})"
                        + f"\nVideo introduction: \n{desc}"
                        + f'\nUnion video: \t\t\t{"Yes" if i["is_union_video"] else "No"}'
                        + f"\nPlay count: \t\t\t{play}"
                        + f"\nLike count: \t\t\t{like}"
                        + f"\nFavorite count: \t\t\t{favo}"
                        + f"\nVideo link: \t\t\t{urls}"
                        + f"\nUP master's nickname / UID: \t\t\t{uname} / {user_id}",
                    )
                elif lang == 8:
                    output_text.insert(
                        INSERT,
                        f"Title: \t\t\t{title}"
                        + f"\nAVID: \t\t\tav{avid}"
                        + f"\nBVID: \t\t\t{bvid}"
                        + f"\nVideo tag: \t\t\t{tag}"
                        + f"\nVideo duration: \t\t\t{dura}"
                        + f"\nRelease time: \t\t\t{pubdate}"
                        + f"\nVideo partition: \t\t\t{tpn} ({tpid})"
                        + f"\nVideo introduction: \n{desc}"
                        + f'\nUnion video: \t\t\t{"Yes" if i["is_union_video"] else "No"}'
                        + f"\nPlay count: \t\t\t{play}"
                        + f"\nLike count: \t\t\t{like}"
                        + f"\nFavorite count: \t\t\t{favo}"
                        + f"\nVideo link: \t\t\t{urls}"
                        + f"\nUP master's nickname / UID: \t\t\t{uname} / {user_id}",
                    )
                elif lang == 9:
                    output_text.insert(
                        INSERT,
                        f"Title: \t\t\t{title}"
                        + f"\nAVID: \t\t\tav{avid}"
                        + f"\nBVID: \t\t\t{bvid}"
                        + f"\nVideo tag: \t\t\t{tag}"
                        + f"\nVideo duration: \t\t\t{dura}"
                        + f"\nRelease time: \t\t\t{pubdate}"
                        + f"\nVideo partition: \t\t\t{tpn} ({tpid})"
                        + f"\nVideo introduction: \n{desc}"
                        + f'\nUnion video: \t\t\t{"Yes" if i["is_union_video"] else "No"}'
                        + f"\nPlay count: \t\t\t{play}"
                        + f"\nLike count: \t\t\t{like}"
                        + f"\nFavorite count: \t\t\t{favo}"
                        + f"\nVideo link: \t\t\t{urls}"
                        + f"\nUP master's nickname / UID: \t\t\t{uname} / {user_id}",
                    )
                elif lang == 10:
                    output_text.insert(
                        INSERT,
                        f"Title: \t\t\t{title}"
                        + f"\nAVID: \t\t\tav{avid}"
                        + f"\nBVID: \t\t\t{bvid}"
                        + f"\nVideo tag: \t\t\t{tag}"
                        + f"\nVideo duration: \t\t\t{dura}"
                        + f"\nRelease time: \t\t\t{pubdate}"
                        + f"\nVideo partition: \t\t\t{tpn} ({tpid})"
                        + f"\nVideo introduction: \n{desc}"
                        + f'\nUnion video: \t\t\t{"Yes" if i["is_union_video"] else "No"}'
                        + f"\nPlay count: \t\t\t{play}"
                        + f"\nLike count: \t\t\t{like}"
                        + f"\nFavorite count: \t\t\t{favo}"
                        + f"\nVideo link: \t\t\t{urls}"
                        + f"\nUP master's nickname / UID: \t\t\t{uname} / {user_id}",
                    )
                elif lang == 11:
                    output_text.insert(
                        INSERT,
                        f"Title: \t\t\t{title}"
                        + f"\nAVID: \t\t\tav{avid}"
                        + f"\nBVID: \t\t\t{bvid}"
                        + f"\nVideo tag: \t\t\t{tag}"
                        + f"\nVideo duration: \t\t\t{dura}"
                        + f"\nRelease time: \t\t\t{pubdate}"
                        + f"\nVideo partition: \t\t\t{tpn} ({tpid})"
                        + f"\nVideo introduction: \n{desc}"
                        + f'\nUnion video: \t\t\t{"Yes" if i["is_union_video"] else "No"}'
                        + f"\nPlay count: \t\t\t{play}"
                        + f"\nLike count: \t\t\t{like}"
                        + f"\nFavorite count: \t\t\t{favo}"
                        + f"\nVideo link: \t\t\t{urls}"
                        + f"\nUP master's nickname / UID: \t\t\t{uname} / {user_id}",
                    )
                elif lang == 12:
                    output_text.insert(
                        INSERT,
                        f"Title: \t\t\t{title}"
                        + f"\nAVID: \t\t\tav{avid}"
                        + f"\nBVID: \t\t\t{bvid}"
                        + f"\nVideo tag: \t\t\t{tag}"
                        + f"\nVideo duration: \t\t\t{dura}"
                        + f"\nRelease time: \t\t\t{pubdate}"
                        + f"\nVideo partition: \t\t\t{tpn} ({tpid})"
                        + f"\nVideo introduction: \n{desc}"
                        + f'\nUnion video: \t\t\t{"Yes" if i["is_union_video"] else "No"}'
                        + f"\nPlay count: \t\t\t{play}"
                        + f"\nLike count: \t\t\t{like}"
                        + f"\nFavorite count: \t\t\t{favo}"
                        + f"\nVideo link: \t\t\t{urls}"
                        + f"\nUP master's nickname / UID: \t\t\t{uname} / {user_id}",
                    )
                output_text.insert(INSERT, "\n————————————————————————————————————————————————\n")
            output_text.configure(state=DISABLED)


def search_other() -> None:  # 搜索其他
    sub_window = tkinter.Toplevel(loading_window)
    sub_window.title(window_title)
    sub_window.iconbitmap(icon_file)
    Label(sub_window, text=menu_items[lang][12][0], font=(font_family, 14), fg="purple").pack()
    tool_labels = [
        (
            "搜索专栏",
            "搜索番剧",
            "搜索影视",
            "搜索直播间及主播",
            "搜索话题",
            "搜索用户",
            "搜索相簿",
        ),
        (
            "Search Columns",
            "Search Bangumi",
            "Search Movies",
            "Search live streaming rooms and anchors",
            "Search Subjects(Tags)",
            "Search accounts",
            "Search Albums",
        ),
        (
            "搜尋專欄",
            "搜尋番劇",
            "搜尋影視",
            "搜尋直播間及主播",
            "搜尋話題",
            "搜尋用戶",
            "搜尋相簿",
        ),
        (
            "Search Columns",
            "Search Bangumi",
            "Search Movies",
            "Search live streaming rooms and anchors",
            "Search Subjects(Tags)",
            "Search accounts",
            "Search Albums",
        ),
        (
            "Search Columns",
            "Search Bangumi",
            "Search Movies",
            "Search live streaming rooms and anchors",
            "Search Subjects(Tags)",
            "Search accounts",
            "Search Albums",
        ),
        (
            "Search Columns",
            "Search Bangumi",
            "Search Movies",
            "Search live streaming rooms and anchors",
            "Search Subjects(Tags)",
            "Search accounts",
            "Search Albums",
        ),
        (
            "Search Columns",
            "Search Bangumi",
            "Search Movies",
            "Search live streaming rooms and anchors",
            "Search Subjects(Tags)",
            "Search accounts",
            "Search Albums",
        ),
        (
            "Search Columns",
            "Search Bangumi",
            "Search Movies",
            "Search live streaming rooms and anchors",
            "Search Subjects(Tags)",
            "Search accounts",
            "Search Albums",
        ),
        (
            "Search Columns",
            "Search Bangumi",
            "Search Movies",
            "Search live streaming rooms and anchors",
            "Search Subjects(Tags)",
            "Search accounts",
            "Search Albums",
        ),
        (
            "Search Columns",
            "Search Bangumi",
            "Search Movies",
            "Search live streaming rooms and anchors",
            "Search Subjects(Tags)",
            "Search accounts",
            "Search Albums",
        ),
        (
            "Search Columns",
            "Search Bangumi",
            "Search Movies",
            "Search live streaming rooms and anchors",
            "Search Subjects(Tags)",
            "Search accounts",
            "Search Albums",
        ),
        (
            "Search Columns",
            "Search Bangumi",
            "Search Movies",
            "Search live streaming rooms and anchors",
            "Search Subjects(Tags)",
            "Search accounts",
            "Search Albums",
        ),
        (
            "Search Columns",
            "Search Bangumi",
            "Search Movies",
            "Search live streaming rooms and anchors",
            "Search Subjects(Tags)",
            "Search accounts",
            "Search Albums",
        ),
    ]

    def col() -> None:
        page = request_api(
            "https://api.bilibili.com/x/web-interface/search/type?search_type=article&keyword=114514",
            headers=headers,
        )
        response_data = read_api_response(page)
        msg = api_message(response_data)
        if lang != 0 and api_code(response_data) != 0:
            msg = translated_api_message(api_code(response_data), msg)
        if api_code(response_data) == -412:
            nologin = [
                f"{msg}，请先登录！",
                f"{msg}. Please log in first!",
                f"{msg}，請先登入！",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
            ]
            showwarning(title=window_title, message=nologin[lang])
        elif api_code(response_data) != 0:
            erroroccur = [
                f'出现错误：{msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'出現錯誤：{msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
            ]
            showwarning(title=window_title, message=erroroccur[lang])
        else:
            search = [
                "输入你要搜索的内容...",
                "Enter the content you want to search for...",
                "輸入你要搜尋的內容...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
            ]
            searkey = askstring(title=window_title, prompt=search[lang])
            if searkey == None:
                return None
            pginput = [
                "输入搜索内容页码（一页20个，默认第一页）...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "輸入搜尋內容頁碼（一頁20個，默認為第一頁）...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
            ]
            pge = askinteger(title=window_title, prompt=pginput[lang])
            if pge == None:
                pge = 1
            detail_url = f"https://api.bilibili.com/x/web-interface/search/type?search_type=article&keyword={searkey}&page={pge}"
            order_list = {
                0: "totalrank",
                1: "click",
                2: "pubdate",
                3: "dm",
                4: "stow",
                5: "scores",
                6: "attention",
                None: "totalrank",
            }
            odrinput = [
                "输入排序方式：\n0:综合排序（默认）\n1:最多点击\n2:最新发布\n3:最多弹幕\n4:最多收藏\n5:最多评论\n6:最多喜欢",
                "Enter sorting method:\n0:Comprehensive sorting(default)\n1:Maximum clicks\n2:Latest released\n3:Maximum danmaku\n4:Maximum Collections\n5:Most commented\n6:Most Likes",
                "輸入排序方式：\n0:綜合排序（默認）\n1:最多點擊\n2:最新發佈\n3:最多彈幕\n4:最多收藏\n5:最多評論\n6:最多點贊",
                "Enter sorting method:\n0:Comprehensive sorting(default)\n1:Maximum clicks\n2:Latest released\n3:Maximum danmaku\n4:Maximum Collections\n5:Most commented\n6:Most Likes",
                "Enter sorting method:\n0:Comprehensive sorting(default)\n1:Maximum clicks\n2:Latest released\n3:Maximum danmaku\n4:Maximum Collections\n5:Most commented\n6:Most Likes",
                "Enter sorting method:\n0:Comprehensive sorting(default)\n1:Maximum clicks\n2:Latest released\n3:Maximum danmaku\n4:Maximum Collections\n5:Most commented\n6:Most Likes",
                "Enter sorting method:\n0:Comprehensive sorting(default)\n1:Maximum clicks\n2:Latest released\n3:Maximum danmaku\n4:Maximum Collections\n5:Most commented\n6:Most Likes",
                "Enter sorting method:\n0:Comprehensive sorting(default)\n1:Maximum clicks\n2:Latest released\n3:Maximum danmaku\n4:Maximum Collections\n5:Most commented\n6:Most Likes",
                "Enter sorting method:\n0:Comprehensive sorting(default)\n1:Maximum clicks\n2:Latest released\n3:Maximum danmaku\n4:Maximum Collections\n5:Most commented\n6:Most Likes",
                "Enter sorting method:\n0:Comprehensive sorting(default)\n1:Maximum clicks\n2:Latest released\n3:Maximum danmaku\n4:Maximum Collections\n5:Most commented\n6:Most Likes",
                "Enter sorting method:\n0:Comprehensive sorting(default)\n1:Maximum clicks\n2:Latest released\n3:Maximum danmaku\n4:Maximum Collections\n5:Most commented\n6:Most Likes",
                "Enter sorting method:\n0:Comprehensive sorting(default)\n1:Maximum clicks\n2:Latest released\n3:Maximum danmaku\n4:Maximum Collections\n5:Most commented\n6:Most Likes",
                "Enter sorting method:\n0:Comprehensive sorting(default)\n1:Maximum clicks\n2:Latest released\n3:Maximum danmaku\n4:Maximum Collections\n5:Most commented\n6:Most Likes",
            ]
            odri = askinteger(title=window_title, prompt=odrinput[lang])
            try:
                order = order_list[odri]
            except Exception:
                order = order_list[0]
            duration_prompt = [
                "输入专栏分区：\n0:全部（默认）\n1:游戏\n2:动画\n3:生活\n16:轻小说\n17:科技\n28:影视\n29:兴趣",
                "Enter column partition: \n0:All(default)\n1:Game\n2:Animation(Douga)\n3:Life\n16:Light Novel\n17:Technology\n28:Film & TV\n29:Interest",
                "輸入專欄分區：\n0:全部（默認）\n1:遊戲\n2:動畫\n3:生活\n16:輕小說\n17:科技\n28:影視\n29:興趣",
                "Enter column partition: \n0:All(default)\n1:Game\n2:Animation(Douga)\n3:Life\n16:Light Novel\n17:Technology\n28:Film & TV\n29:Interest",
                "Enter column partition: \n0:All(default)\n1:Game\n2:Animation(Douga)\n3:Life\n16:Light Novel\n17:Technology\n28:Film & TV\n29:Interest",
                "Enter column partition: \n0:All(default)\n1:Game\n2:Animation(Douga)\n3:Life\n16:Light Novel\n17:Technology\n28:Film & TV\n29:Interest",
                "Enter column partition: \n0:All(default)\n1:Game\n2:Animation(Douga)\n3:Life\n16:Light Novel\n17:Technology\n28:Film & TV\n29:Interest",
                "Enter column partition: \n0:All(default)\n1:Game\n2:Animation(Douga)\n3:Life\n16:Light Novel\n17:Technology\n28:Film & TV\n29:Interest",
                "Enter column partition: \n0:All(default)\n1:Game\n2:Animation(Douga)\n3:Life\n16:Light Novel\n17:Technology\n28:Film & TV\n29:Interest",
                "Enter column partition: \n0:All(default)\n1:Game\n2:Animation(Douga)\n3:Life\n16:Light Novel\n17:Technology\n28:Film & TV\n29:Interest",
                "Enter column partition: \n0:All(default)\n1:Game\n2:Animation(Douga)\n3:Life\n16:Light Novel\n17:Technology\n28:Film & TV\n29:Interest",
                "Enter column partition: \n0:All(default)\n1:Game\n2:Animation(Douga)\n3:Life\n16:Light Novel\n17:Technology\n28:Film & TV\n29:Interest",
                "Enter column partition: \n0:All(default)\n1:Game\n2:Animation(Douga)\n3:Life\n16:Light Novel\n17:Technology\n28:Film & TV\n29:Interest",
            ]
            dura = askinteger(title=window_title, prompt=duration_prompt[lang])
            if dura == None or not dura in (0, 1, 2, 3, 16, 17, 28, 29):
                dura = 0
            detail_url += f"&order={order}&category_id={dura}"
            page2 = request_api(detail_url, headers=headers)
            soup2 = require_api_success(read_api_response(page2))
            try:
                resl = soup2["data"]["result"] or []
            except Exception:
                noresult = [
                    "无结果",
                    "No results",
                    "無結果",
                    "No results",
                    "No results",
                    "No results",
                    "No results",
                    "No results",
                    "No results",
                    "No results",
                    "No results",
                    "No results",
                    "No results",
                ]
                showwarning(title=window_title, message=noresult[lang])
            else:
                outpt()
                for i in resl:
                    title = i["title"].replace("&quot;", '"')
                    title = title.replace('<em class="keyword">', "[[[").replace(
                        "</em>", "]]]"
                    )
                    if lang == 0:
                        output_text.insert(
                            INSERT,
                            f"专栏标题：\t\t{title}"
                            + f'\n专栏CV号：\t\tcv{i["id"]}'
                            + f'\n专栏子分区：\t\t{i["category_name"]}'
                            + f'\n专栏投稿时间：\t\t{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["pub_time"]))}'
                            + f'\n专栏文章预览：\n{i["desc"]}'
                            + f'\n阅读量：\t\t{i["view"]}'
                            + f'\n点赞量：\t\t{i["like"]}'
                            + f'\n专栏链接：\t\t{"https://www.bilibili.com/read/cv"+str(i["id"])}'
                            + f'\nUP主UID：\t\t{i["mid"]}',
                        )
                    elif lang == 1:
                        output_text.insert(
                            INSERT,
                            f"Column title: \t\t\t{title}"
                            + f'\nColumn CV ID:\t\t\tcv{i["id"]}'
                            + f'\nColumn sub partition:\t\t\t{i["category_name"]}'
                            + f'\nColumn submission time:\t\t\t{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["pub_time"]))}'
                            + f'\nColumn preview:\n{i["desc"]}'
                            + f'\nView count:\t\t\t{i["view"]}'
                            + f'\nLike count:\t\t\t{i["like"]}'
                            + f'\nColumn link:\t\t\t{"https://www.bilibili.com/read/cv"+str(i["id"])}'
                            + f'\nUID of UP master:\t\t\t{i["mid"]}',
                        )
                    elif lang == 2:
                        output_text.insert(
                            INSERT,
                            f"專欄標題：\t\t{to_traditional(title)}"
                            + f'\n專欄CV號：\t\tcv{i["id"]}'
                            + f'\n專欄子分區：\t\t{to_traditional(i["category_name"])}'
                            + f'\n專欄投稿時間：\t\t{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["pub_time"]))}'
                            + f'\n專欄文章預覽：\n{to_traditional(i["desc"])}'
                            + f'\n閱讀量：\t\t{i["view"]}'
                            + f'\n點贊量：\t\t{i["like"]}'
                            + f'\n專欄連結：\t\t{"https://www.bilibili.com/read/cv"+str(i["id"])}'
                            + f'\nUP主UID：\t\t{i["mid"]}',
                        )
                    elif lang == 3:
                        output_text.insert(
                            INSERT,
                            f"Column title: \t\t\t{title}"
                            + f'\nColumn CV ID:\t\t\tcv{i["id"]}'
                            + f'\nColumn sub partition:\t\t\t{i["category_name"]}'
                            + f'\nColumn submission time:\t\t\t{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["pub_time"]))}'
                            + f'\nColumn preview:\n{i["desc"]}'
                            + f'\nView count:\t\t\t{i["view"]}'
                            + f'\nLike count:\t\t\t{i["like"]}'
                            + f'\nColumn link:\t\t\t{"https://www.bilibili.com/read/cv"+str(i["id"])}'
                            + f'\nUID of UP master:\t\t\t{i["mid"]}',
                        )
                    elif lang == 4:
                        output_text.insert(
                            INSERT,
                            f"Column title: \t\t\t{title}"
                            + f'\nColumn CV ID:\t\t\tcv{i["id"]}'
                            + f'\nColumn sub partition:\t\t\t{i["category_name"]}'
                            + f'\nColumn submission time:\t\t\t{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["pub_time"]))}'
                            + f'\nColumn preview:\n{i["desc"]}'
                            + f'\nView count:\t\t\t{i["view"]}'
                            + f'\nLike count:\t\t\t{i["like"]}'
                            + f'\nColumn link:\t\t\t{"https://www.bilibili.com/read/cv"+str(i["id"])}'
                            + f'\nUID of UP master:\t\t\t{i["mid"]}',
                        )
                    elif lang == 5:
                        output_text.insert(
                            INSERT,
                            f"Column title: \t\t\t{title}"
                            + f'\nColumn CV ID:\t\t\tcv{i["id"]}'
                            + f'\nColumn sub partition:\t\t\t{i["category_name"]}'
                            + f'\nColumn submission time:\t\t\t{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["pub_time"]))}'
                            + f'\nColumn preview:\n{i["desc"]}'
                            + f'\nView count:\t\t\t{i["view"]}'
                            + f'\nLike count:\t\t\t{i["like"]}'
                            + f'\nColumn link:\t\t\t{"https://www.bilibili.com/read/cv"+str(i["id"])}'
                            + f'\nUID of UP master:\t\t\t{i["mid"]}',
                        )
                    elif lang == 6:
                        output_text.insert(
                            INSERT,
                            f"Column title: \t\t\t{title}"
                            + f'\nColumn CV ID:\t\t\tcv{i["id"]}'
                            + f'\nColumn sub partition:\t\t\t{i["category_name"]}'
                            + f'\nColumn submission time:\t\t\t{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["pub_time"]))}'
                            + f'\nColumn preview:\n{i["desc"]}'
                            + f'\nView count:\t\t\t{i["view"]}'
                            + f'\nLike count:\t\t\t{i["like"]}'
                            + f'\nColumn link:\t\t\t{"https://www.bilibili.com/read/cv"+str(i["id"])}'
                            + f'\nUID of UP master:\t\t\t{i["mid"]}',
                        )
                    elif lang == 7:
                        output_text.insert(
                            INSERT,
                            f"Column title: \t\t\t{title}"
                            + f'\nColumn CV ID:\t\t\tcv{i["id"]}'
                            + f'\nColumn sub partition:\t\t\t{i["category_name"]}'
                            + f'\nColumn submission time:\t\t\t{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["pub_time"]))}'
                            + f'\nColumn preview:\n{i["desc"]}'
                            + f'\nView count:\t\t\t{i["view"]}'
                            + f'\nLike count:\t\t\t{i["like"]}'
                            + f'\nColumn link:\t\t\t{"https://www.bilibili.com/read/cv"+str(i["id"])}'
                            + f'\nUID of UP master:\t\t\t{i["mid"]}',
                        )
                    elif lang == 8:
                        output_text.insert(
                            INSERT,
                            f"Column title: \t\t\t{title}"
                            + f'\nColumn CV ID:\t\t\tcv{i["id"]}'
                            + f'\nColumn sub partition:\t\t\t{i["category_name"]}'
                            + f'\nColumn submission time:\t\t\t{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["pub_time"]))}'
                            + f'\nColumn preview:\n{i["desc"]}'
                            + f'\nView count:\t\t\t{i["view"]}'
                            + f'\nLike count:\t\t\t{i["like"]}'
                            + f'\nColumn link:\t\t\t{"https://www.bilibili.com/read/cv"+str(i["id"])}'
                            + f'\nUID of UP master:\t\t\t{i["mid"]}',
                        )
                    elif lang == 9:
                        output_text.insert(
                            INSERT,
                            f"Column title: \t\t\t{title}"
                            + f'\nColumn CV ID:\t\t\tcv{i["id"]}'
                            + f'\nColumn sub partition:\t\t\t{i["category_name"]}'
                            + f'\nColumn submission time:\t\t\t{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["pub_time"]))}'
                            + f'\nColumn preview:\n{i["desc"]}'
                            + f'\nView count:\t\t\t{i["view"]}'
                            + f'\nLike count:\t\t\t{i["like"]}'
                            + f'\nColumn link:\t\t\t{"https://www.bilibili.com/read/cv"+str(i["id"])}'
                            + f'\nUID of UP master:\t\t\t{i["mid"]}',
                        )
                    elif lang == 10:
                        output_text.insert(
                            INSERT,
                            f"Column title: \t\t\t{title}"
                            + f'\nColumn CV ID:\t\t\tcv{i["id"]}'
                            + f'\nColumn sub partition:\t\t\t{i["category_name"]}'
                            + f'\nColumn submission time:\t\t\t{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["pub_time"]))}'
                            + f'\nColumn preview:\n{i["desc"]}'
                            + f'\nView count:\t\t\t{i["view"]}'
                            + f'\nLike count:\t\t\t{i["like"]}'
                            + f'\nColumn link:\t\t\t{"https://www.bilibili.com/read/cv"+str(i["id"])}'
                            + f'\nUID of UP master:\t\t\t{i["mid"]}',
                        )
                    elif lang == 11:
                        output_text.insert(
                            INSERT,
                            f"Column title: \t\t\t{title}"
                            + f'\nColumn CV ID:\t\t\tcv{i["id"]}'
                            + f'\nColumn sub partition:\t\t\t{i["category_name"]}'
                            + f'\nColumn submission time:\t\t\t{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["pub_time"]))}'
                            + f'\nColumn preview:\n{i["desc"]}'
                            + f'\nView count:\t\t\t{i["view"]}'
                            + f'\nLike count:\t\t\t{i["like"]}'
                            + f'\nColumn link:\t\t\t{"https://www.bilibili.com/read/cv"+str(i["id"])}'
                            + f'\nUID of UP master:\t\t\t{i["mid"]}',
                        )
                    elif lang == 12:
                        output_text.insert(
                            INSERT,
                            f"Column title: \t\t\t{title}"
                            + f'\nColumn CV ID:\t\t\tcv{i["id"]}'
                            + f'\nColumn sub partition:\t\t\t{i["category_name"]}'
                            + f'\nColumn submission time:\t\t\t{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["pub_time"]))}'
                            + f'\nColumn preview:\n{i["desc"]}'
                            + f'\nView count:\t\t\t{i["view"]}'
                            + f'\nLike count:\t\t\t{i["like"]}'
                            + f'\nColumn link:\t\t\t{"https://www.bilibili.com/read/cv"+str(i["id"])}'
                            + f'\nUID of UP master:\t\t\t{i["mid"]}',
                        )
                    output_text.insert(
                        INSERT, "\n————————————————————————————————————————————————\n"
                    )
                output_text.configure(state=DISABLED)

    def bangumi() -> None: ...

    def movie() -> None: ...

    def live() -> None: ...

    def tag() -> None: ...

    def acc() -> None:
        for t in range(1, MAX_RETRIES + 1):
            try:
                page = request_api(
                    "https://api.bilibili.com/x/web-interface/search/type?search_type=bili_user&keyword=114514",
                    headers=headers,
                )
            except Exception as e:
                if t < MAX_RETRIES:
                    pass
                else:
                    error_text = str(e)
                    error_msgs = [
                        f"请求尝试{t}次后仍然发生错误：{error_text}",
                        f"The request still failed after {t} attempts: {error_text}",
                        f"請求嘗試{t}次後仍然發生錯誤：{error_text}",
                        f"要求を {t} 回試行した後もエラーが発生しました： {error_text}",
                        f"Nach {t} Versuchen an der Anforderung trat immer noch ein Fehler auf: {error_text}",
                        f"Une erreur se produisait encore après {t} tentatives de requête : {error_text}",
                        f"ข้อผิดพลาดยังคงเกิดขึ้นหลังจาก {t} ครั้งของความพยายามที่คําขอ: {error_text}",
                        f"요청을 {t}번 시도한 후에도 오류가 계속 발생했습니다: {error_text}",
                        f"Ошибка по-прежнему возникала после {t} попыток выполнения запроса: {error_text}",
                        f"Vẫn xảy ra lỗi sau {t} lần thử yêu cầu: {error_text}",
                        f"Ainda ocorreu um erro após {t} vezes de tentativas na solicitação: {error_text}",
                        f"Todavía se ha producido un error después de {t} veces de intentos en la solicitud: {error_text}",
                        f"Kesalahan masih terjadi setelah {t} kali upaya permintaan: {error_text}",
                    ]
                    showwarning(title=window_title, message=error_msgs[lang])
                    return None
            else:
                break
        response_data = read_api_response(page)
        msg = api_message(response_data)
        if lang != 0 and api_code(response_data) != 0:
            msg = translated_api_message(api_code(response_data), msg)
        if api_code(response_data) == -412:
            nologin = [
                f"{msg}，请先登录！",
                f"{msg}. Please log in first!",
                f"{msg}，請先登入！",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
                f"{msg}. Please log in first!",
            ]
            showwarning(title=window_title, message=nologin[lang])
        elif api_code(response_data) != 0:
            erroroccur = [
                f'出现错误：{msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'出現錯誤：{msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
                f'An error has occurred: {msg}({api_code(response_data)})',
            ]
            showwarning(title=window_title, message=erroroccur[lang])
        else:
            search = [
                "输入你要搜索的内容...",
                "Enter the content you want to search for...",
                "輸入你要搜尋的內容...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
                "Enter the content you want to search for...",
            ]
            searkey = askstring(title=window_title, prompt=search[lang])
            if searkey == None:
                return None
            pginput = [
                "输入搜索内容页码（一页20个，默认第一页）...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "輸入搜尋內容頁碼（一頁20個，默認為第一頁）...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
                "Enter the page number of the search content (20 results per page and default to first page)...",
            ]
            pge = askinteger(title=window_title, prompt=pginput[lang])
            if pge == None:
                pge = 1
            detail_url = f"https://api.bilibili.com/x/web-interface/search/type?search_type=bili_user&keyword={searkey}&page={pge}"
            order_list = {0: "0", 1: "fans", 2: "level", None: "0"}
            odri = askinteger(
                title=window_title,
                prompt="输入排序方式：\n0:默认排序（默认）\n1:粉丝数\n2:用户等级",
            )
            try:
                order = order_list[odri]
            except Exception:
                odri = 0
                order = order_list[0]
            dura = askinteger(
                title=window_title,
                prompt="输入用户分类：\n0:全部（默认）\n1:up主\n2:普通用户\n3:认证用户",
            )
            if dura == None or not dura in (0, 1, 2, 3):
                dura = 0
            detail_url += f"&order={order}&user_type={dura}"
            if odri >= 1:
                odrup = askinteger(
                    title=window_title,
                    prompt="输入排序顺序：\n0:默认排序（默认）\n1:粉丝数\n2:用户等级",
                )
                if odrup > 2 or odrup < 0:
                    odrup = 0
                detail_url += f"&order_sort={odrup}"
            for t in range(1, MAX_RETRIES + 1):
                try:
                    page2 = request_api(detail_url, headers=headers)
                except Exception as e:
                    if t < MAX_RETRIES:
                        pass
                    else:
                        error_text = str(e)
                        error_msgs = [
                            f"请求尝试{t}次后仍然发生错误：{error_text}",
                            f"The request still failed after {t} attempts: {error_text}",
                            f"請求嘗試{t}次後仍然發生錯誤：{error_text}",
                            f"要求を {t} 回試行した後もエラーが発生しました： {error_text}",
                            f"Nach {t} Versuchen an der Anforderung trat immer noch ein Fehler auf: {error_text}",
                            f"Une erreur se produisait encore après {t} tentatives de requête : {error_text}",
                            f"ข้อผิดพลาดยังคงเกิดขึ้นหลังจาก {t} ครั้งของความพยายามที่คําขอ: {error_text}",
                            f"요청을 {t}번 시도한 후에도 오류가 계속 발생했습니다: {error_text}",
                            f"Ошибка по-прежнему возникала после {t} попыток выполнения запроса: {error_text}",
                            f"Vẫn xảy ra lỗi sau {t} lần thử yêu cầu: {error_text}",
                            f"Ainda ocorreu um erro após {t} vezes de tentativas na solicitação: {error_text}",
                            f"Todavía se ha producido un error después de {t} veces de intentos en la solicitud: {error_text}",
                            f"Kesalahan masih terjadi setelah {t} kali upaya permintaan: {error_text}",
                        ]
                        showwarning(title=window_title, message=error_msgs[lang])
                        return None
                else:
                    break
            soup2 = require_api_success(read_api_response(page2))
            try:
                resl = soup2["data"]["result"] or []
            except Exception:
                showwarning(title=window_title, message="无结果")
            else:
                gdrl = [
                    {1: "男", 2: "女", 3: "保密"},
                    {1: "Male", 2: "Female", 3: "Secret"},
                    {1: "男", 2: "女", 3: "保密"},
                    {1: "Male", 2: "Female", 3: "Secret"},
                    {1: "Male", 2: "Female", 3: "Secret"},
                    {1: "Male", 2: "Female", 3: "Secret"},
                    {1: "Male", 2: "Female", 3: "Secret"},
                    {1: "Male", 2: "Female", 3: "Secret"},
                    {1: "Male", 2: "Female", 3: "Secret"},
                    {1: "Male", 2: "Female", 3: "Secret"},
                    {1: "Male", 2: "Female", 3: "Secret"},
                    {1: "Male", 2: "Female", 3: "Secret"},
                    {1: "Male", 2: "Female", 3: "Secret"},
                ]
                outpt()
                attempt_msg = [
                    f"请求共尝试了{t}次。\n",
                    f"The request was attempted {t} time(s).\n",
                    f"請求共嘗試了{t}次。\n",
                    f"要求は {t} 回試行されました。\n",
                    f"Die Anfrage wurde {t} Mal versucht.\n",
                    f"La demande a été tentée {t} fois.\n",
                    f"คําขอถูกพยายามเป็นเวลา {t} ครั้ง\n",
                    f"요청이 {t}번 시도되었습니다.\n",
                    f"Запрос был выполнен в течение {t} раз.\n",
                    f"Yêu cầu đã được cố gắng cho {t} lần.\n",
                    f"O pedido foi tentado por {t} vezes.\n",
                    f"La solicitud se intentó {t} veces.\n",
                    f"Permintaan itu dicoba untuk {t} kali.\n",
                ]
                output_text.insert(INSERT, attempt_msg[lang])
                for i in resl:
                    if lang == 0:
                        output_text.insert(
                            INSERT,
                            f'用户昵称：\t\t{i["uname"]}'
                            + f'\n用户UID：\t\t{i["mid"]}'
                            + f'\n用户签名：\n{i["usign"]}'
                            + f'\n用户粉丝数：\t\t{i["fans"]}'
                            + f'\n用户稿件数：\t\t{i["videos"]}'
                            + f'\n等级：\t\t{i["level"]}'
                            + f'\n性别：\t\t{gdrl[lang][i["gender"]]}'
                            + f'\n主页链接：\t\thttps://space.bilibili.com/{i["mid"]}'
                            + f'\n是否为up主：\t\t{"是" if i["is_upuser"] else "否"}'
                            + f'\n是否在直播：\t\t{"是" if i["is_live"] else "否"}',
                        )
                    elif lang == 1:
                        output_text.insert(
                            INSERT,
                            f'User Nickname:\t\t\t{i["uname"]}'
                            + f'\nUser ID:\t\t\t{i["mid"]}'
                            + f'\nUser Sign:\n{i["usign"]}'
                            + f'\nFans count:\t\t\t{i["fans"]}'
                            + f'\nVideo count:\t\t\t{i["videos"]}'
                            + f'\nLevel:\t\t\t{i["level"]}'
                            + f'\nGender:\t\t\t{gdrl[lang][i["gender"]]}'
                            + f'\nSpace link:\t\t\thttps://space.bilibili.com/{i["mid"]}'
                            + f'\nUP master:\t\t\t{"Yes" if i["is_upuser"] else "No"}'
                            + f'\nLive status:\t\t\t{"Yes" if i["is_live"] else "No"}',
                        )
                    elif lang == 2:
                        output_text.insert(
                            INSERT,
                            f'使用者暱稱：\t\t{i["uname"]}'
                            + f'\n使用者UID：\t\t{i["mid"]}'
                            + f'\n使用者簽名：\n{to_traditional(i["usign"])}'
                            + f'\n使用者粉絲數：\t\t{i["fans"]}'
                            + f'\n使用者稿件數：\t\t{i["videos"]}'
                            + f'\n等級：\t\t{i["level"]}'
                            + f'\n性別：\t\t{gdrl[lang][i["gender"]]}'
                            + f'\n主頁連結：\t\thttps://space.bilibili.com/{i["mid"]}'
                            + f'\n是否為up主：\t\t{"是" if i["is_upuser"] else "否"}'
                            + f'\n是否在直播：\t\t{"是" if i["is_live"] else "否"}',
                        )
                    elif lang == 3:
                        output_text.insert(
                            INSERT,
                            f'User Nickname:\t\t\t{i["uname"]}'
                            + f'\nUser ID:\t\t\t{i["mid"]}'
                            + f'\nUser Sign:\n{i["usign"]}'
                            + f'\nFans count:\t\t\t{i["fans"]}'
                            + f'\nVideo count:\t\t\t{i["videos"]}'
                            + f'\nLevel:\t\t\t{i["level"]}'
                            + f'\nGender:\t\t\t{gdrl[lang][i["gender"]]}'
                            + f'\nSpace link:\t\t\thttps://space.bilibili.com/{i["mid"]}'
                            + f'\nUP master:\t\t\t{"Yes" if i["is_upuser"] else "No"}'
                            + f'\nLive status:\t\t\t{"Yes" if i["is_live"] else "No"}',
                        )
                    elif lang == 4:
                        output_text.insert(
                            INSERT,
                            f'User Nickname:\t\t\t{i["uname"]}'
                            + f'\nUser ID:\t\t\t{i["mid"]}'
                            + f'\nUser Sign:\n{i["usign"]}'
                            + f'\nFans count:\t\t\t{i["fans"]}'
                            + f'\nVideo count:\t\t\t{i["videos"]}'
                            + f'\nLevel:\t\t\t{i["level"]}'
                            + f'\nGender:\t\t\t{gdrl[lang][i["gender"]]}'
                            + f'\nSpace link:\t\t\thttps://space.bilibili.com/{i["mid"]}'
                            + f'\nUP master:\t\t\t{"Yes" if i["is_upuser"] else "No"}'
                            + f'\nLive status:\t\t\t{"Yes" if i["is_live"] else "No"}',
                        )
                    elif lang == 5:
                        output_text.insert(
                            INSERT,
                            f'User Nickname:\t\t\t{i["uname"]}'
                            + f'\nUser ID:\t\t\t{i["mid"]}'
                            + f'\nUser Sign:\n{i["usign"]}'
                            + f'\nFans count:\t\t\t{i["fans"]}'
                            + f'\nVideo count:\t\t\t{i["videos"]}'
                            + f'\nLevel:\t\t\t{i["level"]}'
                            + f'\nGender:\t\t\t{gdrl[lang][i["gender"]]}'
                            + f'\nSpace link:\t\t\thttps://space.bilibili.com/{i["mid"]}'
                            + f'\nUP master:\t\t\t{"Yes" if i["is_upuser"] else "No"}'
                            + f'\nLive status:\t\t\t{"Yes" if i["is_live"] else "No"}',
                        )
                    elif lang == 6:
                        output_text.insert(
                            INSERT,
                            f'User Nickname:\t\t\t{i["uname"]}'
                            + f'\nUser ID:\t\t\t{i["mid"]}'
                            + f'\nUser Sign:\n{i["usign"]}'
                            + f'\nFans count:\t\t\t{i["fans"]}'
                            + f'\nVideo count:\t\t\t{i["videos"]}'
                            + f'\nLevel:\t\t\t{i["level"]}'
                            + f'\nGender:\t\t\t{gdrl[lang][i["gender"]]}'
                            + f'\nSpace link:\t\t\thttps://space.bilibili.com/{i["mid"]}'
                            + f'\nUP master:\t\t\t{"Yes" if i["is_upuser"] else "No"}'
                            + f'\nLive status:\t\t\t{"Yes" if i["is_live"] else "No"}',
                        )
                    elif lang == 7:
                        output_text.insert(
                            INSERT,
                            f'User Nickname:\t\t\t{i["uname"]}'
                            + f'\nUser ID:\t\t\t{i["mid"]}'
                            + f'\nUser Sign:\n{i["usign"]}'
                            + f'\nFans count:\t\t\t{i["fans"]}'
                            + f'\nVideo count:\t\t\t{i["videos"]}'
                            + f'\nLevel:\t\t\t{i["level"]}'
                            + f'\nGender:\t\t\t{gdrl[lang][i["gender"]]}'
                            + f'\nSpace link:\t\t\thttps://space.bilibili.com/{i["mid"]}'
                            + f'\nUP master:\t\t\t{"Yes" if i["is_upuser"] else "No"}'
                            + f'\nLive status:\t\t\t{"Yes" if i["is_live"] else "No"}',
                        )
                    elif lang == 8:
                        output_text.insert(
                            INSERT,
                            f'User Nickname:\t\t\t{i["uname"]}'
                            + f'\nUser ID:\t\t\t{i["mid"]}'
                            + f'\nUser Sign:\n{i["usign"]}'
                            + f'\nFans count:\t\t\t{i["fans"]}'
                            + f'\nVideo count:\t\t\t{i["videos"]}'
                            + f'\nLevel:\t\t\t{i["level"]}'
                            + f'\nGender:\t\t\t{gdrl[lang][i["gender"]]}'
                            + f'\nSpace link:\t\t\thttps://space.bilibili.com/{i["mid"]}'
                            + f'\nUP master:\t\t\t{"Yes" if i["is_upuser"] else "No"}'
                            + f'\nLive status:\t\t\t{"Yes" if i["is_live"] else "No"}',
                        )
                    elif lang == 9:
                        output_text.insert(
                            INSERT,
                            f'User Nickname:\t\t\t{i["uname"]}'
                            + f'\nUser ID:\t\t\t{i["mid"]}'
                            + f'\nUser Sign:\n{i["usign"]}'
                            + f'\nFans count:\t\t\t{i["fans"]}'
                            + f'\nVideo count:\t\t\t{i["videos"]}'
                            + f'\nLevel:\t\t\t{i["level"]}'
                            + f'\nGender:\t\t\t{gdrl[lang][i["gender"]]}'
                            + f'\nSpace link:\t\t\thttps://space.bilibili.com/{i["mid"]}'
                            + f'\nUP master:\t\t\t{"Yes" if i["is_upuser"] else "No"}'
                            + f'\nLive status:\t\t\t{"Yes" if i["is_live"] else "No"}',
                        )
                    elif lang == 10:
                        output_text.insert(
                            INSERT,
                            f'User Nickname:\t\t\t{i["uname"]}'
                            + f'\nUser ID:\t\t\t{i["mid"]}'
                            + f'\nUser Sign:\n{i["usign"]}'
                            + f'\nFans count:\t\t\t{i["fans"]}'
                            + f'\nVideo count:\t\t\t{i["videos"]}'
                            + f'\nLevel:\t\t\t{i["level"]}'
                            + f'\nGender:\t\t\t{gdrl[lang][i["gender"]]}'
                            + f'\nSpace link:\t\t\thttps://space.bilibili.com/{i["mid"]}'
                            + f'\nUP master:\t\t\t{"Yes" if i["is_upuser"] else "No"}'
                            + f'\nLive status:\t\t\t{"Yes" if i["is_live"] else "No"}',
                        )
                    elif lang == 11:
                        output_text.insert(
                            INSERT,
                            f'User Nickname:\t\t\t{i["uname"]}'
                            + f'\nUser ID:\t\t\t{i["mid"]}'
                            + f'\nUser Sign:\n{i["usign"]}'
                            + f'\nFans count:\t\t\t{i["fans"]}'
                            + f'\nVideo count:\t\t\t{i["videos"]}'
                            + f'\nLevel:\t\t\t{i["level"]}'
                            + f'\nGender:\t\t\t{gdrl[lang][i["gender"]]}'
                            + f'\nSpace link:\t\t\thttps://space.bilibili.com/{i["mid"]}'
                            + f'\nUP master:\t\t\t{"Yes" if i["is_upuser"] else "No"}'
                            + f'\nLive status:\t\t\t{"Yes" if i["is_live"] else "No"}',
                        )
                    elif lang == 12:
                        output_text.insert(
                            INSERT,
                            f'User Nickname:\t\t\t{i["uname"]}'
                            + f'\nUser ID:\t\t\t{i["mid"]}'
                            + f'\nUser Sign:\n{i["usign"]}'
                            + f'\nFans count:\t\t\t{i["fans"]}'
                            + f'\nVideo count:\t\t\t{i["videos"]}'
                            + f'\nLevel:\t\t\t{i["level"]}'
                            + f'\nGender:\t\t\t{gdrl[lang][i["gender"]]}'
                            + f'\nSpace link:\t\t\thttps://space.bilibili.com/{i["mid"]}'
                            + f'\nUP master:\t\t\t{"Yes" if i["is_upuser"] else "No"}'
                            + f'\nLive status:\t\t\t{"Yes" if i["is_live"] else "No"}',
                        )
                    output_text.insert(
                        INSERT, "\n————————————————————————————————————————————————\n"
                    )
                output_text.configure(state=DISABLED)

    def album() -> None: ...

    bco = Button(sub_window, text=tool_labels[lang][0], command=col, font=default_font)
    bba = Button(sub_window, text=tool_labels[lang][1], command=bangumi, font=default_font)
    bmo = Button(sub_window, text=tool_labels[lang][2], command=movie, font=default_font)
    bls = Button(sub_window, text=tool_labels[lang][3], command=live, font=default_font)
    bsb = Button(sub_window, text=tool_labels[lang][4], command=tag, font=default_font)
    bac = Button(sub_window, text=tool_labels[lang][5], command=acc, font=default_font)
    bal = Button(sub_window, text=tool_labels[lang][6], command=album, font=default_font)
    bl = [bco, bba, bmo, bls, bsb, bac, bal]
    for i in bl:
        i.pack(side="left")


def get_recommendations() -> None:  # 获取单视频推荐列表
    while True:
        vid = askstring(
            title=window_title,
            prompt="输入B站视频av号或BV号或者链接（不加av或BV按av号算，链接目前只支持BV，结果每次都有可能不一样）...",
        )
        if vid == None:
            return None
        lvid2 = ["av", "BV", "bv"]
        if vid[:4] == "http":
            try:
                vid = vid[vid.index("BV") :][:12]
            except Exception:
                vid = "ytdb"
        if (
            vid != None
            and vid[0:2] not in lvid2
            and vid[0:1] not in lvid1
            and vid not in lvid1
        ):
            showwarning(title=window_title, message="请重新输入")
        else:
            break
    if vid == None:
        return None
    if vid[0:2] == "av" or vid[0:2] == "BV" or vid[0:2] == "bv":
        url = "https://www.bilibili.com/video/" + vid
    elif vid[0:1] in lvid1:
        url = "https://www.bilibili.com/video/av" + vid
    if vid[0:2] == "av":
        avid = vid[2:]
        detail_url = "https://api.bilibili.com/x/web-interface/archive/related?aid=" + avid
        page2 = request_api(detail_url, headers=headers)
        soup2 = read_api_response(page2)
    elif vid[0:1] in lvid1:
        avid = vid
        detail_url = "https://api.bilibili.com/x/web-interface/archive/related?aid=" + vid
        page2 = request_api(detail_url, headers=headers)
        soup2 = read_api_response(page2)
    elif vid[0:2] == "BV" or vid[0:2] == "bv":
        url3 = "https://api.bilibili.com/x/web-interface/archive/related?bvid=" + vid
        page3 = request_api(url3, headers=headers)
        soup2 = read_api_response(page3)
    status_code = api_code(soup2)
    if status_code != 0:
        msge = api_message(soup2)
        if msge == "啥都木有":
            msge = "视频不存在"
        showwarning(title=window_title, message="由于 " + msge + "(" + str(status_code) + ") ，信息获取失败！")
    else:
        data = soup2["data"]
        if len(data) == 0:
            showwarning(title=window_title, message="无数据")
        else:
            outpt()
            for i in data:
                avid = i["aid"]
                bvid = i["bvid"]
                tpn = i["tname"]
                tpid = i["tid"]
                description = i["desc"]
                title = i["title"]
                uname = i["owner"]["name"]
                user_id = i["owner"]["mid"]
                stat = i["stat"]
                play = stat["view"]
                danm = stat["danmaku"]
                rpl = stat["reply"]
                favo = stat["favorite"]
                coin = stat["coin"]
                shar = stat["share"]
                try:
                    location = i["dimension"]["pub_location"]
                except Exception:
                    location = "无"
                dura = "%02d:%02d" % divmod(i["duration"], 60)
                like = stat["like"]
                url4 = i["short_link_v2"]
                output_text.insert(
                    INSERT,
                    f"视频标题：\t\t{title}"
                    + f"\n视频AV号：\t\tav{avid}"
                    + f"\n视频BV号：\t\t{bvid}"
                    + f"\n视频简介：\n{description}"
                    + f"\n视频时长：\t\t{dura}"
                    + f"\n视频分区：\t\t{tpn}（{tpid}）"
                    + f"\n视频发布地区：\t\t{location}"
                    + f"\n播放量：\t\t{play}"
                    + f"\n点赞量：\t\t{like}"
                    + f"\n收藏量：\t\t{favo}"
                    + f"\n弹幕量：\t\t{danm}"
                    + f"\n评论量：\t\t{rpl}"
                    + f"\n投币量：\t\t{coin}"
                    + f"\n分享量：\t\t{shar}"
                    + f"\n视频短链接：\t\t{url4}"
                    + f"\nUP主昵称 / UID：\t\t{uname} / {user_id}",
                )
                output_text.insert(INSERT, "\n————————————————————————————————————————————————\n")
            output_text.configure(state=DISABLED)


def query_audio_info() -> None:  # 查询音频信息
    sid = askinteger(title=window_title, prompt="输入B站音频AUID（不加au）")
    if sid == None:
        return None
    sid = str(sid)
    url = "https://www.bilibili.com/audio/music-service-c/web/song/info?sid=" + sid
    page = request_api(url, headers=headers)
    response_data = read_api_response(page)
    status_code = api_code(response_data)
    if status_code != 0:
        msg = api_message(response_data) if lang == 0 else translated_api_message(status_code, api_message(response_data))
        warning_msg = [
            f"出现错误：{msg}({status_code})",
            f"An error has occurred: {msg}({status_code})",
        ]
        showwarning(title=window_title, message=warning_msg[lang])
        return None
    else:
        data = response_data["data"]
        detail_url = "https://www.bilibili.com/audio/au" + sid
        user_id = data.get("uid", data.get("user_id", "—"))
        uname = data["uname"]
        title = data["title"]
        description = data["intro"]
        avid = data["aid"]
        if avid == 0:
            avid, bvid = "无", "无"
        else:
            avid = str(avid)
            bvid = data["bvid"]
        outsmall()
        output_text.insert(
            INSERT,
            f"音频标题：\t\t{title}"
            + f"\n音频简介：\n{description}"
            + f"\n关联视频AV号：\t\t{avid}"
            + f"\n关联视频BV号：\t\t{bvid}"
            + f"\nUP主昵称：\t\t{uname}"
            + f"\nUP主UID：\t\t{user_id}"
            + f"\n音频链接：\t\t{detail_url}",
        )
        output_text.config(state=DISABLED)


def query_liveroom_info() -> None:  # 查询直播间信息（直播间ID）
    rid = askinteger(title=window_title, prompt="输入直播间ID...")
    if rid == None:
        return None
    rid = str(rid)
    url = "https://api.live.bilibili.com/room/v1/Room/get_info?room_id=" + rid
    page = request_api(url, headers=headers)
    response_data = read_api_response(page)
    status_code = api_code(response_data)
    if status_code != 0:
        msg = api_message(response_data) if lang == 0 else translated_api_message(status_code, api_message(response_data))
        warning_msg = [
            f"出现错误：{msg}({status_code})",
            f"An error has occurred: {msg}({status_code})",
        ]
        showwarning(title=window_title, message=warning_msg[lang])
        return None
    else:
        data = response_data["data"]
        user_id = data["user_id"]
        rid = data["room_id"]
        if data["short_id"] == 0:
            shortid = "无短号"
        else:
            shortid = data["short_id"]
        prid = data["parent_area_id"]
        prea = data["parent_area_name"]
        arid = data["area_id"]
        area = data["area_name"]
        title = data["title"]
        livt = data["live_time"]
        if livt == "0000-00-00 00:00:00":
            livt = "未开播"
        badgedict = {"v_company": "机构认证：", "v_person": "个人认证："}
        badge = (data.get("new_pendants") or {}).get("badge")
        desc = data["description"]
        badg = ""
        if badge == None:
            badg += "未认证"
        else:
            badg += badgedict.get(badge.get("name"), "") + (badge.get("desc") or "")
        outsmall()
        output_text.insert(
            INSERT,
            f"直播间标题：\t\t{title}"
            + f"\n直播间简介：\n{desc}"
            + f"\n开播时间：\t\t{livt}"
            + f"\n分区：\t\t{area}（{arid}）"
            + f"\n父分区：\t\t{prea}（{prid}）"
            + f"\n播主UID：\t\t{user_id}"
            + f"\n直播间号：\t\t{rid}"
            + f"\n直播间短号：\t\t{shortid}",
        )
        output_text.config(state=DISABLED)


def query_user_liveroom() -> None:  # 查询用户对应直播间信息
    user_id = askinteger(title=window_title, prompt="输入播主UID...")
    if user_id == None:
        return None
    user_id = str(user_id)
    url = "https://api.live.bilibili.com/live_user/v1/Master/info?uid=" + user_id
    response_data = read_api_response(request_api(url, headers=headers))
    status_code = api_code(response_data)
    if status_code != 0:
        emsg = api_message(response_data)
        showwarning(title=window_title, message="发生错误：" + emsg + "(" + str(status_code) + ")")
    else:
        data = response_data["data"]
        uname = data["info"]["uname"]
        lv = data["exp"]["master_level"]["level"]
        fans = data["follower_num"]
        rid = data["room_id"]
        medalname = data["medal_name"]
        news = data.get("room_news") or {}
        content = news.get("content") or "—"
        ctime = news.get("ctime") or "—"
        outsmall()
        output_text.insert(
            INSERT,
            f"播主昵称：\t\t{uname}"
            + f"\n播主UID：\t\t{user_id}"
            + f"\n播主直播等级：\t\t{lv}"
            + f"\n粉丝数：\t\t{fans}"
            + f"\n粉丝勋章名称：\t\t{medalname}"
            + f"\n直播间公告：\n{content}"
            + f"\n公告发布时间：\t\t{ctime}"
            + f"\n直播间号：\t\t{rid}",
        )
        output_text.config(state=DISABLED)


def get_ranking() -> None:  # 获取最新视频排行榜
    sub_window = tkinter.Toplevel(loading_window)
    sub_window.title(window_title)
    sub_window.iconbitmap(icon_file)
    Label(sub_window, text=menu_items[lang][17][0], font=(font_family, 14), fg="purple").pack()
    tool_labels = [
        (
            "总排行",
            "动画",
            "",
            "",
            "音乐",
            "舞蹈",
            "游戏",
            "知识",
            "科技",
            "运动",
            "汽车",
            "生活",
            "美食",
            "动物圈",
            "鬼畜",
            "时尚",
            "娱乐",
            "影视",
            "纪录片",
            "电影",
            "电视剧",
        ),
        (
            "Overall ranking",
            "Animation(Douga)",
            "",
            "",
            "Music",
            "Dance",
            "Game",
            "Knowledge",
            "Technology",
            "Sports",
            "Car",
            "Life",
            "Food",
            "Animal",
            "Kichiku",
            "Fashion",
            "Entertainment",
            "Film & TV",
            "Documentary",
            "Movie",
            "TV play",
        ),
        (
            "總排行",
            "動畫",
            "",
            "",
            "音樂",
            "舞蹈",
            "遊戲",
            "知識",
            "科技",
            "運動",
            "汽車",
            "生活",
            "美食",
            "動物圈",
            "鬼畜",
            "時尚",
            "娛樂",
            "影視",
            "紀錄片",
            "電影",
            "電視劇",
        ),
        (
            "総合ランキング",
            "アニメーション",
            "",
            "",
            "音楽",
            "ダンス",
            "ゲーム",
            "知識",
            "技術",
            "スポーツ",
            "自動車",
            "生活",
            "食品",
            "動物",
            "鬼畜",
            "ファッション",
            "エンタメ",
            "映画・ドラマ",
            "ドキュメンタリー",
            "映画",
            "テレビドラマ",
        ),
        (
            "Gesamtwertung",
            "Animation",
            "",
            "",
            "Musik",
            "Tanz",
            "Spiel",
            "Wissen",
            "Technologie",
            "Sport",
            "Auto",
            "Leben",
            "Essen",
            "Tiere",
            "Kichiku",
            "Mode",
            "Unterhaltung",
            "Film & TV",
            "Dokumentation",
            "Film",
            "TV-Serie",
        ),
        (
            "Classement général",
            "Animation",
            "",
            "",
            "Musique",
            "Danse",
            "Jeux",
            "Connaissance",
            "Technologie",
            "Sports",
            "Voitures",
            "Vie",
            "Nourriture",
            "Animaux",
            "Kichiku",
            "Mode",
            "Divertissement",
            "Films et séries",
            "Documentaire",
            "Films",
            "Série TV",
        ),
        (
            "Overall ranking",
            "Animation(Douga)",
            "",
            "",
            "Music",
            "Dance",
            "Game",
            "Knowledge",
            "Technology",
            "Sports",
            "Car",
            "Life",
            "Food",
            "Animal",
            "Kichiku",
            "Fashion",
            "Entertainment",
            "Film & TV",
            "Documentary",
            "Movie",
            "TV play",
        ),
        (
            "Overall ranking",
            "Animation(Douga)",
            "",
            "",
            "Music",
            "Dance",
            "Game",
            "Knowledge",
            "Technology",
            "Sports",
            "Car",
            "Life",
            "Food",
            "Animal",
            "Kichiku",
            "Fashion",
            "Entertainment",
            "Film & TV",
            "Documentary",
            "Movie",
            "TV play",
        ),
        (
            "Overall ranking",
            "Animation(Douga)",
            "",
            "",
            "Music",
            "Dance",
            "Game",
            "Knowledge",
            "Technology",
            "Sports",
            "Car",
            "Life",
            "Food",
            "Animal",
            "Kichiku",
            "Fashion",
            "Entertainment",
            "Film & TV",
            "Documentary",
            "Movie",
            "TV play",
        ),
        (
            "Overall ranking",
            "Animation(Douga)",
            "",
            "",
            "Music",
            "Dance",
            "Game",
            "Knowledge",
            "Technology",
            "Sports",
            "Car",
            "Life",
            "Food",
            "Animal",
            "Kichiku",
            "Fashion",
            "Entertainment",
            "Film & TV",
            "Documentary",
            "Movie",
            "TV play",
        ),
        (
            "Overall ranking",
            "Animation(Douga)",
            "",
            "",
            "Music",
            "Dance",
            "Game",
            "Knowledge",
            "Technology",
            "Sports",
            "Car",
            "Life",
            "Food",
            "Animal",
            "Kichiku",
            "Fashion",
            "Entertainment",
            "Film & TV",
            "Documentary",
            "Movie",
            "TV play",
        ),
        (
            "Overall ranking",
            "Animation(Douga)",
            "",
            "",
            "Music",
            "Dance",
            "Game",
            "Knowledge",
            "Technology",
            "Sports",
            "Car",
            "Life",
            "Food",
            "Animal",
            "Kichiku",
            "Fashion",
            "Entertainment",
            "Film & TV",
            "Documentary",
            "Movie",
            "TV play",
        ),
        (
            "Overall ranking",
            "Animation(Douga)",
            "",
            "",
            "Music",
            "Dance",
            "Game",
            "Knowledge",
            "Technology",
            "Sports",
            "Car",
            "Life",
            "Food",
            "Animal",
            "Kichiku",
            "Fashion",
            "Entertainment",
            "Film & TV",
            "Documentary",
            "Movie",
            "TV play",
        ),
    ]

    def overall(tid=None) -> None:
        url = "https://api.bilibili.com/x/web-interface/ranking/v2?"
        if tid != None:
            url += f"rid={tid}"
        try:
            page = read_api_response(request_api(url, headers=headers))
        except Exception as e:
            wl = [
                f"出现错误：{e}",
                f"An error has occurred: {e}",
                f"發生錯誤：{e}",
                f"エラーが発生しました：{e}",
                f"Ein Fehler ist aufgetreten: {e}",
                f"Une erreur est survenue: {e}",
                f"An error has occurred: {e}",
                f"An error has occurred: {e}",
                f"An error has occurred: {e}",
                f"An error has occurred: {e}",
                f"An error has occurred: {e}",
                f"An error has occurred: {e}",
                f"An error has occurred: {e}",
            ]
            showwarning(title=window_title, message=wl[lang])
            return None
        status_code = api_code(page)
        if status_code != 0:
            msg = api_message(page) if lang == 0 else translated_api_message(status_code, api_message(page))
            wl = [
                f"出现错误：{msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"發生錯誤：{msg}({status_code})",
                f"エラーが発生しました：{msg}({status_code})",
                f"Ein Fehler ist aufgetreten: {msg}({status_code})",
                f"Une erreur est survenue: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
            ]
            showwarning(title=window_title, message=wl[lang])
            return None
        data = page["data"]
        outpt()
        if lang == 0:
            output_text.insert(
                INSERT,
                data["note"] + "\n——————————————————————————————————————————————————\n",
            )
        else:
            output_text.insert(
                INSERT,
                foreign.lang1["排行"][lang - 1]
                + "\n——————————————————————————————————————————————————\n",
            )
        lst = data["list"]
        for i in lst:
            avid = i["aid"]
            bvid = i["bvid"]
            fp = i["videos"]
            tpn = i["tname"]
            tpid = i["tid"]
            title = i["title"]
            pbd = i["pubdate"]
            if lang == 0 or lang == 2 or lang == 3:
                pbdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(pbd))
            elif lang == 1:
                pbdate = time.strftime("%m-%d-%Y %H:%M:%S", time.localtime(pbd))
            elif lang == 4 or lang == 5:
                pbdate = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(pbd))
            desc = i["desc"]
            dura = "%02d:%02d" % divmod(i["duration"], 60)
            user_id = i["owner"]["mid"]
            uname = i["owner"]["name"]
            stat = i["stat"]
            view = stat["view"]
            danm = stat["danmaku"]
            rpl = stat["reply"]
            favo = stat["favorite"]
            coin = stat["coin"]
            shar = stat["share"]
            like = stat["like"]
            try:
                location = i["pub_location"]
            except Exception:
                no_info_msg = [
                    "无信息",
                    "No information",
                    "無信息",
                    "情報がありません",
                    "Keine Informationen",
                    "Aucune information",
                    "ไม่มีข้อมูล",
                    "정보 없음",
                    "Нет информации",
                    "Không có thông tin",
                    "Sem informação",
                    "Sin información",
                    "Tidak ada informasi",
                ]
                location = no_info_msg[lang]
            surl = i["short_link_v2"]
            if lang == 0:
                output_text.insert(
                    INSERT,
                    f"视频标题：\t\t{title}"
                    + f"\n视频AV号：\t\tav{avid}"
                    + f"\n视频BV号：\t\t{bvid}"
                    + f"\n视频简介：\n{desc}"
                    + f"\n视频总时长：\t\t{dura}"
                    + f"\n视频分区：\t\t{tpn}（{tpid}）"
                    + f"\n发布日期：\t\t{pbdate}"
                    + f"\n视频分P总数：\t\t{fp}"
                    + f"\n播放量：\t\t{view}"
                    + f"\n点赞量：\t\t{like}"
                    + f"\n收藏量：\t\t{favo}"
                    + f"\n弹幕量：\t\t{danm}"
                    + f"\n评论量：\t\t{rpl}"
                    + f"\n投币量：\t\t{coin}"
                    + f"\n分享量：\t\t{shar}"
                    + f"\n视频发布地区：\t\t{location}"
                    + f"\n视频短链接：\t\t{surl}"
                    + f"\nUP主昵称 / UID：\t\t{uname} / {user_id}",
                )
            elif lang == 1:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{title}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{bvid}"
                    + f"\nIntroduction:\n{desc}"
                    + f"\nTotal time:\t\t\t{dura}"
                    + f"\nPartition: \t\t\t{tpn} ({tpid})"
                    + f"\nAnnounce date:\t\t\t{pbdate}"
                    + f"\nVideo count:\t\t\t{fp}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nDanmaku count:\t\t\t{danm}"
                    + f"\nComment count:\t\t\t{rpl}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nShare count:\t\t\t{shar}"
                    + f"\nAnnounce location:\t\t\t{location}"
                    + f"\nVideo short link:\t\t\t{surl}"
                    + f"\nUP master's nickname / UID:\t\t\t{uname} / {user_id}",
                )
            elif lang == 2:
                output_text.insert(
                    INSERT,
                    f"視頻標題：\t\t{to_traditional(title)}"
                    + f"\n視頻AV號：\t\tav{avid}"
                    + f"\n視頻BV號：\t\t{bvid}"
                    + f"\n視頻簡介：\n{to_traditional(desc)}"
                    + f"\n視頻總時長：\t\t{dura}"
                    + f"\n視頻分區：\t\t{to_traditional(tpn)}（{tpid}）"
                    + f"\n發佈日期：\t\t{pbdate}"
                    + f"\n視頻分P總數：\t\t{fp}"
                    + f"\n播放量：\t\t{view}"
                    + f"\n點贊量：\t\t{like}"
                    + f"\n收藏量：\t\t{favo}"
                    + f"\n彈幕量：\t\t{danm}"
                    + f"\n評論量：\t\t{rpl}"
                    + f"\n投幣量：\t\t{coin}"
                    + f"\n分享量：\t\t{shar}"
                    + f"\n視頻發佈地區：\t\t{to_traditional(location)}"
                    + f"\n視頻短連結：\t\t{surl}"
                    + f"\nUP主暱稱 / UID：\t\t{uname} / {user_id}",
                )
            elif lang == 3:
                output_text.insert(
                    INSERT,
                    f"タイトル:\t\t\t{title}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{bvid}"
                    + f"\n紹介:\n{desc}"
                    + f"\n合計時間:\t\t\t{dura}"
                    + f"\nカテゴリ:\t\t\t{tpn}（{tpid}）"
                    + f"\n公開日:\t\t\t{pbdate}"
                    + f"\n動画数:\t\t\t{fp}"
                    + f"\n再生数:\t\t\t{view}"
                    + f"\nいいね数:\t\t\t{like}"
                    + f"\nお気に入り数:\t\t\t{favo}"
                    + f"\n弾幕数:\t\t\t{danm}"
                    + f"\nコメント数:\t\t\t{rpl}"
                    + f"\nコイン数:\t\t\t{coin}"
                    + f"\nシェア数:\t\t\t{shar}"
                    + f"\n投稿地域:\t\t\t{location}"
                    + f"\n動画の短縮リンク:\t\t\t{surl}"
                    + f"\nUP主ニックネーム / UID:\t\t\t{uname} / {user_id}",
                )
            elif lang == 4:
                output_text.insert(
                    INSERT,
                    f"Titel:\t\t\t{title}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{bvid}"
                    + f"\nEinleitung:\n{desc}"
                    + f"\nGesamtzeit:\t\t\t{dura}"
                    + f"\nPartition: \t\t\t{tpn} ({tpid})"
                    + f"\nVeröffentlichungsdatum:\t\t\t{pbdate}"
                    + f"\nAnzahl der Videos:\t\t\t{fp}"
                    + f"\nAufrufe:\t\t\t{view}"
                    + f"\nLikes:\t\t\t{like}"
                    + f"\nFavoriten:\t\t\t{favo}"
                    + f"\nDanmaku-Anzahl:\t\t\t{danm}"
                    + f"\nKommentare:\t\t\t{rpl}"
                    + f"\nMünzen:\t\t\t{coin}"
                    + f"\nShares:\t\t\t{shar}"
                    + f"\nUpload-Region:\t\t\t{location}"
                    + f"\nVideo-Kurzlink:\t\t\t{surl}"
                    + f"\nSpitzname des UP-Meisters / UID:\t\t\t{uname} / {user_id}",
                )
            elif lang == 5:
                output_text.insert(
                    INSERT,
                    f"Titre:\t\t\t{title}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{bvid}"
                    + f"\nPrésentation:\n{desc}"
                    + f"\nTemps total:\t\t\t{dura}"
                    + f"\nPartition : \t\t\t{tpn} ({tpid})"
                    + f"\nDate de publication:\t\t\t{pbdate}"
                    + f"\nNombre de vidéos:\t\t\t{fp}"
                    + f"\nNombre de vues:\t\t\t{view}"
                    + f"\nNombre de likes:\t\t\t{like}"
                    + f"\nNombre de favoris:\t\t\t{favo}"
                    + f"\nNombre de danmaku:\t\t\t{danm}"
                    + f"\nNombre de commentaires:\t\t\t{rpl}"
                    + f"\nNombre de pièces:\t\t\t{coin}"
                    + f"\nNombre de partages:\t\t\t{shar}"
                    + f"\nRégion de publication:\t\t\t{location}"
                    + f"\nLien court vers la vidéo:\t\t\t{surl}"
                    + f"\nSurnom de l’UP master / UID:\t\t\t{uname} / {user_id}",
                )
            elif lang == 6:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{title}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{bvid}"
                    + f"\nIntroduction:\n{desc}"
                    + f"\nTotal time:\t\t\t{dura}"
                    + f"\nPartition: \t\t\t{tpn} ({tpid})"
                    + f"\nAnnounce date:\t\t\t{pbdate}"
                    + f"\nVideo count:\t\t\t{fp}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nDanmaku count:\t\t\t{danm}"
                    + f"\nComment count:\t\t\t{rpl}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nShare count:\t\t\t{shar}"
                    + f"\nAnnounce location:\t\t\t{location}"
                    + f"\nVideo short link:\t\t\t{surl}"
                    + f"\nUP master's nickname / UID:\t\t\t{uname} / {user_id}",
                )
            elif lang == 7:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{title}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{bvid}"
                    + f"\nIntroduction:\n{desc}"
                    + f"\nTotal time:\t\t\t{dura}"
                    + f"\nPartition: \t\t\t{tpn} ({tpid})"
                    + f"\nAnnounce date:\t\t\t{pbdate}"
                    + f"\nVideo count:\t\t\t{fp}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nDanmaku count:\t\t\t{danm}"
                    + f"\nComment count:\t\t\t{rpl}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nShare count:\t\t\t{shar}"
                    + f"\nAnnounce location:\t\t\t{location}"
                    + f"\nVideo short link:\t\t\t{surl}"
                    + f"\nUP master's nickname / UID:\t\t\t{uname} / {user_id}",
                )
            elif lang == 8:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{title}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{bvid}"
                    + f"\nIntroduction:\n{desc}"
                    + f"\nTotal time:\t\t\t{dura}"
                    + f"\nPartition: \t\t\t{tpn} ({tpid})"
                    + f"\nAnnounce date:\t\t\t{pbdate}"
                    + f"\nVideo count:\t\t\t{fp}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nDanmaku count:\t\t\t{danm}"
                    + f"\nComment count:\t\t\t{rpl}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nShare count:\t\t\t{shar}"
                    + f"\nAnnounce location:\t\t\t{location}"
                    + f"\nVideo short link:\t\t\t{surl}"
                    + f"\nUP master's nickname / UID:\t\t\t{uname} / {user_id}",
                )
            elif lang == 9:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{title}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{bvid}"
                    + f"\nIntroduction:\n{desc}"
                    + f"\nTotal time:\t\t\t{dura}"
                    + f"\nPartition: \t\t\t{tpn} ({tpid})"
                    + f"\nAnnounce date:\t\t\t{pbdate}"
                    + f"\nVideo count:\t\t\t{fp}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nDanmaku count:\t\t\t{danm}"
                    + f"\nComment count:\t\t\t{rpl}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nShare count:\t\t\t{shar}"
                    + f"\nAnnounce location:\t\t\t{location}"
                    + f"\nVideo short link:\t\t\t{surl}"
                    + f"\nUP master's nickname / UID:\t\t\t{uname} / {user_id}",
                )
            elif lang == 10:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{title}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{bvid}"
                    + f"\nIntroduction:\n{desc}"
                    + f"\nTotal time:\t\t\t{dura}"
                    + f"\nPartition: \t\t\t{tpn} ({tpid})"
                    + f"\nAnnounce date:\t\t\t{pbdate}"
                    + f"\nVideo count:\t\t\t{fp}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nDanmaku count:\t\t\t{danm}"
                    + f"\nComment count:\t\t\t{rpl}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nShare count:\t\t\t{shar}"
                    + f"\nAnnounce location:\t\t\t{location}"
                    + f"\nVideo short link:\t\t\t{surl}"
                    + f"\nUP master's nickname / UID:\t\t\t{uname} / {user_id}",
                )
            elif lang == 11:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{title}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{bvid}"
                    + f"\nIntroduction:\n{desc}"
                    + f"\nTotal time:\t\t\t{dura}"
                    + f"\nPartition: \t\t\t{tpn} ({tpid})"
                    + f"\nAnnounce date:\t\t\t{pbdate}"
                    + f"\nVideo count:\t\t\t{fp}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nDanmaku count:\t\t\t{danm}"
                    + f"\nComment count:\t\t\t{rpl}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nShare count:\t\t\t{shar}"
                    + f"\nAnnounce location:\t\t\t{location}"
                    + f"\nVideo short link:\t\t\t{surl}"
                    + f"\nUP master's nickname / UID:\t\t\t{uname} / {user_id}",
                )
            elif lang == 12:
                output_text.insert(
                    INSERT,
                    f"Title:\t\t\t{title}"
                    + f"\nAVID:\t\t\tav{avid}"
                    + f"\nBVID:\t\t\t{bvid}"
                    + f"\nIntroduction:\n{desc}"
                    + f"\nTotal time:\t\t\t{dura}"
                    + f"\nPartition: \t\t\t{tpn} ({tpid})"
                    + f"\nAnnounce date:\t\t\t{pbdate}"
                    + f"\nVideo count:\t\t\t{fp}"
                    + f"\nPlay count:\t\t\t{view}"
                    + f"\nLike count:\t\t\t{like}"
                    + f"\nFavorite count:\t\t\t{favo}"
                    + f"\nDanmaku count:\t\t\t{danm}"
                    + f"\nComment count:\t\t\t{rpl}"
                    + f"\nCoin count:\t\t\t{coin}"
                    + f"\nShare count:\t\t\t{shar}"
                    + f"\nAnnounce location:\t\t\t{location}"
                    + f"\nVideo short link:\t\t\t{surl}"
                    + f"\nUP master's nickname / UID:\t\t\t{uname} / {user_id}",
                )
            output_text.insert(INSERT, "\n——————————————————————————————————————————————————\n")
        output_text.configure(state=DISABLED)

    douga = lambda: overall(1)
    music = lambda: overall(3)
    dance = lambda: overall(129)
    game = lambda: overall(4)
    know = lambda: overall(36)
    tech = lambda: overall(188)
    sports = lambda: overall(234)
    car = lambda: overall(223)
    life = lambda: overall(160)
    food = lambda: overall(211)
    animal = lambda: overall(217)
    kichiku = lambda: overall(119)
    fashion = lambda: overall(155)
    ent = lambda: overall(5)
    cinephile = lambda: overall(181)
    documentary = lambda: overall(177)
    movie = lambda: overall(23)
    tv = lambda: overall(11)
    bor = Button(sub_window, text=tool_labels[lang][0], command=overall, font=default_font)
    account_status = Button(sub_window, text=tool_labels[lang][1], command=douga, font=default_font)
    bmu = Button(sub_window, text=tool_labels[lang][4], command=music, font=default_font)
    bda = Button(sub_window, text=tool_labels[lang][5], command=dance, font=default_font)
    bga = Button(sub_window, text=tool_labels[lang][6], command=game, font=default_font)
    bkn = Button(sub_window, text=tool_labels[lang][7], command=know, font=default_font)
    btc = Button(sub_window, text=tool_labels[lang][8], command=tech, font=default_font)
    bsp = Button(sub_window, text=tool_labels[lang][9], command=sports, font=default_font)
    bca = Button(sub_window, text=tool_labels[lang][10], command=car, font=default_font)
    blf = Button(sub_window, text=tool_labels[lang][11], command=life, font=default_font)
    bfd = Button(sub_window, text=tool_labels[lang][12], command=food, font=default_font)
    bam = Button(sub_window, text=tool_labels[lang][13], command=animal, font=default_font)
    bkc = Button(sub_window, text=tool_labels[lang][14], command=kichiku, font=default_font)
    bfs = Button(sub_window, text=tool_labels[lang][15], command=fashion, font=default_font)
    ben = Button(sub_window, text=tool_labels[lang][16], command=ent, font=default_font)
    bci = Button(sub_window, text=tool_labels[lang][17], command=cinephile, font=default_font)
    bdc = Button(sub_window, text=tool_labels[lang][18], command=documentary, font=default_font)
    bmo = Button(sub_window, text=tool_labels[lang][19], command=movie, font=default_font)
    btv = Button(sub_window, text=tool_labels[lang][20], command=tv, font=default_font)
    bl = [
        bor,
        account_status,
        bmu,
        bda,
        bga,
        bkn,
        btc,
        bsp,
        bca,
        blf,
        bfd,
        bam,
        bkc,
        bfs,
        ben,
        bci,
        bdc,
        bmo,
        btv,
    ]
    for i in bl:
        i.pack()


def get_must_see() -> None:  # 获取入站必刷视频
    url = "https://api.bilibili.com/x/web-interface/popular/precious?"
    page = request_api(url, headers=headers)
    response_data = read_api_response(page)
    status_code = api_code(response_data)
    if status_code != 0:
        msg = api_message(response_data) if lang == 0 else translated_api_message(status_code, api_message(response_data))
        warning_msg = [
            f"出现错误：{msg}({status_code})",
            f"An error has occurred: {msg}({status_code})",
        ]
        showwarning(title=window_title, message=warning_msg[lang])
        return None
    data = response_data["data"]
    outpt()
    video_amount = data["explain"][11:-6]
    if lang == 0:
        output_text.insert(
            INSERT,
            data["title"]
            + "——"
            + data["explain"]
            + "\n——————————————————————————————————————————————————\n",
        )
    else:
        output_text.insert(
            INSERT,
            foreign.lang1["入站必刷"][lang - 1] % video_amount
            + "\n——————————————————————————————————————————————————\n",
        )
    lst = data["list"]
    for i in lst:
        avid = str(i["aid"])
        bvid = i["bvid"]
        fp = str(i["videos"])
        tpn = i["tname"]
        tpid = str(i["tid"])
        title = i["title"]
        pbd = i["pubdate"]
        if lang in [0, 2, 3, 7]:
            pbdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(pbd))
        elif lang in [1, 9]:
            pbdate = time.strftime("%m-%d-%Y %H:%M:%S", time.localtime(pbd))
        elif lang in [4, 5, 6, 8, 10, 11, 12]:
            pbdate = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(pbd))
        desc = i["desc"]
        dura = "%02d:%02d" % divmod(i["duration"], 60)
        user_id = str(i["owner"]["mid"])
        uname = i["owner"]["name"]
        stat = i["stat"]
        view = str(stat["view"])
        danm = str(stat["danmaku"])
        rpl = str(stat["reply"])
        favo = str(stat["favorite"])
        coin = str(stat["coin"])
        shar = str(stat["share"])
        like = str(stat["like"])
        try:
            location = i["pub_location"]
        except Exception:
            no_info_msg = [
                "无信息",
                "No information",
                "無信息",
                "No information",
                "No information",
                "No information",
                "No information",
                "No information",
                "No information",
                "No information",
                "No information",
                "No information",
                "No information",
            ]
            location = no_info_msg[lang]
        surl = i["short_link_v2"]
        reas = i["achievement"]
        if lang == 0:
            output_text.insert(
                INSERT,
                f"视频标题：\t\t{title}"
                + f"\n视频AV号：\t\tav{avid}"
                + f"\n视频BV号：\t\t{bvid}"
                + f"\n视频简介：\n{desc}"
                + f"\n视频总时长：\t\t{dura}"
                + f"\n视频分区：\t\t{tpn}（{tpid}）"
                + f"\n发布日期：\t\t{pbdate}"
                + f"\n视频分P总数：\t\t{fp}"
                + f"\n受推荐理由：\t\t{reas}"
                + f"\n播放量：\t\t{view}"
                + f"\n点赞量：\t\t{like}"
                + f"\n收藏量：\t\t{favo}"
                + f"\n弹幕量：\t\t{danm}"
                + f"\n评论量：\t\t{rpl}"
                + f"\n投币量：\t\t{coin}"
                + f"\n分享量：\t\t{shar}"
                + f"\n视频发布地区：\t\t{location}"
                + f"\n视频短链接：\t\t{surl}"
                + f"\nUP主昵称 / UID：\t\t{uname} / {user_id}",
            )
        elif lang == 1:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{title}"
                + f"\nAVID:\t\t\t\tav{avid}"
                + f"\nBVID:\t\t\t\t{bvid}"
                + f"\nIntroduction:\n{desc}"
                + f"\nTotal time:\t\t\t\t{dura}"
                + f"\nPartition: \t\t\t\t{tpn} ({tpid})"
                + f"\nAnnounce date:\t\t\t\t{pbdate}"
                + f"\nVideo count:\t\t\t\t{fp}"
                + f"\nReason to be recommended:\t\t\t\t{reas}"
                + f"\nPlay count:\t\t\t\t{view}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nDanmaku count:\t\t\t\t{danm}"
                + f"\nComment count:\t\t\t\t{rpl}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nShare count:\t\t\t\t{shar}"
                + f"\nAnnounce location:\t\t\t\t{location}"
                + f"\nVideo short link:\t\t\t\t{surl}"
                + f"\nUP master's nickname / UID:\t\t\t\t{uname} / {user_id}",
            )
        elif lang == 2:
            output_text.insert(
                INSERT,
                f"影片標題：\t\t{to_traditional(title)}"
                + f"\n影片AV號：\t\tav{avid}"
                + f"\n影片BV號：\t\t{bvid}"
                + f"\n影片簡介：\n{to_traditional(desc)}"
                + f"\n影片總時長：\t\t{dura}"
                + f"\n影片分區：\t\t{to_traditional(tpn)}（{tpid}）"
                + f"\n釋出日期：\t\t{pbdate}"
                + f"\n影片分P總數：\t\t{fp}"
                + f"\n受推薦理由：\t\t{to_traditional(reas)}"
                + f"\n播放量：\t\t{view}"
                + f"\n點贊量：\t\t{like}"
                + f"\n收藏量：\t\t{favo}"
                + f"\n彈幕量：\t\t{danm}"
                + f"\n評論量：\t\t{rpl}"
                + f"\n投幣量：\t\t{coin}"
                + f"\n分享量：\t\t{shar}"
                + f"\n影片釋出地區：\t\t{to_traditional(location)}"
                + f"\n影片短連結：\t\t{surl}"
                + f"\nUP主暱稱 / UID：\t\t{uname} / {user_id}",
            )
        elif lang == 3:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{title}"
                + f"\nAVID:\t\t\t\tav{avid}"
                + f"\nBVID:\t\t\t\t{bvid}"
                + f"\nIntroduction:\n{desc}"
                + f"\nTotal time:\t\t\t\t{dura}"
                + f"\nPartition: \t\t\t\t{tpn} ({tpid})"
                + f"\nAnnounce date:\t\t\t\t{pbdate}"
                + f"\nVideo count:\t\t\t\t{fp}"
                + f"\nReason to be recommended:\t\t\t\t{reas}"
                + f"\nPlay count:\t\t\t\t{view}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nDanmaku count:\t\t\t\t{danm}"
                + f"\nComment count:\t\t\t\t{rpl}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nShare count:\t\t\t\t{shar}"
                + f"\nAnnounce location:\t\t\t\t{location}"
                + f"\nVideo short link:\t\t\t\t{surl}"
                + f"\nUP master's nickname / UID:\t\t\t\t{uname} / {user_id}",
            )
        elif lang == 4:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{title}"
                + f"\nAVID:\t\t\t\tav{avid}"
                + f"\nBVID:\t\t\t\t{bvid}"
                + f"\nIntroduction:\n{desc}"
                + f"\nTotal time:\t\t\t\t{dura}"
                + f"\nPartition: \t\t\t\t{tpn} ({tpid})"
                + f"\nAnnounce date:\t\t\t\t{pbdate}"
                + f"\nVideo count:\t\t\t\t{fp}"
                + f"\nReason to be recommended:\t\t\t\t{reas}"
                + f"\nPlay count:\t\t\t\t{view}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nDanmaku count:\t\t\t\t{danm}"
                + f"\nComment count:\t\t\t\t{rpl}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nShare count:\t\t\t\t{shar}"
                + f"\nAnnounce location:\t\t\t\t{location}"
                + f"\nVideo short link:\t\t\t\t{surl}"
                + f"\nUP master's nickname / UID:\t\t\t\t{uname} / {user_id}",
            )
        elif lang == 5:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{title}"
                + f"\nAVID:\t\t\t\tav{avid}"
                + f"\nBVID:\t\t\t\t{bvid}"
                + f"\nIntroduction:\n{desc}"
                + f"\nTotal time:\t\t\t\t{dura}"
                + f"\nPartition: \t\t\t\t{tpn} ({tpid})"
                + f"\nAnnounce date:\t\t\t\t{pbdate}"
                + f"\nVideo count:\t\t\t\t{fp}"
                + f"\nReason to be recommended:\t\t\t\t{reas}"
                + f"\nPlay count:\t\t\t\t{view}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nDanmaku count:\t\t\t\t{danm}"
                + f"\nComment count:\t\t\t\t{rpl}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nShare count:\t\t\t\t{shar}"
                + f"\nAnnounce location:\t\t\t\t{location}"
                + f"\nVideo short link:\t\t\t\t{surl}"
                + f"\nUP master's nickname / UID:\t\t\t\t{uname} / {user_id}",
            )
        elif lang == 6:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{title}"
                + f"\nAVID:\t\t\t\tav{avid}"
                + f"\nBVID:\t\t\t\t{bvid}"
                + f"\nIntroduction:\n{desc}"
                + f"\nTotal time:\t\t\t\t{dura}"
                + f"\nPartition: \t\t\t\t{tpn} ({tpid})"
                + f"\nAnnounce date:\t\t\t\t{pbdate}"
                + f"\nVideo count:\t\t\t\t{fp}"
                + f"\nReason to be recommended:\t\t\t\t{reas}"
                + f"\nPlay count:\t\t\t\t{view}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nDanmaku count:\t\t\t\t{danm}"
                + f"\nComment count:\t\t\t\t{rpl}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nShare count:\t\t\t\t{shar}"
                + f"\nAnnounce location:\t\t\t\t{location}"
                + f"\nVideo short link:\t\t\t\t{surl}"
                + f"\nUP master's nickname / UID:\t\t\t\t{uname} / {user_id}",
            )
        elif lang == 7:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{title}"
                + f"\nAVID:\t\t\t\tav{avid}"
                + f"\nBVID:\t\t\t\t{bvid}"
                + f"\nIntroduction:\n{desc}"
                + f"\nTotal time:\t\t\t\t{dura}"
                + f"\nPartition: \t\t\t\t{tpn} ({tpid})"
                + f"\nAnnounce date:\t\t\t\t{pbdate}"
                + f"\nVideo count:\t\t\t\t{fp}"
                + f"\nReason to be recommended:\t\t\t\t{reas}"
                + f"\nPlay count:\t\t\t\t{view}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nDanmaku count:\t\t\t\t{danm}"
                + f"\nComment count:\t\t\t\t{rpl}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nShare count:\t\t\t\t{shar}"
                + f"\nAnnounce location:\t\t\t\t{location}"
                + f"\nVideo short link:\t\t\t\t{surl}"
                + f"\nUP master's nickname / UID:\t\t\t\t{uname} / {user_id}",
            )
        elif lang == 8:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{title}"
                + f"\nAVID:\t\t\t\tav{avid}"
                + f"\nBVID:\t\t\t\t{bvid}"
                + f"\nIntroduction:\n{desc}"
                + f"\nTotal time:\t\t\t\t{dura}"
                + f"\nPartition: \t\t\t\t{tpn} ({tpid})"
                + f"\nAnnounce date:\t\t\t\t{pbdate}"
                + f"\nVideo count:\t\t\t\t{fp}"
                + f"\nReason to be recommended:\t\t\t\t{reas}"
                + f"\nPlay count:\t\t\t\t{view}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nDanmaku count:\t\t\t\t{danm}"
                + f"\nComment count:\t\t\t\t{rpl}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nShare count:\t\t\t\t{shar}"
                + f"\nAnnounce location:\t\t\t\t{location}"
                + f"\nVideo short link:\t\t\t\t{surl}"
                + f"\nUP master's nickname / UID:\t\t\t\t{uname} / {user_id}",
            )
        elif lang == 9:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{title}"
                + f"\nAVID:\t\t\t\tav{avid}"
                + f"\nBVID:\t\t\t\t{bvid}"
                + f"\nIntroduction:\n{desc}"
                + f"\nTotal time:\t\t\t\t{dura}"
                + f"\nPartition: \t\t\t\t{tpn} ({tpid})"
                + f"\nAnnounce date:\t\t\t\t{pbdate}"
                + f"\nVideo count:\t\t\t\t{fp}"
                + f"\nReason to be recommended:\t\t\t\t{reas}"
                + f"\nPlay count:\t\t\t\t{view}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nDanmaku count:\t\t\t\t{danm}"
                + f"\nComment count:\t\t\t\t{rpl}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nShare count:\t\t\t\t{shar}"
                + f"\nAnnounce location:\t\t\t\t{location}"
                + f"\nVideo short link:\t\t\t\t{surl}"
                + f"\nUP master's nickname / UID:\t\t\t\t{uname} / {user_id}",
            )
        elif lang == 10:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{title}"
                + f"\nAVID:\t\t\t\tav{avid}"
                + f"\nBVID:\t\t\t\t{bvid}"
                + f"\nIntroduction:\n{desc}"
                + f"\nTotal time:\t\t\t\t{dura}"
                + f"\nPartition: \t\t\t\t{tpn} ({tpid})"
                + f"\nAnnounce date:\t\t\t\t{pbdate}"
                + f"\nVideo count:\t\t\t\t{fp}"
                + f"\nReason to be recommended:\t\t\t\t{reas}"
                + f"\nPlay count:\t\t\t\t{view}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nDanmaku count:\t\t\t\t{danm}"
                + f"\nComment count:\t\t\t\t{rpl}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nShare count:\t\t\t\t{shar}"
                + f"\nAnnounce location:\t\t\t\t{location}"
                + f"\nVideo short link:\t\t\t\t{surl}"
                + f"\nUP master's nickname / UID:\t\t\t\t{uname} / {user_id}",
            )
        elif lang == 11:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{title}"
                + f"\nAVID:\t\t\t\tav{avid}"
                + f"\nBVID:\t\t\t\t{bvid}"
                + f"\nIntroduction:\n{desc}"
                + f"\nTotal time:\t\t\t\t{dura}"
                + f"\nPartition: \t\t\t\t{tpn} ({tpid})"
                + f"\nAnnounce date:\t\t\t\t{pbdate}"
                + f"\nVideo count:\t\t\t\t{fp}"
                + f"\nReason to be recommended:\t\t\t\t{reas}"
                + f"\nPlay count:\t\t\t\t{view}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nDanmaku count:\t\t\t\t{danm}"
                + f"\nComment count:\t\t\t\t{rpl}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nShare count:\t\t\t\t{shar}"
                + f"\nAnnounce location:\t\t\t\t{location}"
                + f"\nVideo short link:\t\t\t\t{surl}"
                + f"\nUP master's nickname / UID:\t\t\t\t{uname} / {user_id}",
            )
        elif lang == 12:
            output_text.insert(
                INSERT,
                f"Title:\t\t\t\t{title}"
                + f"\nAVID:\t\t\t\tav{avid}"
                + f"\nBVID:\t\t\t\t{bvid}"
                + f"\nIntroduction:\n{desc}"
                + f"\nTotal time:\t\t\t\t{dura}"
                + f"\nPartition: \t\t\t\t{tpn} ({tpid})"
                + f"\nAnnounce date:\t\t\t\t{pbdate}"
                + f"\nVideo count:\t\t\t\t{fp}"
                + f"\nReason to be recommended:\t\t\t\t{reas}"
                + f"\nPlay count:\t\t\t\t{view}"
                + f"\nLike count:\t\t\t\t{like}"
                + f"\nFavorite count:\t\t\t\t{favo}"
                + f"\nDanmaku count:\t\t\t\t{danm}"
                + f"\nComment count:\t\t\t\t{rpl}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nShare count:\t\t\t\t{shar}"
                + f"\nAnnounce location:\t\t\t\t{location}"
                + f"\nVideo short link:\t\t\t\t{surl}"
                + f"\nUP master's nickname / UID:\t\t\t\t{uname} / {user_id}",
            )
        output_text.insert(INSERT, "\n——————————————————————————————————————————————————\n")
    output_text.configure(state=DISABLED)


def view_fan_changes() -> None:  # 查看用户粉丝实时变动数据
    user_id = askinteger(title=window_title, minvalue=1, prompt={
        LANG_CN: "输入B站UID...", LANG_TC: "輸入B站UID...",
    }.get(lang, "Input Bilibili UID..."))
    if user_id is None:
        return
    interval = askfloat(title=window_title, minvalue=1, prompt={
        LANG_CN: "输入请求间隔（秒）...", LANG_TC: "輸入請求間隔（秒）...",
    }.get(lang, "Request interval in seconds..."))
    if interval is None:
        return

    from queue import Empty, SimpleQueue

    outlabel()
    monitor_window = output_window
    label = Label(monitor_window, font=default_font)
    label.pack()
    stopped = threading.Event()
    updates = SimpleQueue()
    monitor_window.bind("<Destroy>", lambda event: stopped.set() if event.widget == monitor_window else None)
    url = f"https://api.bilibili.com/x/web-interface/card?mid={user_id}"
    monitor_headers = {**headers, "Referer": f"https://space.bilibili.com/{user_id}/"}
    caption = {
        LANG_CN: "UID：{}，昵称：{}，粉丝数量：{}",
        LANG_TC: "UID：{}，暱稱：{}，粉絲數量：{}",
    }.get(lang, "UID: {}, Nickname: {}, Fan count: {}")

    def collect():
        while not stopped.is_set():
            try:
                result = api_data(request_api(url, headers=monitor_headers))
                card = result.get("card")
                if not isinstance(card, dict):
                    raise APIError("未返回用户名片 / No user card returned")
                text = caption.format(user_id, card.get("name", "—"), result.get("follower", card.get("fans", "—")))
            except APIError as error:
                text = str(error)
            except OSError:
                text = "请求失败或超时 / Request failed or timed out"
            if stopped.is_set():
                break
            text = time.strftime("%Y-%m-%d %H:%M:%S") + "  " + text
            try:
                write_to_file(f"User_{user_id}_Fans_Real-time_Data.txt", text + "\n")
            except (OSError, UnicodeError):
                text += "\n日志写入失败 / Could not write the log"
            updates.put(text)
            stopped.wait(interval)

    def show_update():
        try:
            while True:
                label.configure(text=updates.get_nowait())
        except Empty:
            monitor_window.after(200, show_update)

    threading.Thread(target=collect, daemon=True).start()
    show_update()


def logged_user_info() -> None:  # 登录用户信息
    url = "https://api.bilibili.com/x/space/myinfo?"
    for t in range(1, MAX_RETRIES + 1):
        try:
            page = request_api(url, headers=headers)
        except Exception as e:
            if t < MAX_RETRIES:
                pass
            else:
                error_text = str(e)
                error_msgs = [
                    f"请求尝试{t}次后仍然发生错误：{error_text}",
                    f"The request still failed after {t} attempts: {error_text}",
                    f"請求嘗試{t}次後仍然發生錯誤：{error_text}",
                    f"要求を {t} 回試行した後もエラーが発生しました： {error_text}",
                    f"Nach {t} Versuchen an der Anforderung trat immer noch ein Fehler auf: {error_text}",
                    f"Une erreur se produisait encore après {t} tentatives de requête : {error_text}",
                    f"ข้อผิดพลาดยังคงเกิดขึ้นหลังจาก {t} ครั้งของความพยายามที่คําขอ: {error_text}",
                    f"요청을 {t}번 시도한 후에도 오류가 계속 발생했습니다: {error_text}",
                    f"Ошибка по-прежнему возникала после {t} попыток выполнения запроса: {error_text}",
                    f"Vẫn xảy ra lỗi sau {t} lần thử yêu cầu: {error_text}",
                    f"Ainda ocorreu um erro após {t} vezes de tentativas na solicitação: {error_text}",
                    f"Todavía se ha producido un error después de {t} veces de intentos en la solicitud: {error_text}",
                    f"Kesalahan masih terjadi setelah {t} kali upaya permintaan: {error_text}",
                ]
                showwarning(title=window_title, message=error_msgs[lang])
                return None
        else:
            break
    response_data = read_api_response(page)
    status_code = api_code(response_data)
    if status_code != 0:
        msge = api_message(response_data) if lang == 0 else translated_api_message(status_code, api_message(response_data))
        showwarning(title=window_title, message=msge + "(" + str(status_code) + ")")
    else:
        data = response_data["data"]
        user_id = str(data["mid"])
        uname = data["name"]
        sex = translated_api_message(data.get("sex"), data.get("sex") or "—")
        account_status = data["silence"]
        signature = data.get("sign") or data.get("signature") or ""
        lv = str(data["level"])
        banl = [
            ("正常", "被封禁"),
            ("Normal", "Banned"),
            ("正常", "被封禁"),
            ("正常", "禁止"),
            ("Normal", "Verboten"),
            ("Normal", "Interdit"),
            ("ปกติ", "ห้าม"),
            ("보통", "금지"),
            ("Нормальный", "Запрещены"),
            ("Bình thường", "Bị cấm"),
            ("Normal", "Banned"),
            ("Normal", "Banned"),
            ("Normal", "Banned"),
        ]
        account_status = banl[lang][account_status]
        vip = data.get("vip") or {}
        vip_status = (vip.get("label") or vip.get("Label") or {}).get("text") or ""
        if vip_status == "":
            novipl = [
                "未开通大会员或已过期",
                "Big Member is not activated or has expired",
                "未開通大會員或已過期",
                "ビッグメンバーが開いていないか、古くなっています",
                "Big-Member ist nicht aktiviert oder abgelaufen",
                "Big Member n’est pas activé ou a expiré",
                "สมาชิกรายใหญ่ไม่ได้เปิดหรือล้าสมัย",
                "큰 멤버가 열려 있지 않거나 오래되었습니다.",
                "Big Member не активирован или срок его действия истёк",
                "Thành viên lớn không được mở hoặc lỗi thời",
                "Big Member is not activated or has expired",
                "Big Member is not activated or has expired",
                "Big Member is not activated or has expired",
            ]
            vip_status = novipl[lang]
        elif lang != 0:
            vip_status = translated_api_message(vip_status, vip_status)
        official = data.get("Official") or data.get("official") or {}
        verification_status = official.get("role", 0)
        offict = official.get("title") or ""
        if verification_status == 0:
            verification_status = "未认证"
        elif 1 <= verification_status <= 2 or 7 <= verification_status <= 9:
            verification_status = "个人认证："
        elif 3 <= verification_status <= 6:
            verification_status = "机构认证："
        verification_status = translated_api_message(verification_status, str(verification_status)) + offict
        coin = str(data.get("coins", "—"))
        birth = data.get("birthday")
        if not isinstance(birth, (int, float)) or birth <= 0:
            nobirthday = [
                "无生日数据",
                "No birthday data",
                "無生日數據",
                "誕生日データなし",
                "Keine Geburtstagsdaten",
                "Pas de données sur la date de naissance",
                "ไม่มีข้อมูลวันเกิด",
                "생일 데이터 없음",
                "Нет данных о дате рождения",
                "Không có dữ liệu ngày sinh",
                "No birthday data",
                "No birthday data",
                "No birthday data",
            ]
            birthday = nobirthday[lang]
        else:
            birthday = time_convert(birth, 2)
        pend = data["pendant"]
        pendid = pend["pid"]
        nothing = [
            "无",
            "Nothing",
            "無",
            "何もない",
            "Nichts",
            "Rien",
            "ไม่มีอะไร",
            "무",
            "Ничто",
            "Không có",
            "Nothing",
            "Nothing",
            "Nothing",
        ]
        if pendid == 0:
            pendn = nothing[lang]
        else:
            pendn = pend["name"]
        np = data["nameplate"]
        npid = np["nid"]
        if npid == 0:
            npn = nothing[lang]
        else:
            if lang == 0:
                npn = np["name"] + "——" + np["level"] + "：" + np["condition"]
            else:
                npl = foreign.lang1[np["level"]][lang - 1]
                npn = np["name"] + "——" + npl + ": " + np["condition"]
        detail_url = "https://api.bilibili.com/x/relation/stat?vmid=" + user_id
        soup2 = require_api_success(read_api_response(request_api(detail_url, headers=headers)))
        fans = str(soup2["data"]["follower"])
        follow = str(soup2["data"]["following"])
        jointime = "—"
        try:
            calendar = api_data(request_api(
                "https://member.bilibili.com/x2/creative/h5/calendar/event?ts=0", headers=headers,
            ))
            profile = ((calendar.get("pfs") or {}).get("profile") or {})
            joined_at = profile.get("jointime")
            if isinstance(joined_at, (int, float)) and joined_at > 0:
                jointime = time_convert(joined_at)
        except (APIError, OSError):
            # The creator calendar may be unavailable to this account.
            pass
        url4 = "https://api.bilibili.com/x/web-interface/nav?"
        data4 = api_data(request_api(url4, headers=headers))
        vip_due = data4.get("vipDueDate")
        viptime = time_convert(vip_due // 1000) if isinstance(vip_due, int) and vip_due > 0 else "—"
        issm = data4.get("is_senior_member")
        moral = str(data4.get("moral", data.get("moral", "—")))
        em = data4.get("email_verified", data.get("email_status"))
        mble = data4.get("mobile_verified", data.get("tel_status"))
        isjr = data4.get("is_jury")
        smjr = [
            [("否", "是"), ("未验证", "已验证")],
            [("No", "Yes"), ("Uncertificated", "Certificated")],
            [("否", "是"), ("未驗證", "已驗證")],
            [("いいえ", "はい"), ("未認証", "認定済み")],
            [("Nein", "Ja"), ("Unzertifiziert", "Zertifiziert")],
            [("Non", "Oui"), ("Sans certificat", "Certifié")],
            [("ไม่ใช่", "ใช่"), ("ไม่ได้รับการรับรอง", "รับรอง")],
            [("아니요", "예"), ("인증되지 않음", "인증")],
            [("Нет", "Да"), ("Не подтверждён", "Подтверждён")],
            [("Không", "Có"), ("Chưa được cấp giấy chứng nhận", "Chứng nhận")],
            [("No", "Yes"), ("Uncertificated", "Certificated")],
            [("No", "Yes"), ("Uncertificated", "Certificated")],
            [("No", "Yes"), ("Uncertificated", "Certificated")],
        ]
        seniormember = smjr[lang][0][issm] if issm in (0, 1) else "—"
        jury = smjr[lang][0][isjr] if isjr in (0, 1) else "—"
        mobile = smjr[lang][1][mble] if mble in (0, 1) else "—"
        email = smjr[lang][1][em] if em in (0, 1) else "—"
        wallet = data4.get("wallet") or {}
        bcoin = str(wallet.get("bcoin_balance", "—"))
        coupon = str(wallet.get("coupon_balance", "—"))
        exp = str((data4.get("level_info") or {}).get("current_exp", "—"))
        outpt()
        attempt_msg = [
            f"请求共尝试了{t}次。\n",
            f"The request was attempted {t} time(s).\n",
            f"請求共嘗試了{t}次。\n",
            f"要求は {t} 回試行されました。\n",
            f"Die Anfrage wurde {t} Mal versucht.\n",
            f"La demande a été tentée {t} fois.\n",
            f"คําขอถูกพยายามเป็นเวลา {t} ครั้ง\n",
            f"요청이 {t}번 시도되었습니다.\n",
            f"Запрос был выполнен в течение {t} раз.\n",
            f"Yêu cầu đã được cố gắng cho {t} lần.\n",
            f"O pedido foi tentado por {t} vezes.\n",
            f"La solicitud se intentó {t} veces.\n",
            f"Permintaan itu dicoba untuk {t} kali.\n",
        ]
        output_text.insert(INSERT, attempt_msg[lang])
        if lang == 0:
            output_text.insert(
                INSERT,
                f"昵称：\t\t{uname}"
                + f"\nUID：\t\t{user_id}"
                + f"\n性别：\t\t{sex}"
                + f"\n大会员状态：\t\t{vip_status}"
                + f"\n大会员到期时间：\t\t{viptime}"
                + f"\n入站时间：\t\t{jointime}"
                + f"\n认证状态：\t\t{verification_status}"
                + f"\n账号状态：\t\t{account_status}"
                + f"\n粉丝数：\t\t{fans}"
                + f"\n关注数：\t\t{follow}"
                + f"\n硬币数量：\t\t{coin}"
                + f"\nB币数量：\t\t{bcoin}"
                + f"\n其中B币券数量：\t\t{coupon}"
                + f"\n签名：\n{signature}"
                + f"\n等级：\t\t{lv}"
                + f"\n当前经验：\t\t{exp}"
                + f"\n生日：\t\t{birthday}"
                + f"\n头像框：\t\t{pendn}"
                + f"\n勋章：\t\t{npn}"
                + f"\n手机验证状态：\t\t{mobile}"
                + f"\n邮箱验证状态：\t\t{email}"
                + f"\n是否为硬核会员：\t\t{seniormember}"
                + f"\n是否为风纪委员：\t\t{jury}"
                + f"\n节操值：\t\t{moral}"
                + f"\nB站空间：\t\thttps://space.bilibili.com/{user_id}",
            )
        elif lang == 1:
            output_text.insert(
                INSERT,
                f"Nickname:\t\t\t\t{uname}"
                + f"\nUID:\t\t\t\t{user_id}"
                + f"\nGender:\t\t\t\t{sex}"
                + f"\nBig Member status:\t\t\t\t{vip_status}"
                + f"\nBig Member expiration date:\t\t\t\t{viptime}"
                + f"\nTime of joining Bilibili:\t\t\t\t{jointime}"
                + f"\nCertification status:\t\t\t\t{verification_status}"
                + f"\nAccount Status:\t\t\t\t{account_status}"
                + f"\nFans count:\t\t\t\t{fans}"
                + f"\nFollow count:\t\t\t\t{follow}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nB Coin count:\t\t\t\t{bcoin}"
                + f"\nB Coin coupons:\t\t\t\t{coupon}"
                + f"\nSign:\n{signature}"
                + f"\nLevel:\t\t\t\t{lv}"
                + f"\nCurrent EXP:\t\t\t\t{exp}"
                + f"\nBirthday:\t\t\t\t{birthday}"
                + f"\nAvatar frame:\t\t\t\t{pendn}"
                + f"\nNameplate:\t\t\t\t{npn}"
                + f"\nPhone verification status:\t\t\t\t{mobile}"
                + f"\nEmail verification status:\t\t\t\t{email}"
                + f"\nSenior member:\t\t\t\t{seniormember}"
                + f"\nJury member:\t\t\t\t{jury}"
                + f"\nMoral value:\t\t\t\t{moral}"
                + f"\nBilibili space link:\t\t\t\thttps://space.bilibili.com/{user_id}",
            )
        elif lang == 2:
            output_text.insert(
                INSERT,
                f"暱稱：\t\t{uname}"
                + f"\nUID：\t\t{user_id}"
                + f"\n性別：\t\t{sex}"
                + f"\n大會員狀態：\t\t{vip_status}"
                + f"\n大會員到期時間：\t\t{viptime}"
                + f"\n入站時間：\t\t{jointime}"
                + f"\n認證狀態：\t\t{to_traditional(verification_status)}"
                + f"\n賬號狀態：\t\t{account_status}"
                + f"\n粉絲數：\t\t{fans}"
                + f"\n關注數：\t\t{follow}"
                + f"\n硬幣數量：\t\t{coin}"
                + f"\nB幣數量：\t\t{bcoin}"
                + f"\n其中B幣券數量：\t\t{coupon}"
                + f"\n簽名：\n{to_traditional(signature)}"
                + f"\n等級：\t\t{lv}"
                + f"\n當前經驗：\t\t{exp}"
                + f"\n生日：\t\t{birthday}"
                + f"\n頭像框：\t\t{to_traditional(pendn)}"
                + f"\n勳章：\t\t{to_traditional(npn)}"
                + f"\n手機驗證狀態：\t\t{mobile}"
                + f"\n郵箱驗證狀態：\t\t{email}"
                + f"\n是否為硬核會員：\t\t{seniormember}"
                + f"\n是否為風紀委員：\t\t{jury}"
                + f"\n節操值：\t\t{moral}"
                + f"\nB站空間：\t\thttps://space.bilibili.com/{user_id}",
            )
        elif lang == 3:
            output_text.insert(
                INSERT,
                f"Nickname:\t\t\t\t{uname}"
                + f"\nUID:\t\t\t\t{user_id}"
                + f"\nGender:\t\t\t\t{sex}"
                + f"\nBig Member status:\t\t\t\t{vip_status}"
                + f"\nBig Member expiration date:\t\t\t\t{viptime}"
                + f"\nTime of joining Bilibili:\t\t\t\t{jointime}"
                + f"\nCertification status:\t\t\t\t{verification_status}"
                + f"\nAccount Status:\t\t\t\t{account_status}"
                + f"\nFans count:\t\t\t\t{fans}"
                + f"\nFollow count:\t\t\t\t{follow}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nB Coin count:\t\t\t\t{bcoin}"
                + f"\nB Coin coupons:\t\t\t\t{coupon}"
                + f"\nSign:\n{signature}"
                + f"\nLevel:\t\t\t\t{lv}"
                + f"\nCurrent EXP:\t\t\t\t{exp}"
                + f"\nBirthday:\t\t\t\t{birthday}"
                + f"\nAvatar frame:\t\t\t\t{pendn}"
                + f"\nNameplate:\t\t\t\t{npn}"
                + f"\nPhone verification status:\t\t\t\t{mobile}"
                + f"\nEmail verification status:\t\t\t\t{email}"
                + f"\nSenior member:\t\t\t\t{seniormember}"
                + f"\nJury member:\t\t\t\t{jury}"
                + f"\nMoral value:\t\t\t\t{moral}"
                + f"\nBilibili space link:\t\t\t\thttps://space.bilibili.com/{user_id}",
            )
        elif lang == 4:
            output_text.insert(
                INSERT,
                f"Nickname:\t\t\t\t{uname}"
                + f"\nUID:\t\t\t\t{user_id}"
                + f"\nGender:\t\t\t\t{sex}"
                + f"\nBig Member status:\t\t\t\t{vip_status}"
                + f"\nBig Member expiration date:\t\t\t\t{viptime}"
                + f"\nTime of joining Bilibili:\t\t\t\t{jointime}"
                + f"\nCertification status:\t\t\t\t{verification_status}"
                + f"\nAccount Status:\t\t\t\t{account_status}"
                + f"\nFans count:\t\t\t\t{fans}"
                + f"\nFollow count:\t\t\t\t{follow}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nB Coin count:\t\t\t\t{bcoin}"
                + f"\nB Coin coupons:\t\t\t\t{coupon}"
                + f"\nSign:\n{signature}"
                + f"\nLevel:\t\t\t\t{lv}"
                + f"\nCurrent EXP:\t\t\t\t{exp}"
                + f"\nBirthday:\t\t\t\t{birthday}"
                + f"\nAvatar frame:\t\t\t\t{pendn}"
                + f"\nNameplate:\t\t\t\t{npn}"
                + f"\nPhone verification status:\t\t\t\t{mobile}"
                + f"\nEmail verification status:\t\t\t\t{email}"
                + f"\nSenior member:\t\t\t\t{seniormember}"
                + f"\nJury member:\t\t\t\t{jury}"
                + f"\nMoral value:\t\t\t\t{moral}"
                + f"\nBilibili space link:\t\t\t\thttps://space.bilibili.com/{user_id}",
            )
        elif lang == 5:
            output_text.insert(
                INSERT,
                f"Nickname:\t\t\t\t{uname}"
                + f"\nUID:\t\t\t\t{user_id}"
                + f"\nGender:\t\t\t\t{sex}"
                + f"\nBig Member status:\t\t\t\t{vip_status}"
                + f"\nBig Member expiration date:\t\t\t\t{viptime}"
                + f"\nTime of joining Bilibili:\t\t\t\t{jointime}"
                + f"\nCertification status:\t\t\t\t{verification_status}"
                + f"\nAccount Status:\t\t\t\t{account_status}"
                + f"\nFans count:\t\t\t\t{fans}"
                + f"\nFollow count:\t\t\t\t{follow}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nB Coin count:\t\t\t\t{bcoin}"
                + f"\nB Coin coupons:\t\t\t\t{coupon}"
                + f"\nSign:\n{signature}"
                + f"\nLevel:\t\t\t\t{lv}"
                + f"\nCurrent EXP:\t\t\t\t{exp}"
                + f"\nBirthday:\t\t\t\t{birthday}"
                + f"\nAvatar frame:\t\t\t\t{pendn}"
                + f"\nNameplate:\t\t\t\t{npn}"
                + f"\nPhone verification status:\t\t\t\t{mobile}"
                + f"\nEmail verification status:\t\t\t\t{email}"
                + f"\nSenior member:\t\t\t\t{seniormember}"
                + f"\nJury member:\t\t\t\t{jury}"
                + f"\nMoral value:\t\t\t\t{moral}"
                + f"\nBilibili space link:\t\t\t\thttps://space.bilibili.com/{user_id}",
            )
        elif lang == 6:
            output_text.insert(
                INSERT,
                f"Nickname:\t\t\t\t{uname}"
                + f"\nUID:\t\t\t\t{user_id}"
                + f"\nGender:\t\t\t\t{sex}"
                + f"\nBig Member status:\t\t\t\t{vip_status}"
                + f"\nBig Member expiration date:\t\t\t\t{viptime}"
                + f"\nTime of joining Bilibili:\t\t\t\t{jointime}"
                + f"\nCertification status:\t\t\t\t{verification_status}"
                + f"\nAccount Status:\t\t\t\t{account_status}"
                + f"\nFans count:\t\t\t\t{fans}"
                + f"\nFollow count:\t\t\t\t{follow}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nB Coin count:\t\t\t\t{bcoin}"
                + f"\nB Coin coupons:\t\t\t\t{coupon}"
                + f"\nSign:\n{signature}"
                + f"\nLevel:\t\t\t\t{lv}"
                + f"\nCurrent EXP:\t\t\t\t{exp}"
                + f"\nBirthday:\t\t\t\t{birthday}"
                + f"\nAvatar frame:\t\t\t\t{pendn}"
                + f"\nNameplate:\t\t\t\t{npn}"
                + f"\nPhone verification status:\t\t\t\t{mobile}"
                + f"\nEmail verification status:\t\t\t\t{email}"
                + f"\nSenior member:\t\t\t\t{seniormember}"
                + f"\nJury member:\t\t\t\t{jury}"
                + f"\nMoral value:\t\t\t\t{moral}"
                + f"\nBilibili space link:\t\t\t\thttps://space.bilibili.com/{user_id}",
            )
        elif lang == 7:
            output_text.insert(
                INSERT,
                f"Nickname:\t\t\t\t{uname}"
                + f"\nUID:\t\t\t\t{user_id}"
                + f"\nGender:\t\t\t\t{sex}"
                + f"\nBig Member status:\t\t\t\t{vip_status}"
                + f"\nBig Member expiration date:\t\t\t\t{viptime}"
                + f"\nTime of joining Bilibili:\t\t\t\t{jointime}"
                + f"\nCertification status:\t\t\t\t{verification_status}"
                + f"\nAccount Status:\t\t\t\t{account_status}"
                + f"\nFans count:\t\t\t\t{fans}"
                + f"\nFollow count:\t\t\t\t{follow}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nB Coin count:\t\t\t\t{bcoin}"
                + f"\nB Coin coupons:\t\t\t\t{coupon}"
                + f"\nSign:\n{signature}"
                + f"\nLevel:\t\t\t\t{lv}"
                + f"\nCurrent EXP:\t\t\t\t{exp}"
                + f"\nBirthday:\t\t\t\t{birthday}"
                + f"\nAvatar frame:\t\t\t\t{pendn}"
                + f"\nNameplate:\t\t\t\t{npn}"
                + f"\nPhone verification status:\t\t\t\t{mobile}"
                + f"\nEmail verification status:\t\t\t\t{email}"
                + f"\nSenior member:\t\t\t\t{seniormember}"
                + f"\nJury member:\t\t\t\t{jury}"
                + f"\nMoral value:\t\t\t\t{moral}"
                + f"\nBilibili space link:\t\t\t\thttps://space.bilibili.com/{user_id}",
            )
        elif lang == 8:
            output_text.insert(
                INSERT,
                f"Nickname:\t\t\t\t{uname}"
                + f"\nUID:\t\t\t\t{user_id}"
                + f"\nGender:\t\t\t\t{sex}"
                + f"\nBig Member status:\t\t\t\t{vip_status}"
                + f"\nBig Member expiration date:\t\t\t\t{viptime}"
                + f"\nTime of joining Bilibili:\t\t\t\t{jointime}"
                + f"\nCertification status:\t\t\t\t{verification_status}"
                + f"\nAccount Status:\t\t\t\t{account_status}"
                + f"\nFans count:\t\t\t\t{fans}"
                + f"\nFollow count:\t\t\t\t{follow}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nB Coin count:\t\t\t\t{bcoin}"
                + f"\nB Coin coupons:\t\t\t\t{coupon}"
                + f"\nSign:\n{signature}"
                + f"\nLevel:\t\t\t\t{lv}"
                + f"\nCurrent EXP:\t\t\t\t{exp}"
                + f"\nBirthday:\t\t\t\t{birthday}"
                + f"\nAvatar frame:\t\t\t\t{pendn}"
                + f"\nNameplate:\t\t\t\t{npn}"
                + f"\nPhone verification status:\t\t\t\t{mobile}"
                + f"\nEmail verification status:\t\t\t\t{email}"
                + f"\nSenior member:\t\t\t\t{seniormember}"
                + f"\nJury member:\t\t\t\t{jury}"
                + f"\nMoral value:\t\t\t\t{moral}"
                + f"\nBilibili space link:\t\t\t\thttps://space.bilibili.com/{user_id}",
            )
        elif lang == 9:
            output_text.insert(
                INSERT,
                f"Nickname:\t\t\t\t{uname}"
                + f"\nUID:\t\t\t\t{user_id}"
                + f"\nGender:\t\t\t\t{sex}"
                + f"\nBig Member status:\t\t\t\t{vip_status}"
                + f"\nBig Member expiration date:\t\t\t\t{viptime}"
                + f"\nTime of joining Bilibili:\t\t\t\t{jointime}"
                + f"\nCertification status:\t\t\t\t{verification_status}"
                + f"\nAccount Status:\t\t\t\t{account_status}"
                + f"\nFans count:\t\t\t\t{fans}"
                + f"\nFollow count:\t\t\t\t{follow}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nB Coin count:\t\t\t\t{bcoin}"
                + f"\nB Coin coupons:\t\t\t\t{coupon}"
                + f"\nSign:\n{signature}"
                + f"\nLevel:\t\t\t\t{lv}"
                + f"\nCurrent EXP:\t\t\t\t{exp}"
                + f"\nBirthday:\t\t\t\t{birthday}"
                + f"\nAvatar frame:\t\t\t\t{pendn}"
                + f"\nNameplate:\t\t\t\t{npn}"
                + f"\nPhone verification status:\t\t\t\t{mobile}"
                + f"\nEmail verification status:\t\t\t\t{email}"
                + f"\nSenior member:\t\t\t\t{seniormember}"
                + f"\nJury member:\t\t\t\t{jury}"
                + f"\nMoral value:\t\t\t\t{moral}"
                + f"\nBilibili space link:\t\t\t\thttps://space.bilibili.com/{user_id}",
            )
        elif lang == 10:
            output_text.insert(
                INSERT,
                f"Nickname:\t\t\t\t{uname}"
                + f"\nUID:\t\t\t\t{user_id}"
                + f"\nGender:\t\t\t\t{sex}"
                + f"\nBig Member status:\t\t\t\t{vip_status}"
                + f"\nBig Member expiration date:\t\t\t\t{viptime}"
                + f"\nTime of joining Bilibili:\t\t\t\t{jointime}"
                + f"\nCertification status:\t\t\t\t{verification_status}"
                + f"\nAccount Status:\t\t\t\t{account_status}"
                + f"\nFans count:\t\t\t\t{fans}"
                + f"\nFollow count:\t\t\t\t{follow}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nB Coin count:\t\t\t\t{bcoin}"
                + f"\nB Coin coupons:\t\t\t\t{coupon}"
                + f"\nSign:\n{signature}"
                + f"\nLevel:\t\t\t\t{lv}"
                + f"\nCurrent EXP:\t\t\t\t{exp}"
                + f"\nBirthday:\t\t\t\t{birthday}"
                + f"\nAvatar frame:\t\t\t\t{pendn}"
                + f"\nNameplate:\t\t\t\t{npn}"
                + f"\nPhone verification status:\t\t\t\t{mobile}"
                + f"\nEmail verification status:\t\t\t\t{email}"
                + f"\nSenior member:\t\t\t\t{seniormember}"
                + f"\nJury member:\t\t\t\t{jury}"
                + f"\nMoral value:\t\t\t\t{moral}"
                + f"\nBilibili space link:\t\t\t\thttps://space.bilibili.com/{user_id}",
            )
        elif lang == 11:
            output_text.insert(
                INSERT,
                f"Nickname:\t\t\t\t{uname}"
                + f"\nUID:\t\t\t\t{user_id}"
                + f"\nGender:\t\t\t\t{sex}"
                + f"\nBig Member status:\t\t\t\t{vip_status}"
                + f"\nBig Member expiration date:\t\t\t\t{viptime}"
                + f"\nTime of joining Bilibili:\t\t\t\t{jointime}"
                + f"\nCertification status:\t\t\t\t{verification_status}"
                + f"\nAccount Status:\t\t\t\t{account_status}"
                + f"\nFans count:\t\t\t\t{fans}"
                + f"\nFollow count:\t\t\t\t{follow}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nB Coin count:\t\t\t\t{bcoin}"
                + f"\nB Coin coupons:\t\t\t\t{coupon}"
                + f"\nSign:\n{signature}"
                + f"\nLevel:\t\t\t\t{lv}"
                + f"\nCurrent EXP:\t\t\t\t{exp}"
                + f"\nBirthday:\t\t\t\t{birthday}"
                + f"\nAvatar frame:\t\t\t\t{pendn}"
                + f"\nNameplate:\t\t\t\t{npn}"
                + f"\nPhone verification status:\t\t\t\t{mobile}"
                + f"\nEmail verification status:\t\t\t\t{email}"
                + f"\nSenior member:\t\t\t\t{seniormember}"
                + f"\nJury member:\t\t\t\t{jury}"
                + f"\nMoral value:\t\t\t\t{moral}"
                + f"\nBilibili space link:\t\t\t\thttps://space.bilibili.com/{user_id}",
            )
        elif lang == 12:
            output_text.insert(
                INSERT,
                f"Nickname:\t\t\t\t{uname}"
                + f"\nUID:\t\t\t\t{user_id}"
                + f"\nGender:\t\t\t\t{sex}"
                + f"\nBig Member status:\t\t\t\t{vip_status}"
                + f"\nBig Member expiration date:\t\t\t\t{viptime}"
                + f"\nTime of joining Bilibili:\t\t\t\t{jointime}"
                + f"\nCertification status:\t\t\t\t{verification_status}"
                + f"\nAccount Status:\t\t\t\t{account_status}"
                + f"\nFans count:\t\t\t\t{fans}"
                + f"\nFollow count:\t\t\t\t{follow}"
                + f"\nCoin count:\t\t\t\t{coin}"
                + f"\nB Coin count:\t\t\t\t{bcoin}"
                + f"\nB Coin coupons:\t\t\t\t{coupon}"
                + f"\nSign:\n{signature}"
                + f"\nLevel:\t\t\t\t{lv}"
                + f"\nCurrent EXP:\t\t\t\t{exp}"
                + f"\nBirthday:\t\t\t\t{birthday}"
                + f"\nAvatar frame:\t\t\t\t{pendn}"
                + f"\nNameplate:\t\t\t\t{npn}"
                + f"\nPhone verification status:\t\t\t\t{mobile}"
                + f"\nEmail verification status:\t\t\t\t{email}"
                + f"\nSenior member:\t\t\t\t{seniormember}"
                + f"\nJury member:\t\t\t\t{jury}"
                + f"\nMoral value:\t\t\t\t{moral}"
                + f"\nBilibili space link:\t\t\t\thttps://space.bilibili.com/{user_id}",
            )
        output_text.configure(state=DISABLED)


def logged_user_operations() -> None:
    sub_window = tkinter.Toplevel(loading_window)
    sub_window.title(window_title)
    sub_window.iconbitmap(icon_file)
    Label(sub_window, text=menu_items[lang]["luop"][0], font=(font_family, 14), fg="purple").pack()
    tool_labels = [
        (
            "查看是否有风纪委员会资格",
            "查询用户黑名单",
            "查看视频历史记录",
            "查看稍后再看列表",
            "查看UP主视频状态",
            "直播签到",
            "获取用户关注列表",
            "获取用户粉丝列表",
        ),
        (
            "Check if there is a qualification for the Jury Committee",
            "Query user blacklist",
            "View video history",
            "View the list of videos to watch",
            "View the video status of UP master",
            "Live check-in",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "查看是否有風紀委員會資格",
            "查詢用戶黑名單",
            "查看視頻歷史記錄",
            "查看稍後再看清單",
            "查看UP主的視頻狀態",
            "直播簽到",
            "獲取使用者關注列表",
            "獲取使用者粉絲列表",
        ),
        (
            "Check if there is a qualification for the Jury Committee",
            "Query user blacklist",
            "View video history",
            "View the list of videos to watch",
            "View the video status of UP master",
            "Live check-in",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Check if there is a qualification for the Jury Committee",
            "Query user blacklist",
            "View video history",
            "View the list of videos to watch",
            "View the video status of UP master",
            "Live check-in",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Check if there is a qualification for the Jury Committee",
            "Query user blacklist",
            "View video history",
            "View the list of videos to watch",
            "View the video status of UP master",
            "Live check-in",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Check if there is a qualification for the Jury Committee",
            "Query user blacklist",
            "View video history",
            "View the list of videos to watch",
            "View the video status of UP master",
            "Live check-in",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Check if there is a qualification for the Jury Committee",
            "Query user blacklist",
            "View video history",
            "View the list of videos to watch",
            "View the video status of UP master",
            "Live check-in",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Check if there is a qualification for the Jury Committee",
            "Query user blacklist",
            "View video history",
            "View the list of videos to watch",
            "View the video status of UP master",
            "Live check-in",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Check if there is a qualification for the Jury Committee",
            "Query user blacklist",
            "View video history",
            "View the list of videos to watch",
            "View the video status of UP master",
            "Live check-in",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Check if there is a qualification for the Jury Committee",
            "Query user blacklist",
            "View video history",
            "View the list of videos to watch",
            "View the video status of UP master",
            "Live check-in",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Check if there is a qualification for the Jury Committee",
            "Query user blacklist",
            "View video history",
            "View the list of videos to watch",
            "View the video status of UP master",
            "Live check-in",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Check if there is a qualification for the Jury Committee",
            "Query user blacklist",
            "View video history",
            "View the list of videos to watch",
            "View the video status of UP master",
            "Live check-in",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
    ]
    attb = [
        {0: "未关注", 2: "已关注", 6: "已互粉", 128: "已拉黑"},
        {
            0: "Not following",
            2: "Following",
            6: "Followed each other",
            128: "Blacklisted",
        },
        {0: "未關注", 2: "已關注", 6: "已互相關注", 128: "已拉入黑名單"},
        {
            0: "Not following",
            2: "Following",
            6: "Followed each other",
            128: "Blacklisted",
        },
        {
            0: "Not following",
            2: "Following",
            6: "Followed each other",
            128: "Blacklisted",
        },
        {
            0: "Not following",
            2: "Following",
            6: "Followed each other",
            128: "Blacklisted",
        },
        {
            0: "Not following",
            2: "Following",
            6: "Followed each other",
            128: "Blacklisted",
        },
        {
            0: "Not following",
            2: "Following",
            6: "Followed each other",
            128: "Blacklisted",
        },
        {
            0: "Not following",
            2: "Following",
            6: "Followed each other",
            128: "Blacklisted",
        },
        {
            0: "Not following",
            2: "Following",
            6: "Followed each other",
            128: "Blacklisted",
        },
        {
            0: "Not following",
            2: "Following",
            6: "Followed each other",
            128: "Blacklisted",
        },
        {
            0: "Not following",
            2: "Following",
            6: "Followed each other",
            128: "Blacklisted",
        },
        {
            0: "Not following",
            2: "Following",
            6: "Followed each other",
            128: "Blacklisted",
        },
    ]

    def juryqualify() -> None:
        page = request_api(
            "https://api.bilibili.com/x/credit/v2/jury/requirement?", headers=headers
        )
        response_data = read_api_response(page)
        status_code = api_code(response_data)
        if status_code != 0:
            msg = api_message(response_data) if lang == 0 else translated_api_message(status_code, api_message(response_data))
            warning_msg = [
                f"出现错误：{msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"發生錯誤：{msg}({status_code})",
                f"エラーが発生しました：{msg}({status_code})",
                f"Ein Fehler ist aufgetreten: {msg}({status_code})",
                f"Une erreur est survenue: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
            ]
            showwarning(title=window_title, message=warning_msg[lang])
            return None
        data = response_data["data"]
        blocked, cert, rule = data["blocked"], data["cert"], data["rule"]
        if not blocked and cert and rule:
            juryok = [
                "恭喜你有资格加入风纪委员会！",
                "Congratulations! You are eligible to join the Jury Committee!",
                "恭喜你有資格加入風紀委員會！",
                "風紀委員会に参加する資格があります。おめでとうございます！",
                "Herzlichen Glückwunsch! Sie sind berechtigt, dem Jurykomitee beizutreten!",
                "Félicitations ! Vous êtes éligible pour rejoindre le Comité de révision!",
                "Congratulations! You are eligible to join the Jury Committee!",
                "Congratulations! You are eligible to join the Jury Committee!",
                "Congratulations! You are eligible to join the Jury Committee!",
                "Congratulations! You are eligible to join the Jury Committee!",
                "Congratulations! You are eligible to join the Jury Committee!",
                "Congratulations! You are eligible to join the Jury Committee!",
                "Congratulations! You are eligible to join the Jury Committee!",
            ]
            showinfo(title=window_title, message=juryok[lang])
        else:
            juryfalse = [
                "你现在无法加入风纪委员会，原因如下：",
                "You are currently not eligible to join the Jury Committee for the following reasons:",
                "你現在無法加入風紀委員會，原因如下：",
                "現在、風紀委員会に参加できません。理由は次の通りです。",
                "Derzeit sind Sie aus folgenden Gründen nicht berechtigt, dem Jurykomitee beizutreten:",
                "Vous n'êtes actuellement pas admissible au Comité d'évaluation pour les raisons suivantes:",
                "You are currently not eligible to join the Jury Committee for the following reasons:",
                "You are currently not eligible to join the Jury Committee for the following reasons:",
                "You are currently not eligible to join the Jury Committee for the following reasons:",
                "You are currently not eligible to join the Jury Committee for the following reasons:",
                "You are currently not eligible to join the Jury Committee for the following reasons:",
                "You are currently not eligible to join the Jury Committee for the following reasons:",
                "You are currently not eligible to join the Jury Committee for the following reasons:",
            ]
            falsereas = [
                ("\n账号被封禁", "\n未实名认证", "\n90天内有违规记录"),
                (
                    "\nAccount is banned",
                    "\nNo real name authentication conducted",
                    "\nThere is a violation record within 90 days",
                ),
                ("\n帳號被封停", "\n未進行實名認證", "\n90天內存在違規記錄"),
                (
                    "\nアカウントが禁止されています",
                    "\n実名認証を行っていない",
                    "\n90日以内に違反記録があります",
                ),
                (
                    "\nKonto ist gesperrt",
                    "\nKeine Echtnamen-Authentifizierung durchgeführt",
                    "\nInnerhalb von 90 Tagen liegt ein Verstoß vor.",
                ),
                (
                    "\nLe compte est interdit",
                    "\nNon certifié par nom réel",
                    "\nViolation enregistrée dans les 90 jours",
                ),
                (
                    "\nAccount is banned",
                    "\nNo real name authentication conducted",
                    "\nThere is a violation record within 90 days",
                ),
                (
                    "\nAccount is banned",
                    "\nNo real name authentication conducted",
                    "\nThere is a violation record within 90 days",
                ),
                (
                    "\nAccount is banned",
                    "\nNo real name authentication conducted",
                    "\nThere is a violation record within 90 days",
                ),
                (
                    "\nAccount is banned",
                    "\nNo real name authentication conducted",
                    "\nThere is a violation record within 90 days",
                ),
                (
                    "\nAccount is banned",
                    "\nNo real name authentication conducted",
                    "\nThere is a violation record within 90 days",
                ),
                (
                    "\nAccount is banned",
                    "\nNo real name authentication conducted",
                    "\nThere is a violation record within 90 days",
                ),
                (
                    "\nAccount is banned",
                    "\nNo real name authentication conducted",
                    "\nThere is a violation record within 90 days",
                ),
            ]
            jf = juryfalse[lang]
            if blocked:
                jf += falsereas[lang][0]
            if not cert:
                jf += falsereas[lang][1]
            if not rule:
                jf += falsereas[lang][2]
            showerror(title=window_title, message=jf)

    def blacklist() -> None:
        page = request_api(
            "https://api.bilibili.com/x/relation/blacks?", headers=headers
        )
        response_data = read_api_response(page)
        status_code = api_code(response_data)
        if status_code != 0:
            msg = api_message(response_data) if lang == 0 else translated_api_message(status_code, api_message(response_data))
            warning_msg = [
                f"出现错误：{msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"出现错误：{msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
            ]
            showwarning(title=window_title, message=warning_msg[lang])
            return None
        data = response_data["data"]
        ls = data["list"]
        outpt()
        for i in ls:
            vtp = [
                ("无", "大会员", "年度及以上大会员"),
                ("No", "Big member", "Annual big member or greater"),
                ("無", "大會員", "年度及以上大會員"),
                ("No", "Big member", "Annual big member or greater"),
                ("No", "Big member", "Annual big member or greater"),
                ("No", "Big member", "Annual big member or greater"),
                ("No", "Big member", "Annual big member or greater"),
                ("No", "Big member", "Annual big member or greater"),
                ("No", "Big member", "Annual big member or greater"),
                ("No", "Big member", "Annual big member or greater"),
                ("No", "Big member", "Annual big member or greater"),
                ("No", "Big member", "Annual big member or greater"),
                ("No", "Big member", "Annual big member or greater"),
            ]
            user_id = i["mid"]
            attribute = attb[lang][i["attribute"]]
            mt = i["mtime"]
            if lang == 0 or lang == 2 or lang == 3 or lang == 7:
                mtm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mt))
            elif lang == 1 or lang == 9:
                mtm = time.strftime("%m-%d-%Y %H:%M:%S", time.localtime(mt))
            elif lang == 4 or lang == 5 or lang == 6 or lang == 8:
                mtm = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(mt))
            nickname = i["uname"]
            signature = i["signature"]
            viptype = vtp[lang][i["vip"]["vipType"]]
            output_text.insert(
                INSERT,
                f"昵称：\t\t{nickname}"
                + f"\nUID：\t\t{user_id}"
                + f"\n关系状态：\t\t{attribute}"
                + f"\n拉黑时间：\t\t{mtm}"
                + f"\n大会员状态：\t\t{viptype}"
                + f"\n用户签名：\n{signature}",
            )
            output_text.insert(INSERT, "\n——————————————————————————————————————————————————\n")
        output_text.configure(state=DISABLED)

    def history() -> None:
        page = request_api(
            "https://api.bilibili.com/x/web-interface/history/cursor?ps=30&type=archive",
            headers=headers,
        )
        response_data = read_api_response(page)
        status_code = api_code(response_data)
        if status_code != 0:
            msg = api_message(response_data) if lang == 0 else translated_api_message(status_code, api_message(response_data))
            warning_msg = [
                f"出现错误：{msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
            ]
            showwarning(title=window_title, message=warning_msg[lang])
            return None
        data = response_data["data"]
        ls = data["list"]
        outpt()
        platform = [
            {
                0: "其他",
                1: "手机端",
                3: "手机端",
                5: "手机端",
                7: "手机端",
                2: "web端",
                4: "pad端",
                6: "pad端",
                33: "TV端",
            },
            {
                0: "Other",
                1: "Mobile",
                3: "Mobile",
                5: "Mobile",
                7: "Mobile",
                2: "Web",
                4: "Pad",
                6: "Pad",
                33: "TV",
            },
            {
                0: "其他",
                1: "手機端",
                3: "手機端",
                5: "手機端",
                7: "手機端",
                2: "web端",
                4: "pad端",
                6: "pad端",
                33: "TV端",
            },
            {
                0: "Other",
                1: "Mobile",
                3: "Mobile",
                5: "Mobile",
                7: "Mobile",
                2: "Web",
                4: "Pad",
                6: "Pad",
                33: "TV",
            },
            {
                0: "Other",
                1: "Mobile",
                3: "Mobile",
                5: "Mobile",
                7: "Mobile",
                2: "Web",
                4: "Pad",
                6: "Pad",
                33: "TV",
            },
            {
                0: "Other",
                1: "Mobile",
                3: "Mobile",
                5: "Mobile",
                7: "Mobile",
                2: "Web",
                4: "Pad",
                6: "Pad",
                33: "TV",
            },
            {
                0: "Other",
                1: "Mobile",
                3: "Mobile",
                5: "Mobile",
                7: "Mobile",
                2: "Web",
                4: "Pad",
                6: "Pad",
                33: "TV",
            },
            {
                0: "Other",
                1: "Mobile",
                3: "Mobile",
                5: "Mobile",
                7: "Mobile",
                2: "Web",
                4: "Pad",
                6: "Pad",
                33: "TV",
            },
            {
                0: "Other",
                1: "Mobile",
                3: "Mobile",
                5: "Mobile",
                7: "Mobile",
                2: "Web",
                4: "Pad",
                6: "Pad",
                33: "TV",
            },
            {
                0: "Other",
                1: "Mobile",
                3: "Mobile",
                5: "Mobile",
                7: "Mobile",
                2: "Web",
                4: "Pad",
                6: "Pad",
                33: "TV",
            },
            {
                0: "Other",
                1: "Mobile",
                3: "Mobile",
                5: "Mobile",
                7: "Mobile",
                2: "Web",
                4: "Pad",
                6: "Pad",
                33: "TV",
            },
            {
                0: "Other",
                1: "Mobile",
                3: "Mobile",
                5: "Mobile",
                7: "Mobile",
                2: "Web",
                4: "Pad",
                6: "Pad",
                33: "TV",
            },
            {
                0: "Other",
                1: "Mobile",
                3: "Mobile",
                5: "Mobile",
                7: "Mobile",
                2: "Web",
                4: "Pad",
                6: "Pad",
                33: "TV",
            },
        ]
        yn = [
            ("否", "是"),
            ("No", "Yes"),
            ("否", "是"),
            ("No", "Yes"),
            ("No", "Yes"),
            ("No", "Yes"),
            ("No", "Yes"),
            ("No", "Yes"),
            ("No", "Yes"),
            ("No", "Yes"),
            ("No", "Yes"),
            ("No", "Yes"),
            ("No", "Yes"),
        ]
        for i in ls:
            title = i["title"] if lang != 2 else to_traditional(i["title"])
            hsr = i["history"]
            aid = hsr["oid"]
            bvid = hsr["bvid"]
            pg = hsr["page"]
            cid = hsr["cid"]
            ptitle = hsr["part"]
            plf = platform[lang][hsr["dt"]]
            pgs = i["videos"]
            uname = i["author_name"]
            user_id = i["author_mid"]
            vtime = i["view_at"]
            if lang == 0 or lang == 2 or lang == 3 or lang == 7:
                vt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(vtime))
            elif lang == 1 or lang == 9:
                vt = time.strftime("%m-%d-%Y %H:%M:%S", time.localtime(vtime))
            elif lang == 4 or lang == 5 or lang == 6:
                vt = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(vtime))
            progress = i["progress"]
            prgs = "%02d:%02d" % divmod(progress, 60) if progress >= 0 else ""
            duration = i["duration"]
            dura = "%02d:%02d" % divmod(duration, 60)
            badge = i["badge"]
            tag = i["tag_name"]
            fav = yn[lang][i["is_fav"]]
            if lang == 0:
                output_text.insert(
                    INSERT,
                    f"视频标题：\t\t{title}"
                    + f"\n视频AV号：\t\tav{aid}"
                    + f"\n视频BV号：\t\t{bvid}"
                    + f"\n观看分P的CID：\t\t{cid}"
                    + f"\n观看视频分P：\t\t{pg}"
                    + f"\n视频分P标题：\t\t{ptitle}"
                    + f"\n观看平台：\t\t{plf}"
                    + f"\n视频分P总数：\t\t{pgs}"
                    + f"\n观看时间：\t\t{vt}"
                    + f"\n视频观看时长：\t\t{prgs}"
                    + f"\n视频总时长：\t\t{dura}"
                    + f"\n角标文字：\t\t{badge}"
                    + f"\n子分区名：\t\t{tag}"
                    + f"\n是否已收藏：\t\t{fav}"
                    + f"\nUP主昵称：\t\t{uname}"
                    + f"\nUP主UID：\t\t{user_id}"
                    + f"\n视频链接：\t\thttps://www.bilibili.com/video/av{aid}",
                )
            elif lang == 1:
                output_text.insert(
                    INSERT,
                    f"Video title:\t\t\t{title}"
                    + f"\nVideo AVID:\t\t\tav{aid}"
                    + f"\nVideo BVID:\t\t\t{bvid}"
                    + f"\nCID of current video:\t\t\t{cid}"
                    + f"\nCurrent part:\t\t\t{pg}"
                    + f"\nCurrent video title:\t\t\t{ptitle}"
                    + f"\nPlatform:\t\t\t{plf}"
                    + f"\nNumber of parts:\t\t\t{pgs}"
                    + f"\nTime of watching:\t\t\t{vt}"
                    + f"\nVideo viewing duration:\t\t\t{prgs}"
                    + f"\nTotal video duration:\t\t\t{dura}"
                    + f"\nBadge text:\t\t\t{badge}"
                    + f"\nSub partition name:\t\t\t{tag}"
                    + f"\nBookmarked:\t\t\t{fav}"
                    + f"\nUP master's nickname:\t\t\t{uname}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{aid}",
                )
            elif lang == 2:
                output_text.insert(
                    INSERT,
                    f"視頻標題：\t\t{to_traditional(title)}"
                    + f"\n視頻AV號：\t\tav{aid}"
                    + f"\n視頻BV號：\t\t{bvid}"
                    + f"\n觀看分P的CID：\t\t{cid}"
                    + f"\n觀看視頻分P：\t\t{pg}"
                    + f"\n視頻分P標題：\t\t{to_traditional(ptitle)}"
                    + f"\n觀看平臺：\t\t{plf}"
                    + f"\n視頻分P總數：\t\t{pgs}"
                    + f"\n觀看時間：\t\t{vt}"
                    + f"\n視頻觀看時長：\t\t{prgs}"
                    + f"\n視頻總時長：\t\t{dura}"
                    + f"\n角標文字：\t\t{to_traditional(badge)}"
                    + f"\n子分區名：\t\t{to_traditional(tag)}"
                    + f"\n是否已收藏：\t\t{fav}"
                    + f"\nUP主暱稱：\t\t{uname}"
                    + f"\nUP主UID：\t\t{user_id}"
                    + f"\n視頻連結：\t\thttps://www.bilibili.com/video/av{aid}",
                )
            elif lang == 3:
                output_text.insert(
                    INSERT,
                    f"Video title:\t\t\t{title}"
                    + f"\nVideo AVID:\t\t\tav{aid}"
                    + f"\nVideo BVID:\t\t\t{bvid}"
                    + f"\nCID of current video:\t\t\t{cid}"
                    + f"\nCurrent part:\t\t\t{pg}"
                    + f"\nCurrent video title:\t\t\t{ptitle}"
                    + f"\nPlatform:\t\t\t{plf}"
                    + f"\nNumber of parts:\t\t\t{pgs}"
                    + f"\nTime of watching:\t\t\t{vt}"
                    + f"\nVideo viewing duration:\t\t\t{prgs}"
                    + f"\nTotal video duration:\t\t\t{dura}"
                    + f"\nBadge text:\t\t\t{badge}"
                    + f"\nSub partition name:\t\t\t{tag}"
                    + f"\nBookmarked:\t\t\t{fav}"
                    + f"\nUP master's nickname:\t\t\t{uname}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{aid}",
                )
            elif lang == 4:
                output_text.insert(
                    INSERT,
                    f"Video title:\t\t\t{title}"
                    + f"\nVideo AVID:\t\t\tav{aid}"
                    + f"\nVideo BVID:\t\t\t{bvid}"
                    + f"\nCID of current video:\t\t\t{cid}"
                    + f"\nCurrent part:\t\t\t{pg}"
                    + f"\nCurrent video title:\t\t\t{ptitle}"
                    + f"\nPlatform:\t\t\t{plf}"
                    + f"\nNumber of parts:\t\t\t{pgs}"
                    + f"\nTime of watching:\t\t\t{vt}"
                    + f"\nVideo viewing duration:\t\t\t{prgs}"
                    + f"\nTotal video duration:\t\t\t{dura}"
                    + f"\nBadge text:\t\t\t{badge}"
                    + f"\nSub partition name:\t\t\t{tag}"
                    + f"\nBookmarked:\t\t\t{fav}"
                    + f"\nUP master's nickname:\t\t\t{uname}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{aid}",
                )
            elif lang == 5:
                output_text.insert(
                    INSERT,
                    f"Video title:\t\t\t{title}"
                    + f"\nVideo AVID:\t\t\tav{aid}"
                    + f"\nVideo BVID:\t\t\t{bvid}"
                    + f"\nCID of current video:\t\t\t{cid}"
                    + f"\nCurrent part:\t\t\t{pg}"
                    + f"\nCurrent video title:\t\t\t{ptitle}"
                    + f"\nPlatform:\t\t\t{plf}"
                    + f"\nNumber of parts:\t\t\t{pgs}"
                    + f"\nTime of watching:\t\t\t{vt}"
                    + f"\nVideo viewing duration:\t\t\t{prgs}"
                    + f"\nTotal video duration:\t\t\t{dura}"
                    + f"\nBadge text:\t\t\t{badge}"
                    + f"\nSub partition name:\t\t\t{tag}"
                    + f"\nBookmarked:\t\t\t{fav}"
                    + f"\nUP master's nickname:\t\t\t{uname}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{aid}",
                )
            elif lang == 6:
                output_text.insert(
                    INSERT,
                    f"Video title:\t\t\t{title}"
                    + f"\nVideo AVID:\t\t\tav{aid}"
                    + f"\nVideo BVID:\t\t\t{bvid}"
                    + f"\nCID of current video:\t\t\t{cid}"
                    + f"\nCurrent part:\t\t\t{pg}"
                    + f"\nCurrent video title:\t\t\t{ptitle}"
                    + f"\nPlatform:\t\t\t{plf}"
                    + f"\nNumber of parts:\t\t\t{pgs}"
                    + f"\nTime of watching:\t\t\t{vt}"
                    + f"\nVideo viewing duration:\t\t\t{prgs}"
                    + f"\nTotal video duration:\t\t\t{dura}"
                    + f"\nBadge text:\t\t\t{badge}"
                    + f"\nSub partition name:\t\t\t{tag}"
                    + f"\nBookmarked:\t\t\t{fav}"
                    + f"\nUP master's nickname:\t\t\t{uname}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{aid}",
                )
            elif lang == 7:
                output_text.insert(
                    INSERT,
                    f"Video title:\t\t\t{title}"
                    + f"\nVideo AVID:\t\t\tav{aid}"
                    + f"\nVideo BVID:\t\t\t{bvid}"
                    + f"\nCID of current video:\t\t\t{cid}"
                    + f"\nCurrent part:\t\t\t{pg}"
                    + f"\nCurrent video title:\t\t\t{ptitle}"
                    + f"\nPlatform:\t\t\t{plf}"
                    + f"\nNumber of parts:\t\t\t{pgs}"
                    + f"\nTime of watching:\t\t\t{vt}"
                    + f"\nVideo viewing duration:\t\t\t{prgs}"
                    + f"\nTotal video duration:\t\t\t{dura}"
                    + f"\nBadge text:\t\t\t{badge}"
                    + f"\nSub partition name:\t\t\t{tag}"
                    + f"\nBookmarked:\t\t\t{fav}"
                    + f"\nUP master's nickname:\t\t\t{uname}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{aid}",
                )
            elif lang == 8:
                output_text.insert(
                    INSERT,
                    f"Video title:\t\t\t{title}"
                    + f"\nVideo AVID:\t\t\tav{aid}"
                    + f"\nVideo BVID:\t\t\t{bvid}"
                    + f"\nCID of current video:\t\t\t{cid}"
                    + f"\nCurrent part:\t\t\t{pg}"
                    + f"\nCurrent video title:\t\t\t{ptitle}"
                    + f"\nPlatform:\t\t\t{plf}"
                    + f"\nNumber of parts:\t\t\t{pgs}"
                    + f"\nTime of watching:\t\t\t{vt}"
                    + f"\nVideo viewing duration:\t\t\t{prgs}"
                    + f"\nTotal video duration:\t\t\t{dura}"
                    + f"\nBadge text:\t\t\t{badge}"
                    + f"\nSub partition name:\t\t\t{tag}"
                    + f"\nBookmarked:\t\t\t{fav}"
                    + f"\nUP master's nickname:\t\t\t{uname}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{aid}",
                )
            elif lang == 9:
                output_text.insert(
                    INSERT,
                    f"Video title:\t\t\t{title}"
                    + f"\nVideo AVID:\t\t\tav{aid}"
                    + f"\nVideo BVID:\t\t\t{bvid}"
                    + f"\nCID of current video:\t\t\t{cid}"
                    + f"\nCurrent part:\t\t\t{pg}"
                    + f"\nCurrent video title:\t\t\t{ptitle}"
                    + f"\nPlatform:\t\t\t{plf}"
                    + f"\nNumber of parts:\t\t\t{pgs}"
                    + f"\nTime of watching:\t\t\t{vt}"
                    + f"\nVideo viewing duration:\t\t\t{prgs}"
                    + f"\nTotal video duration:\t\t\t{dura}"
                    + f"\nBadge text:\t\t\t{badge}"
                    + f"\nSub partition name:\t\t\t{tag}"
                    + f"\nBookmarked:\t\t\t{fav}"
                    + f"\nUP master's nickname:\t\t\t{uname}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{aid}",
                )
            elif lang == 10:
                output_text.insert(
                    INSERT,
                    f"Video title:\t\t\t{title}"
                    + f"\nVideo AVID:\t\t\tav{aid}"
                    + f"\nVideo BVID:\t\t\t{bvid}"
                    + f"\nCID of current video:\t\t\t{cid}"
                    + f"\nCurrent part:\t\t\t{pg}"
                    + f"\nCurrent video title:\t\t\t{ptitle}"
                    + f"\nPlatform:\t\t\t{plf}"
                    + f"\nNumber of parts:\t\t\t{pgs}"
                    + f"\nTime of watching:\t\t\t{vt}"
                    + f"\nVideo viewing duration:\t\t\t{prgs}"
                    + f"\nTotal video duration:\t\t\t{dura}"
                    + f"\nBadge text:\t\t\t{badge}"
                    + f"\nSub partition name:\t\t\t{tag}"
                    + f"\nBookmarked:\t\t\t{fav}"
                    + f"\nUP master's nickname:\t\t\t{uname}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{aid}",
                )
            elif lang == 11:
                output_text.insert(
                    INSERT,
                    f"Video title:\t\t\t{title}"
                    + f"\nVideo AVID:\t\t\tav{aid}"
                    + f"\nVideo BVID:\t\t\t{bvid}"
                    + f"\nCID of current video:\t\t\t{cid}"
                    + f"\nCurrent part:\t\t\t{pg}"
                    + f"\nCurrent video title:\t\t\t{ptitle}"
                    + f"\nPlatform:\t\t\t{plf}"
                    + f"\nNumber of parts:\t\t\t{pgs}"
                    + f"\nTime of watching:\t\t\t{vt}"
                    + f"\nVideo viewing duration:\t\t\t{prgs}"
                    + f"\nTotal video duration:\t\t\t{dura}"
                    + f"\nBadge text:\t\t\t{badge}"
                    + f"\nSub partition name:\t\t\t{tag}"
                    + f"\nBookmarked:\t\t\t{fav}"
                    + f"\nUP master's nickname:\t\t\t{uname}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{aid}",
                )
            elif lang == 12:
                output_text.insert(
                    INSERT,
                    f"Video title:\t\t\t{title}"
                    + f"\nVideo AVID:\t\t\tav{aid}"
                    + f"\nVideo BVID:\t\t\t{bvid}"
                    + f"\nCID of current video:\t\t\t{cid}"
                    + f"\nCurrent part:\t\t\t{pg}"
                    + f"\nCurrent video title:\t\t\t{ptitle}"
                    + f"\nPlatform:\t\t\t{plf}"
                    + f"\nNumber of parts:\t\t\t{pgs}"
                    + f"\nTime of watching:\t\t\t{vt}"
                    + f"\nVideo viewing duration:\t\t\t{prgs}"
                    + f"\nTotal video duration:\t\t\t{dura}"
                    + f"\nBadge text:\t\t\t{badge}"
                    + f"\nSub partition name:\t\t\t{tag}"
                    + f"\nBookmarked:\t\t\t{fav}"
                    + f"\nUP master's nickname:\t\t\t{uname}"
                    + f"\nUP master's UID:\t\t\t{user_id}"
                    + f"\nVideo link:\t\t\thttps://www.bilibili.com/video/av{aid}",
                )
            output_text.insert(INSERT, "\n——————————————————————————————————————————————————\n")
        output_text.configure(state=DISABLED)

    def upmaster() -> None:
        for t in range(1, MAX_RETRIES + 1):
            try:
                page = request_api(
                    "https://member.bilibili.com/x/web/index/stat?", headers=headers
                )
            except Exception as e:
                if t < MAX_RETRIES:
                    pass
                else:
                    error_text = str(e)
                    error_msgs = [
                        f"请求尝试{t}次后仍然发生错误：{error_text}",
                        f"The request still failed after {t} attempts: {error_text}",
                        f"請求嘗試{t}次後仍然發生錯誤：{error_text}",
                        f"要求を {t} 回試行した後もエラーが発生しました： {error_text}",
                        f"Nach {t} Versuchen an der Anforderung trat immer noch ein Fehler auf: {error_text}",
                        f"Une erreur se produisait encore après {t} tentatives de requête : {error_text}",
                        f"ข้อผิดพลาดยังคงเกิดขึ้นหลังจาก {t} ครั้งของความพยายามที่คําขอ: {error_text}",
                        f"요청을 {t}번 시도한 후에도 오류가 계속 발생했습니다: {error_text}",
                        f"Ошибка по-прежнему возникала после {t} попыток выполнения запроса: {error_text}",
                        f"Vẫn xảy ra lỗi sau {t} lần thử yêu cầu: {error_text}",
                        f"Ainda ocorreu um erro após {t} vezes de tentativas na solicitação: {error_text}",
                        f"Todavía se ha producido un error después de {t} veces de intentos en la solicitud: {error_text}",
                        f"Kesalahan masih terjadi setelah {t} kali upaya permintaan: {error_text}",
                    ]
                    showwarning(title=window_title, message=error_msgs[lang])
                    return None
            else:
                break
        response_data = read_api_response(page)
        status_code = api_code(response_data)
        if status_code != 0:
            msg = api_message(response_data) if lang == 0 else translated_api_message(status_code, api_message(response_data))
            warning_msg = [
                f"出现错误：{msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"發生錯誤：{msg}({status_code})",
                f"エラーが発生しました：{msg}({status_code})",
                f"Ein Fehler ist aufgetreten: {msg}({status_code})",
                f"Une erreur est survenue: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
            ]
            showwarning(title=window_title, message=warning_msg[lang])
            return None
        try:
            data = response_data["data"]
        except Exception:
            notupm = [
                "你不是UP主！",
                "You are not an UP master!",
                "你不是UP主！",
                "あなたはUPマスターではありません！",
                "You are not an UP master!",
                "You are not an UP master!",
                "You are not an UP master!",
                "You are not an UP master!",
                "You are not an UP master!",
                "You are not an UP master!",
                "You are not an UP master!",
                "You are not an UP master!",
                "You are not an UP master!",
            ]
            showwarning(title=window_title, message=notupm[lang])
            return None
        for t in range(1, MAX_RETRIES + 1):
            try:
                page2 = request_api(
                    "https://api.bilibili.com/studio/up-rating/v3/rating/info?",
                    headers=headers,
                )
            except Exception as e:
                if t < MAX_RETRIES:
                    pass
                else:
                    error_text = str(e)
                    error_msgs = [
                        f"请求尝试{t}次后仍然发生错误：{error_text}",
                        f"The request still failed after {t} attempts: {error_text}",
                        f"請求嘗試{t}次後仍然發生錯誤：{error_text}",
                        f"要求を {t} 回試行した後もエラーが発生しました： {error_text}",
                        f"Nach {t} Versuchen an der Anforderung trat immer noch ein Fehler auf: {error_text}",
                        f"Une erreur se produisait encore après {t} tentatives de requête : {error_text}",
                        f"ข้อผิดพลาดยังคงเกิดขึ้นหลังจาก {t} ครั้งของความพยายามที่คําขอ: {error_text}",
                        f"요청을 {t}번 시도한 후에도 오류가 계속 발생했습니다: {error_text}",
                        f"Ошибка по-прежнему возникала после {t} попыток выполнения запроса: {error_text}",
                        f"Vẫn xảy ra lỗi sau {t} lần thử yêu cầu: {error_text}",
                        f"Ainda ocorreu um erro após {t} vezes de tentativas na solicitação: {error_text}",
                        f"Todavía se ha producido un error después de {t} veces de intentos en la solicitud: {error_text}",
                        f"Kesalahan masih terjadi setelah {t} kali upaya permintaan: {error_text}",
                    ]
                    showwarning(title=window_title, message=error_msgs[lang])
                    return None
            else:
                break
        soup2 = require_api_success(read_api_response(page2))
        data2 = soup2["data"]
        user_id = data2["mid"]
        lv = data2["level"]
        score = data2["score"]
        credit = data2["credit"]
        upd = data2.get("update_date")
        upddate = time_convert(upd) if isinstance(upd, (int, float)) and upd > 0 else "—"
        outpt(24)
        if lang == 0:
            output_text.insert(
                INSERT,
                f"用户UID：\t\t{user_id}"
                + f"\n电磁力等级：\t\t{lv}"
                + f"\n电磁力分数：\t\t{score}"
                + f"\n信用分：\t\t{credit}"
                + f"\n电磁力更新时间：\t\t{upddate}"
                + f'\n新增投币：\t\t{data["inc_coin"]}'
                + f'\n新增充电：\t\t{data["inc_elec"]}'
                + f'\n新增收藏：\t\t{data["inc_fav"]}'
                + f'\n新增点赞：\t\t{data["inc_like"]}'
                + f'\n新增分享：\t\t{data["inc_share"]}'
                + f'\n新增播放：\t\t{data["incr_click"]}'
                + f'\n新增弹幕：\t\t{data["incr_dm"]}'
                + f'\n新增粉丝：\t\t{data["incr_fans"]}'
                + f'\n新增评论：\t\t{data["incr_reply"]}'
                + f'\n总计播放：\t\t{data["total_click"]}'
                + f'\n总计投币：\t\t{data["total_coin"]}'
                + f'\n总计弹幕：\t\t{data["total_dm"]}'
                + f'\n总计充电：\t\t{data["total_elec"]}'
                + f'\n总计粉丝：\t\t{data["total_fans"]}'
                + f'\n总计收藏：\t\t{data["total_fav"]}'
                + f'\n总计点赞：\t\t{data["total_like"]}'
                + f'\n总计评论：\t\t{data["total_reply"]}'
                + f'\n总计分享：\t\t{data["total_share"]}',
            )
        elif lang == 1:
            output_text.insert(
                INSERT,
                f"用户UID：\t\t{user_id}"
                + f"\n电磁力等级：\t\t{lv}"
                + f"\n电磁力分数：\t\t{score}"
                + f"\n信用分：\t\t{credit}"
                + f"\n电磁力更新时间：\t\t{upddate}"
                + f'\n新增投币：\t\t{data["inc_coin"]}'
                + f'\n新增充电：\t\t{data["inc_elec"]}'
                + f'\n新增收藏：\t\t{data["inc_fav"]}'
                + f'\n新增点赞：\t\t{data["inc_like"]}'
                + f'\n新增分享：\t\t{data["inc_share"]}'
                + f'\n新增播放：\t\t{data["incr_click"]}'
                + f'\n新增弹幕：\t\t{data["incr_dm"]}'
                + f'\n新增粉丝：\t\t{data["incr_fans"]}'
                + f'\n新增评论：\t\t{data["incr_reply"]}'
                + f'\n总计播放：\t\t{data["total_click"]}'
                + f'\n总计投币：\t\t{data["total_coin"]}'
                + f'\n总计弹幕：\t\t{data["total_dm"]}'
                + f'\n总计充电：\t\t{data["total_elec"]}'
                + f'\n总计粉丝：\t\t{data["total_fans"]}'
                + f'\n总计收藏：\t\t{data["total_fav"]}'
                + f'\n总计点赞：\t\t{data["total_like"]}'
                + f'\n总计评论：\t\t{data["total_reply"]}'
                + f'\n总计分享：\t\t{data["total_share"]}',
            )
        elif lang == 2:
            output_text.insert(
                INSERT,
                f"使用者UID：\t\t{user_id}"
                + f"\n電磁力等級：\t\t{lv}"
                + f"\n電磁力分數：\t\t{score}"
                + f"\n信用分：\t\t{credit}"
                + f"\n電磁力更新時間：\t\t{upddate}"
                + f'\n新增投幣：\t\t{data["inc_coin"]}'
                + f'\n新增充電：\t\t{data["inc_elec"]}'
                + f'\n新增收藏：\t\t{data["inc_fav"]}'
                + f'\n新增點贊：\t\t{data["inc_like"]}'
                + f'\n新增分享：\t\t{data["inc_share"]}'
                + f'\n新增播放：\t\t{data["incr_click"]}'
                + f'\n新增彈幕：\t\t{data["incr_dm"]}'
                + f'\n新增粉絲：\t\t{data["incr_fans"]}'
                + f'\n新增評論：\t\t{data["incr_reply"]}'
                + f'\n總計播放：\t\t{data["total_click"]}'
                + f'\n總計投幣：\t\t{data["total_coin"]}'
                + f'\n總計彈幕：\t\t{data["total_dm"]}'
                + f'\n總計充電：\t\t{data["total_elec"]}'
                + f'\n總計粉絲：\t\t{data["total_fans"]}'
                + f'\n總計收藏：\t\t{data["total_fav"]}'
                + f'\n總計點贊：\t\t{data["total_like"]}'
                + f'\n總計評論：\t\t{data["total_reply"]}'
                + f'\n總計分享：\t\t{data["total_share"]}',
            )
        output_text.config(state=DISABLED)

    def signin() -> None:
        page = request_api(
            "https://api.live.bilibili.com/xlive/web-ucenter/v1/sign/DoSign?",
            headers=headers,
        )
        response_data = read_api_response(page)
        status_code = api_code(response_data)
        if status_code != 0:
            msg = api_message(response_data) if lang == 0 else translated_api_message(status_code, api_message(response_data))
            warning_msg = [
                f"出现错误：{msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"發生錯誤：{msg}({status_code})",
                f"エラーが発生しました：{msg}({status_code})",
                f"Ein Fehler ist aufgetreten: {msg}({status_code})",
                f"Une erreur est survenue: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
            ]
            showwarning(title=window_title, message=warning_msg[lang])
            return
        data = response_data["data"]
        success = [
            f'签到成功！\n获得 {data["text"]}\n{data["specialText"]}\n本月共 {data["allDays"]} 天\n本月已签到 {data["hadSignDays"]} 天',
            f'Sign in successful! \nYou have obtained {data["text"]}\n{data["specialText"]}\nDays this month: {data["allDays"]}\nDays signed in this month: {data["hadSignDays"]}',
            f'簽到成功！\n獲得 {to_traditional(data["text"])}\n{to_traditional(data["specialText"])}\n本月共 {data["allDays"]} 天\n本月已簽到 {data["hadSignDays"]} 天',
            f'Sign in successful! \nYou have obtained {data["text"]}\n{data["specialText"]}\nDays this month: {data["allDays"]}\nDays signed in this month: {data["hadSignDays"]}',
            f'Sign in successful! \nYou have obtained {data["text"]}\n{data["specialText"]}\nDays this month: {data["allDays"]}\nDays signed in this month: {data["hadSignDays"]}',
            f'Sign in successful! \nYou have obtained {data["text"]}\n{data["specialText"]}\nDays this month: {data["allDays"]}\nDays signed in this month: {data["hadSignDays"]}',
            f'Sign in successful! \nYou have obtained {data["text"]}\n{data["specialText"]}\nDays this month: {data["allDays"]}\nDays signed in this month: {data["hadSignDays"]}',
            f'Sign in successful! \nYou have obtained {data["text"]}\n{data["specialText"]}\nDays this month: {data["allDays"]}\nDays signed in this month: {data["hadSignDays"]}',
            f'Sign in successful! \nYou have obtained {data["text"]}\n{data["specialText"]}\nDays this month: {data["allDays"]}\nDays signed in this month: {data["hadSignDays"]}',
            f'Sign in successful! \nYou have obtained {data["text"]}\n{data["specialText"]}\nDays this month: {data["allDays"]}\nDays signed in this month: {data["hadSignDays"]}',
            f'Sign in successful! \nYou have obtained {data["text"]}\n{data["specialText"]}\nDays this month: {data["allDays"]}\nDays signed in this month: {data["hadSignDays"]}',
            f'Sign in successful! \nYou have obtained {data["text"]}\n{data["specialText"]}\nDays this month: {data["allDays"]}\nDays signed in this month: {data["hadSignDays"]}',
            f'Sign in successful! \nYou have obtained {data["text"]}\n{data["specialText"]}\nDays this month: {data["allDays"]}\nDays signed in this month: {data["hadSignDays"]}',
        ]
        showinfo(title=window_title, message=success[lang])

    def follow(types="followings") -> None:
        vmid = askinteger(title=window_title, prompt="输入B站用户UID...")
        if vmid == None:
            return None
        pn = askinteger(title=window_title, prompt="输入查询页码（每页50个，默认为第一页）...")
        url = f"https://api.bilibili.com/x/relation/{types}?vmid={vmid}&pn={pn if pn!=None else 1}"
        for t in range(1, MAX_RETRIES + 1):
            try:
                page = request_api(url, headers=headers)
            except Exception as e:
                if t < MAX_RETRIES:
                    pass
                else:
                    error_text = str(e)
                    error_msgs = [
                        f"请求尝试{t}次后仍然发生错误：{error_text}",
                        f"The request still failed after {t} attempts: {error_text}",
                        f"請求嘗試{t}次後仍然發生錯誤：{error_text}",
                        f"要求を {t} 回試行した後もエラーが発生しました： {error_text}",
                        f"Nach {t} Versuchen an der Anforderung trat immer noch ein Fehler auf: {error_text}",
                        f"Une erreur se produisait encore après {t} tentatives de requête : {error_text}",
                        f"ข้อผิดพลาดยังคงเกิดขึ้นหลังจาก {t} ครั้งของความพยายามที่คําขอ: {error_text}",
                        f"요청을 {t}번 시도한 후에도 오류가 계속 발생했습니다: {error_text}",
                        f"Ошибка по-прежнему возникала после {t} попыток выполнения запроса: {error_text}",
                        f"Vẫn xảy ra lỗi sau {t} lần thử yêu cầu: {error_text}",
                        f"Ainda ocorreu um erro após {t} vezes de tentativas na solicitação: {error_text}",
                        f"Todavía se ha producido un error después de {t} veces de intentos en la solicitud: {error_text}",
                        f"Kesalahan masih terjadi setelah {t} kali upaya permintaan: {error_text}",
                    ]
                    showwarning(title=window_title, message=error_msgs[lang])
                    return None
            else:
                break
        response_data = read_api_response(page)
        status_code = api_code(response_data)
        msg = api_message(response_data)
        if status_code != 0:
            msg = msg if lang == 0 else translated_api_message(status_code, msg)
            warning_msg = [
                f"出现错误：{msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"發生錯誤：{msg}({status_code})",
                f"エラーが発生しました：{msg}({status_code})",
                f"Ein Fehler ist aufgetreten: {msg}({status_code})",
                f"Une erreur est survenue: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
            ]
            showwarning(title=window_title, message=warning_msg[lang])
            return None
        data = response_data["data"]
        ls = data["list"]
        if len(ls) == 0:
            showwarning(
                title=window_title,
                message="查询结果为空，可能查询超出了限定范围或没有那么多关注的用户。",
            )
            return None
        outpt()
        attempt_msg = [
            f"请求共尝试了{t}次。\n",
            f"The request was attempted {t} time(s).\n",
            f"請求共嘗試了{t}次。\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"Permintaan itu dicoba untuk {t} kali.\n",
        ]
        output_text.insert(INSERT, attempt_msg[lang])
        for i in ls:
            user_id = i["mid"]
            attribute = attb[lang][i["attribute"]]
            mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i["mtime"]))
            special = i["special"]
            uname = i["uname"]
            signature = i["signature"]
            official = i["official_verify"]
            offtype = official["type"]
            offdesc = official["desc"]
            vip = i["vip"]
            vtext = vip["Label"]["text"]
            offi = [
                {-1: "无", 0: "个人认证", 1: "机构认证"},
                {-1: "无", 0: "个人认证", 1: "机构认证"},
                {-1: "無", 0: "個人認證", 1: "機構認證"},
            ]
            if lang == 0:
                output_text.insert(
                    INSERT,
                    f"昵称：\t\t{uname}"
                    + f"\nUID：\t\t{user_id}"
                    + f"\n关系状态：\t\t{attribute}"
                    + f"\n关注时间：\t\t{mtime}"
                    + f'\n是否特别关注：\t\t{"是" if special else "否"}'
                    + f"\n用户签名：\n{signature}"
                    + f"\n认证状态：\t\t{offi[0][offtype]}：{offdesc}"
                    + f'\n大会员状态：\t\t{vtext if len(vtext)!=0 else "无"}'
                    + f"\n主页链接：\t\thttps://space.bilibili.com/{user_id}",
                )
            elif lang == 2:
                output_text.insert(
                    INSERT,
                    f"暱稱：\t\t{uname}"
                    + f"\nUID：\t\t{user_id}"
                    + f"\n關係狀態：\t\t{attribute}"
                    + f"\n關注時間：\t\t{mtime}"
                    + f'\n是否特別關注：\t\t{"是" if special else "否"}'
                    + f"\n使用者簽名：\n{to_traditional(signature)}"
                    + f"\n認證狀態：\t\t{offi[2][offtype]}：{to_traditional(offdesc)}"
                    + f'\n大會員狀態：\t\t{foreign.lang1[vtext][1] if len(vtext)!=0 else "無"}'
                    + f"\n主頁連結：\t\thttps://space.bilibili.com/{user_id}",
                )
            output_text.insert(INSERT, "\n————————————————————————————————————————————————————\n")
        output_text.config(state=DISABLED)

    fans = lambda: follow(types="followers")
    bl = [
        Button(sub_window, text=tool_labels[lang][0], command=juryqualify, font=default_font),
        Button(sub_window, text=tool_labels[lang][1], command=blacklist, font=default_font),
        Button(sub_window, text=tool_labels[lang][2], command=history, font=default_font),
        Button(sub_window, text=tool_labels[lang][3], command=1, font=default_font),
        Button(sub_window, text=tool_labels[lang][4], command=upmaster, font=default_font),
        Button(sub_window, text=tool_labels[lang][5], command=signin, font=default_font),
        Button(sub_window, text=tool_labels[lang][6], command=follow, font=default_font),
        Button(sub_window, text=tool_labels[lang][7], command=fans, font=default_font),
    ]
    for i in bl:
        i.pack()


def other_tools() -> None:  # 其他工具
    sub_window = tkinter.Toplevel(loading_window)
    sub_window.title(window_title)
    sub_window.iconbitmap(icon_file)
    Label(sub_window, text=menu_items[lang]["locate"][0], font=(font_family, 14), fg="purple").pack()
    tool_labels = [
        (
            "通过IP确定地理位置",
            "获取当前时间戳（离线）",
            "获取各分区当日投稿数",
            "获取热搜列表",
            "简繁转换器",
        ),
        (
            "Determine geographical location through IP",
            "Get the current timestamp (offline)",
            "Obtain the number of daily submissions from each partition",
            "Get the hot search list",
            "Simplified and Traditional Chinese Converter",
        ),
        (
            "通過IP確定地理位置",
            "取得當前時間戳（離線）",
            "獲取各分區當日投稿數",
            "獲取熱門搜尋列表",
            "簡繁中文轉換器",
        ),
        (
            "IPによる地理的位置の決定",
            "現在のタイムスタンプの取得（オフライン）",
            "パーティションごとの当日の投稿数を取得する",
            "ホット検索リストの取得",
            "簡体字・繁体字変換ツール",
        ),
        (
            "Determine geographical location through IP",
            "Get the current timestamp (offline)",
            "Obtain the number of daily submissions from each partition",
            "Get the hot search list",
            "Simplified and Traditional Chinese Converter",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Determine geographical location through IP",
            "Get the current timestamp (offline)",
            "Obtain the number of daily submissions from each partition",
            "Get the hot search list",
            "Simplified and Traditional Chinese Converter",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Determine geographical location through IP",
            "Get the current timestamp (offline)",
            "Obtain the number of daily submissions from each partition",
            "Get the hot search list",
            "Simplified and Traditional Chinese Converter",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Determine geographical location through IP",
            "Get the current timestamp (offline)",
            "Obtain the number of daily submissions from each partition",
            "Get the hot search list",
            "Simplified and Traditional Chinese Converter",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Determine geographical location through IP",
            "Get the current timestamp (offline)",
            "Obtain the number of daily submissions from each partition",
            "Get the hot search list",
            "Simplified and Traditional Chinese Converter",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Determine geographical location through IP",
            "Get the current timestamp (offline)",
            "Obtain the number of daily submissions from each partition",
            "Get the hot search list",
            "Simplified and Traditional Chinese Converter",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Determine geographical location through IP",
            "Get the current timestamp (offline)",
            "Obtain the number of daily submissions from each partition",
            "Get the hot search list",
            "Simplified and Traditional Chinese Converter",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Determine geographical location through IP",
            "Get the current timestamp (offline)",
            "Obtain the number of daily submissions from each partition",
            "Get the hot search list",
            "Simplified and Traditional Chinese Converter",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
        (
            "Determine geographical location through IP",
            "Get the current timestamp (offline)",
            "Obtain the number of daily submissions from each partition",
            "Get the hot search list",
            "Simplified and Traditional Chinese Converter",
            "Get the follow list of a user",
            "Get the fans list of a user",
        ),
    ]

    def locate() -> None:
        page = request_api(
            "https://api.bilibili.com/x/web-interface/zone?", headers=headers
        )
        response_data = read_api_response(page)
        status_code = api_code(response_data)
        if status_code != 0:
            msg = api_message(response_data) if lang == 0 else translated_api_message(status_code, api_message(response_data))
            warning_msg = [
                f"出现错误：{msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"出現錯誤：{msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
            ]
            showwarning(title=window_title, message=warning_msg[lang])
            return None
        data = response_data["data"]
        no_info_msg = [
            "无信息",
            "No information",
            "無信息",
            "No information",
            "No information",
            "No information",
            "No information",
            "No information",
            "No information",
            "No information",
            "No information",
            "No information",
            "No information",
        ]
        try:
            province = data["province"]
        except Exception:
            province = no_info_msg[lang]
        try:
            city = data["city"]
        except Exception:
            city = no_info_msg[lang]
        outsmall()
        if lang == 0:
            output_text.insert(
                INSERT,
                f'公网IP地址：\t\t{data["addr"]}'
                + f'\n国家/地区名：\t\t{data["country"]}'
                + f"\n省/州：\t\t{province}"
                + f"\n城市：\t\t{city}"
                + f'\n运营商名：\t\t{data["isp"]}'
                + f'\n纬度：\t\t{data["latitude"]}'
                + f'\n经度：\t\t{data["longitude"]}'
                + f'\n国家/地区代码：\t\t{data["country_code"]}',
            )
        elif lang == 2:
            output_text.insert(
                INSERT,
                f'公網IP地址：\t\t{data["addr"]}'
                + f'\n國家/地區名：\t\t{to_traditional(data["country"])}'
                + f"\n省/州：\t\t{to_traditional(province)}"
                + f"\n城市：\t\t{to_traditional(city)}"
                + f'\n運營商名：\t\t{to_traditional(data["isp"])}'
                + f'\n緯度：\t\t{data["latitude"]}'
                + f'\n經度：\t\t{data["longitude"]}'
                + f'\n國家/地區程式碼：\t\t{data["country_code"]}',
            )
        output_text.configure(state=DISABLED)

    def timestamp() -> None:
        ts = time.time()
        outpt(2, 25)
        output_text.insert(INSERT, f"{ts}")
        output_text.configure(state=DISABLED)

    def statis() -> None:
        page = request_api(
            "https://api.bilibili.com/x/web-interface/online?", headers=headers
        )
        response_data = read_api_response(page)
        status_code = api_code(response_data)
        if status_code != 0:
            msg = api_message(response_data) if lang == 0 else translated_api_message(status_code, api_message(response_data))
            warning_msg = [
                f"出现错误：{msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"出现错误：{msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
            ]
            showwarning(title=window_title, message=warning_msg[lang])
            return None
        data = response_data["data"]["region_count"]
        outpt()
        if lang == 0:
            output_text.insert(
                INSERT,
                f'动画：\t\t{data["1"]}'
                + f'\n番剧：\t\t{data["13"]}'
                + f'\n国创：\t\t{data["167"]}'
                + f'\n音乐：\t\t{data["3"]}'
                + f'\n舞蹈：\t\t{data["129"]}'
                + f'\n游戏：\t\t{data["4"]}'
                + f'\n单机游戏：\t\t{data["17"]}'
                + f'\n知识：\t\t{data["36"]}'
                + f'\n数码：\t\t{data["188"]}'
                + f'\n生活：\t\t{data["160"]}'
                + f'\n搞笑：\t\t{data["138"]}'
                + f'\n美食圈：\t\t{data["76"]}'
                + f'\n动物圈：\t\t{data["75"]}'
                + f'\n鬼畜：\t\t{data["119"]}'
                + f'\n时尚：\t\t{data["155"]}'
                + f'\n资讯：\t\t{data["202"]}'
                + f'\n娱乐：\t\t{data["5"]}'
                + f'\n影视：\t\t{data["181"]}'
                + f'\n纪录片：\t\t{data["177"]}'
                + f'\n电影：\t\t{data["23"]}'
                + f'\n电视剧：\t\t{data["11"]}',
            )
        elif lang == 1:
            output_text.insert(
                INSERT,
                f'Animation(Douga):\t\t\t{data["1"]}'
                + f'\nBangumi(Anime):\t\t\t{data["13"]}'
                + f'\nChinese animation (Guochuang):\t\t\t{data["167"]}'
                + f'\nMusic:\t\t\t{data["3"]}'
                + f'\nDance:\t\t\t{data["129"]}'
                + f'\nGame:\t\t\t{data["4"]}'
                + f'\nStand-alone game:\t\t\t{data["17"]}'
                + f'\nKnowledge:\t\t\t{data["36"]}'
                + f'\nDigital:\t\t\t{data["188"]}'
                + f'\nLife:\t\t\t{data["160"]}'
                + f'\nFunny:\t\t\t{data["138"]}'
                + f'\nFood:\t\t\t{data["76"]}'
                + f'\nAnimal:\t\t\t{data["75"]}'
                + f'\nKichiku:\t\t\t{data["119"]}'
                + f'\nFashion:\t\t\t{data["155"]}'
                + f'\nInformation:\t\t\t{data["202"]}'
                + f'\nEntertainment:\t\t\t{data["5"]}'
                + f'\nFilm & TV:\t\t\t{data["181"]}'
                + f'\nDocumentary:\t\t\t{data["177"]}'
                + f'\nMovie:\t\t\t{data["23"]}'
                + f'\nTV play:\t\t\t{data["11"]}',
            )
        elif lang == 2:
            output_text.insert(
                INSERT,
                f'動畫：\t\t{data["1"]}'
                + f'\n番劇：\t\t{data["13"]}'
                + f'\n國創：\t\t{data["167"]}'
                + f'\n音樂：\t\t{data["3"]}'
                + f'\n舞蹈：\t\t{data["129"]}'
                + f'\n遊戲：\t\t{data["4"]}'
                + f'\n單機遊戲：\t\t{data["17"]}'
                + f'\n知識：\t\t{data["36"]}'
                + f'\n數位：\t\t{data["188"]}'
                + f'\n生活：\t\t{data["160"]}'
                + f'\n搞笑：\t\t{data["138"]}'
                + f'\n美食圈：\t\t{data["76"]}'
                + f'\n動物圈：\t\t{data["75"]}'
                + f'\n鬼畜：\t\t{data["119"]}'
                + f'\n時尚：\t\t{data["155"]}'
                + f'\n資訊：\t\t{data["202"]}'
                + f'\n娛樂：\t\t{data["5"]}'
                + f'\n影視：\t\t{data["181"]}'
                + f'\n紀錄片：\t\t{data["177"]}'
                + f'\n電影：\t\t{data["23"]}'
                + f'\n電視劇：\t\t{data["11"]}',
            )
        elif lang == 3:
            output_text.insert(
                INSERT,
                f'Animation(Douga):\t\t\t{data["1"]}'
                + f'\nBangumi(Anime):\t\t\t{data["13"]}'
                + f'\nChinese animation (Guochuang):\t\t\t{data["167"]}'
                + f'\nMusic:\t\t\t{data["3"]}'
                + f'\nDance:\t\t\t{data["129"]}'
                + f'\nGame:\t\t\t{data["4"]}'
                + f'\nStand-alone game:\t\t\t{data["17"]}'
                + f'\nKnowledge:\t\t\t{data["36"]}'
                + f'\nDigital:\t\t\t{data["188"]}'
                + f'\nLife:\t\t\t{data["160"]}'
                + f'\nFunny:\t\t\t{data["138"]}'
                + f'\nFood:\t\t\t{data["76"]}'
                + f'\nAnimal:\t\t\t{data["75"]}'
                + f'\nKichiku:\t\t\t{data["119"]}'
                + f'\nFashion:\t\t\t{data["155"]}'
                + f'\nInformation:\t\t\t{data["202"]}'
                + f'\nEntertainment:\t\t\t{data["5"]}'
                + f'\nFilm & TV:\t\t\t{data["181"]}'
                + f'\nDocumentary:\t\t\t{data["177"]}'
                + f'\nMovie:\t\t\t{data["23"]}'
                + f'\nTV play:\t\t\t{data["11"]}',
            )
        elif lang == 4:
            output_text.insert(
                INSERT,
                f'Animation(Douga):\t\t\t{data["1"]}'
                + f'\nBangumi(Anime):\t\t\t{data["13"]}'
                + f'\nChinese animation (Guochuang):\t\t\t{data["167"]}'
                + f'\nMusic:\t\t\t{data["3"]}'
                + f'\nDance:\t\t\t{data["129"]}'
                + f'\nGame:\t\t\t{data["4"]}'
                + f'\nStand-alone game:\t\t\t{data["17"]}'
                + f'\nKnowledge:\t\t\t{data["36"]}'
                + f'\nDigital:\t\t\t{data["188"]}'
                + f'\nLife:\t\t\t{data["160"]}'
                + f'\nFunny:\t\t\t{data["138"]}'
                + f'\nFood:\t\t\t{data["76"]}'
                + f'\nAnimal:\t\t\t{data["75"]}'
                + f'\nKichiku:\t\t\t{data["119"]}'
                + f'\nFashion:\t\t\t{data["155"]}'
                + f'\nInformation:\t\t\t{data["202"]}'
                + f'\nEntertainment:\t\t\t{data["5"]}'
                + f'\nFilm & TV:\t\t\t{data["181"]}'
                + f'\nDocumentary:\t\t\t{data["177"]}'
                + f'\nMovie:\t\t\t{data["23"]}'
                + f'\nTV play:\t\t\t{data["11"]}',
            )
        elif lang == 5:
            output_text.insert(
                INSERT,
                f'Animation(Douga):\t\t\t{data["1"]}'
                + f'\nBangumi(Anime):\t\t\t{data["13"]}'
                + f'\nChinese animation (Guochuang):\t\t\t{data["167"]}'
                + f'\nMusic:\t\t\t{data["3"]}'
                + f'\nDance:\t\t\t{data["129"]}'
                + f'\nGame:\t\t\t{data["4"]}'
                + f'\nStand-alone game:\t\t\t{data["17"]}'
                + f'\nKnowledge:\t\t\t{data["36"]}'
                + f'\nDigital:\t\t\t{data["188"]}'
                + f'\nLife:\t\t\t{data["160"]}'
                + f'\nFunny:\t\t\t{data["138"]}'
                + f'\nFood:\t\t\t{data["76"]}'
                + f'\nAnimal:\t\t\t{data["75"]}'
                + f'\nKichiku:\t\t\t{data["119"]}'
                + f'\nFashion:\t\t\t{data["155"]}'
                + f'\nInformation:\t\t\t{data["202"]}'
                + f'\nEntertainment:\t\t\t{data["5"]}'
                + f'\nFilm & TV:\t\t\t{data["181"]}'
                + f'\nDocumentary:\t\t\t{data["177"]}'
                + f'\nMovie:\t\t\t{data["23"]}'
                + f'\nTV play:\t\t\t{data["11"]}',
            )
        elif lang == 6:
            output_text.insert(
                INSERT,
                f'Animation(Douga):\t\t\t{data["1"]}'
                + f'\nBangumi(Anime):\t\t\t{data["13"]}'
                + f'\nChinese animation (Guochuang):\t\t\t{data["167"]}'
                + f'\nMusic:\t\t\t{data["3"]}'
                + f'\nDance:\t\t\t{data["129"]}'
                + f'\nGame:\t\t\t{data["4"]}'
                + f'\nStand-alone game:\t\t\t{data["17"]}'
                + f'\nKnowledge:\t\t\t{data["36"]}'
                + f'\nDigital:\t\t\t{data["188"]}'
                + f'\nLife:\t\t\t{data["160"]}'
                + f'\nFunny:\t\t\t{data["138"]}'
                + f'\nFood:\t\t\t{data["76"]}'
                + f'\nAnimal:\t\t\t{data["75"]}'
                + f'\nKichiku:\t\t\t{data["119"]}'
                + f'\nFashion:\t\t\t{data["155"]}'
                + f'\nInformation:\t\t\t{data["202"]}'
                + f'\nEntertainment:\t\t\t{data["5"]}'
                + f'\nFilm & TV:\t\t\t{data["181"]}'
                + f'\nDocumentary:\t\t\t{data["177"]}'
                + f'\nMovie:\t\t\t{data["23"]}'
                + f'\nTV play:\t\t\t{data["11"]}',
            )
        elif lang == 7:
            output_text.insert(
                INSERT,
                f'Animation(Douga):\t\t\t{data["1"]}'
                + f'\nBangumi(Anime):\t\t\t{data["13"]}'
                + f'\nChinese animation (Guochuang):\t\t\t{data["167"]}'
                + f'\nMusic:\t\t\t{data["3"]}'
                + f'\nDance:\t\t\t{data["129"]}'
                + f'\nGame:\t\t\t{data["4"]}'
                + f'\nStand-alone game:\t\t\t{data["17"]}'
                + f'\nKnowledge:\t\t\t{data["36"]}'
                + f'\nDigital:\t\t\t{data["188"]}'
                + f'\nLife:\t\t\t{data["160"]}'
                + f'\nFunny:\t\t\t{data["138"]}'
                + f'\nFood:\t\t\t{data["76"]}'
                + f'\nAnimal:\t\t\t{data["75"]}'
                + f'\nKichiku:\t\t\t{data["119"]}'
                + f'\nFashion:\t\t\t{data["155"]}'
                + f'\nInformation:\t\t\t{data["202"]}'
                + f'\nEntertainment:\t\t\t{data["5"]}'
                + f'\nFilm & TV:\t\t\t{data["181"]}'
                + f'\nDocumentary:\t\t\t{data["177"]}'
                + f'\nMovie:\t\t\t{data["23"]}'
                + f'\nTV play:\t\t\t{data["11"]}',
            )
        elif lang == 8:
            output_text.insert(
                INSERT,
                f'Animation(Douga):\t\t\t{data["1"]}'
                + f'\nBangumi(Anime):\t\t\t{data["13"]}'
                + f'\nChinese animation (Guochuang):\t\t\t{data["167"]}'
                + f'\nMusic:\t\t\t{data["3"]}'
                + f'\nDance:\t\t\t{data["129"]}'
                + f'\nGame:\t\t\t{data["4"]}'
                + f'\nStand-alone game:\t\t\t{data["17"]}'
                + f'\nKnowledge:\t\t\t{data["36"]}'
                + f'\nDigital:\t\t\t{data["188"]}'
                + f'\nLife:\t\t\t{data["160"]}'
                + f'\nFunny:\t\t\t{data["138"]}'
                + f'\nFood:\t\t\t{data["76"]}'
                + f'\nAnimal:\t\t\t{data["75"]}'
                + f'\nKichiku:\t\t\t{data["119"]}'
                + f'\nFashion:\t\t\t{data["155"]}'
                + f'\nInformation:\t\t\t{data["202"]}'
                + f'\nEntertainment:\t\t\t{data["5"]}'
                + f'\nFilm & TV:\t\t\t{data["181"]}'
                + f'\nDocumentary:\t\t\t{data["177"]}'
                + f'\nMovie:\t\t\t{data["23"]}'
                + f'\nTV play:\t\t\t{data["11"]}',
            )
        elif lang == 9:
            output_text.insert(
                INSERT,
                f'Animation(Douga):\t\t\t{data["1"]}'
                + f'\nBangumi(Anime):\t\t\t{data["13"]}'
                + f'\nChinese animation (Guochuang):\t\t\t{data["167"]}'
                + f'\nMusic:\t\t\t{data["3"]}'
                + f'\nDance:\t\t\t{data["129"]}'
                + f'\nGame:\t\t\t{data["4"]}'
                + f'\nStand-alone game:\t\t\t{data["17"]}'
                + f'\nKnowledge:\t\t\t{data["36"]}'
                + f'\nDigital:\t\t\t{data["188"]}'
                + f'\nLife:\t\t\t{data["160"]}'
                + f'\nFunny:\t\t\t{data["138"]}'
                + f'\nFood:\t\t\t{data["76"]}'
                + f'\nAnimal:\t\t\t{data["75"]}'
                + f'\nKichiku:\t\t\t{data["119"]}'
                + f'\nFashion:\t\t\t{data["155"]}'
                + f'\nInformation:\t\t\t{data["202"]}'
                + f'\nEntertainment:\t\t\t{data["5"]}'
                + f'\nFilm & TV:\t\t\t{data["181"]}'
                + f'\nDocumentary:\t\t\t{data["177"]}'
                + f'\nMovie:\t\t\t{data["23"]}'
                + f'\nTV play:\t\t\t{data["11"]}',
            )
        elif lang == 10:
            output_text.insert(
                INSERT,
                f'Animation(Douga):\t\t\t{data["1"]}'
                + f'\nBangumi(Anime):\t\t\t{data["13"]}'
                + f'\nChinese animation (Guochuang):\t\t\t{data["167"]}'
                + f'\nMusic:\t\t\t{data["3"]}'
                + f'\nDance:\t\t\t{data["129"]}'
                + f'\nGame:\t\t\t{data["4"]}'
                + f'\nStand-alone game:\t\t\t{data["17"]}'
                + f'\nKnowledge:\t\t\t{data["36"]}'
                + f'\nDigital:\t\t\t{data["188"]}'
                + f'\nLife:\t\t\t{data["160"]}'
                + f'\nFunny:\t\t\t{data["138"]}'
                + f'\nFood:\t\t\t{data["76"]}'
                + f'\nAnimal:\t\t\t{data["75"]}'
                + f'\nKichiku:\t\t\t{data["119"]}'
                + f'\nFashion:\t\t\t{data["155"]}'
                + f'\nInformation:\t\t\t{data["202"]}'
                + f'\nEntertainment:\t\t\t{data["5"]}'
                + f'\nFilm & TV:\t\t\t{data["181"]}'
                + f'\nDocumentary:\t\t\t{data["177"]}'
                + f'\nMovie:\t\t\t{data["23"]}'
                + f'\nTV play:\t\t\t{data["11"]}',
            )
        elif lang == 11:
            output_text.insert(
                INSERT,
                f'Animation(Douga):\t\t\t{data["1"]}'
                + f'\nBangumi(Anime):\t\t\t{data["13"]}'
                + f'\nChinese animation (Guochuang):\t\t\t{data["167"]}'
                + f'\nMusic:\t\t\t{data["3"]}'
                + f'\nDance:\t\t\t{data["129"]}'
                + f'\nGame:\t\t\t{data["4"]}'
                + f'\nStand-alone game:\t\t\t{data["17"]}'
                + f'\nKnowledge:\t\t\t{data["36"]}'
                + f'\nDigital:\t\t\t{data["188"]}'
                + f'\nLife:\t\t\t{data["160"]}'
                + f'\nFunny:\t\t\t{data["138"]}'
                + f'\nFood:\t\t\t{data["76"]}'
                + f'\nAnimal:\t\t\t{data["75"]}'
                + f'\nKichiku:\t\t\t{data["119"]}'
                + f'\nFashion:\t\t\t{data["155"]}'
                + f'\nInformation:\t\t\t{data["202"]}'
                + f'\nEntertainment:\t\t\t{data["5"]}'
                + f'\nFilm & TV:\t\t\t{data["181"]}'
                + f'\nDocumentary:\t\t\t{data["177"]}'
                + f'\nMovie:\t\t\t{data["23"]}'
                + f'\nTV play:\t\t\t{data["11"]}',
            )
        elif lang == 12:
            output_text.insert(
                INSERT,
                f'Animation(Douga):\t\t\t{data["1"]}'
                + f'\nBangumi(Anime):\t\t\t{data["13"]}'
                + f'\nChinese animation (Guochuang):\t\t\t{data["167"]}'
                + f'\nMusic:\t\t\t{data["3"]}'
                + f'\nDance:\t\t\t{data["129"]}'
                + f'\nGame:\t\t\t{data["4"]}'
                + f'\nStand-alone game:\t\t\t{data["17"]}'
                + f'\nKnowledge:\t\t\t{data["36"]}'
                + f'\nDigital:\t\t\t{data["188"]}'
                + f'\nLife:\t\t\t{data["160"]}'
                + f'\nFunny:\t\t\t{data["138"]}'
                + f'\nFood:\t\t\t{data["76"]}'
                + f'\nAnimal:\t\t\t{data["75"]}'
                + f'\nKichiku:\t\t\t{data["119"]}'
                + f'\nFashion:\t\t\t{data["155"]}'
                + f'\nInformation:\t\t\t{data["202"]}'
                + f'\nEntertainment:\t\t\t{data["5"]}'
                + f'\nFilm & TV:\t\t\t{data["181"]}'
                + f'\nDocumentary:\t\t\t{data["177"]}'
                + f'\nMovie:\t\t\t{data["23"]}'
                + f'\nTV play:\t\t\t{data["11"]}',
            )
        output_text.configure(state=DISABLED)

    def hot() -> None:
        for t in range(1, MAX_RETRIES + 1):
            try:
                page = request_api(
                    "https://s.search.bilibili.com/main/hotword?", headers=headers
                )
            except Exception as e:
                if t < MAX_RETRIES:
                    pass
                else:
                    error_text = str(e)
                    error_msgs = [
                        f"请求尝试{t}次后仍然发生错误：{error_text}",
                        f"The request still failed after {t} attempts: {error_text}",
                        f"請求嘗試{t}次後仍然發生錯誤：{error_text}",
                        f"要求を {t} 回試行した後もエラーが発生しました： {error_text}",
                        f"Nach {t} Versuchen an der Anforderung trat immer noch ein Fehler auf: {error_text}",
                        f"Une erreur se produisait encore après {t} tentatives de requête : {error_text}",
                        f"ข้อผิดพลาดยังคงเกิดขึ้นหลังจาก {t} ครั้งของความพยายามที่คําขอ: {error_text}",
                        f"요청을 {t}번 시도한 후에도 오류가 계속 발생했습니다: {error_text}",
                        f"Ошибка по-прежнему возникала после {t} попыток выполнения запроса: {error_text}",
                        f"Vẫn xảy ra lỗi sau {t} lần thử yêu cầu: {error_text}",
                        f"Ainda ocorreu um erro após {t} vezes de tentativas na solicitação: {error_text}",
                        f"Todavía se ha producido un error después de {t} veces de intentos en la solicitud: {error_text}",
                        f"Kesalahan masih terjadi setelah {t} kali upaya permintaan: {error_text}",
                    ]
                    showwarning(title=window_title, message=error_msgs[lang])
                    return None
            else:
                break
        response_data = read_api_response(page)
        status_code = api_code(response_data)
        if status_code != 0:
            msg = api_message(response_data) if lang == 0 else translated_api_message(status_code, api_message(response_data))
            warning_msg = [
                f"出现错误：{msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"出现错误：{msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
                f"An error has occurred: {msg}({status_code})",
            ]
            showwarning(title=window_title, message=warning_msg[lang])
            return None
        data = response_data["list"]
        outsmall()
        attempt_msg = [
            f"请求共尝试了{t}次。\n",
            f"The request was attempted {t} time(s).\n",
            f"請求共嘗試了{t}次。\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"The request was attempted {t} times.\n",
            f"Permintaan itu dicoba untuk {t} kali.\n",
        ]
        output_text.insert(INSERT, attempt_msg[lang])
        for i in data:
            rank = i["pos"]
            kw = i["keyword"]
            if lang == 0:
                output_text.insert(INSERT, f"第{rank}名：\t\t{kw}\n")
            elif lang == 2:
                output_text.insert(INSERT, f"第{rank}名：\t\t{to_traditional(kw)}\n")
            else:
                output_text.insert(INSERT, f"Rank {rank}: \t\t{kw}\n")
        output_text.configure(state=DISABLED)

    def converter() -> None:
        trans.main()
        converter_labels = [
            (
                "香港繁体→简体",
                "简体→香港繁体",
                "简体→繁体",
                "简体→台湾繁体",
                "简体→台湾繁体（含短语）",
                "繁体→香港繁体",
                "繁体→简体",
                "繁体→台湾繁体",
                "台湾繁体→简体",
                "台湾繁体→简体（含短语）",
            ),
            (
                "Traditional (Hong Kong) → Simplified",
                "Simplified → Traditional (Hong Kong)",
                "Simplified → Traditional",
                "Simplified → Traditional (Taiwan)",
                "Simplified → Traditional (Taiwan, Phrase)",
                "Traditional → Traditional (Hong Kong)",
                "Traditional → Simplified",
                "Traditional → Traditional (Taiwan)",
                "Traditional (Taiwan) → Simplified",
                "Traditional (Taiwan, Phrase) → Simplified",
            ),
            (
                "香港繁體→簡體",
                "簡體→香港繁體",
                "簡體→繁體",
                "簡體→臺灣繁體",
                "簡體→臺灣繁體（含短語）",
                "繁體→香港繁體",
                "繁體→簡體",
                "繁體→臺灣繁體",
                "臺灣繁體→簡體",
                "臺灣繁體→簡體（含短語）",
            ),
            (
                "Traditional (Hong Kong) → Simplified",
                "Simplified → Traditional (Hong Kong)",
                "Simplified → Traditional",
                "Simplified → Traditional (Taiwan)",
                "Simplified → Traditional (Taiwan, Phrase)",
                "Traditional → Traditional (Hong Kong)",
                "Traditional → Simplified",
                "Traditional → Traditional (Taiwan)",
                "Traditional (Taiwan) → Simplified",
                "Traditional (Taiwan, Phrase) → Simplified",
            ),
            (
                "Traditional (Hong Kong) → Simplified",
                "Simplified → Traditional (Hong Kong)",
                "Simplified → Traditional",
                "Simplified → Traditional (Taiwan)",
                "Simplified → Traditional (Taiwan, Phrase)",
                "Traditional → Traditional (Hong Kong)",
                "Traditional → Simplified",
                "Traditional → Traditional (Taiwan)",
                "Traditional (Taiwan) → Simplified",
                "Traditional (Taiwan, Phrase) → Simplified",
            ),
            (
                "Traditional (Hong Kong) → Simplified",
                "Simplified → Traditional (Hong Kong)",
                "Simplified → Traditional",
                "Simplified → Traditional (Taiwan)",
                "Simplified → Traditional (Taiwan, Phrase)",
                "Traditional → Traditional (Hong Kong)",
                "Traditional → Simplified",
                "Traditional → Traditional (Taiwan)",
                "Traditional (Taiwan) → Simplified",
                "Traditional (Taiwan, Phrase) → Simplified",
            ),
            (
                "Traditional (Hong Kong) → Simplified",
                "Simplified → Traditional (Hong Kong)",
                "Simplified → Traditional",
                "Simplified → Traditional (Taiwan)",
                "Simplified → Traditional (Taiwan, Phrase)",
                "Traditional → Traditional (Hong Kong)",
                "Traditional → Simplified",
                "Traditional → Traditional (Taiwan)",
                "Traditional (Taiwan) → Simplified",
                "Traditional (Taiwan, Phrase) → Simplified",
            ),
            (
                "Traditional (Hong Kong) → Simplified",
                "Simplified → Traditional (Hong Kong)",
                "Simplified → Traditional",
                "Simplified → Traditional (Taiwan)",
                "Simplified → Traditional (Taiwan, Phrase)",
                "Traditional → Traditional (Hong Kong)",
                "Traditional → Simplified",
                "Traditional → Traditional (Taiwan)",
                "Traditional (Taiwan) → Simplified",
                "Traditional (Taiwan, Phrase) → Simplified",
            ),
            (
                "Traditional (Hong Kong) → Simplified",
                "Simplified → Traditional (Hong Kong)",
                "Simplified → Traditional",
                "Simplified → Traditional (Taiwan)",
                "Simplified → Traditional (Taiwan, Phrase)",
                "Traditional → Traditional (Hong Kong)",
                "Traditional → Simplified",
                "Traditional → Traditional (Taiwan)",
                "Traditional (Taiwan) → Simplified",
                "Traditional (Taiwan, Phrase) → Simplified",
            ),
            (
                "Traditional (Hong Kong) → Simplified",
                "Simplified → Traditional (Hong Kong)",
                "Simplified → Traditional",
                "Simplified → Traditional (Taiwan)",
                "Simplified → Traditional (Taiwan, Phrase)",
                "Traditional → Traditional (Hong Kong)",
                "Traditional → Simplified",
                "Traditional → Traditional (Taiwan)",
                "Traditional (Taiwan) → Simplified",
                "Traditional (Taiwan, Phrase) → Simplified",
            ),
            (
                "Traditional (Hong Kong) → Simplified",
                "Simplified → Traditional (Hong Kong)",
                "Simplified → Traditional",
                "Simplified → Traditional (Taiwan)",
                "Simplified → Traditional (Taiwan, Phrase)",
                "Traditional → Traditional (Hong Kong)",
                "Traditional → Simplified",
                "Traditional → Traditional (Taiwan)",
                "Traditional (Taiwan) → Simplified",
                "Traditional (Taiwan, Phrase) → Simplified",
            ),
            (
                "Traditional (Hong Kong) → Simplified",
                "Simplified → Traditional (Hong Kong)",
                "Simplified → Traditional",
                "Simplified → Traditional (Taiwan)",
                "Simplified → Traditional (Taiwan, Phrase)",
                "Traditional → Traditional (Hong Kong)",
                "Traditional → Simplified",
                "Traditional → Traditional (Taiwan)",
                "Traditional (Taiwan) → Simplified",
                "Traditional (Taiwan, Phrase) → Simplified",
            ),
            (
                "Traditional (Hong Kong) → Simplified",
                "Simplified → Traditional (Hong Kong)",
                "Simplified → Traditional",
                "Simplified → Traditional (Taiwan)",
                "Simplified → Traditional (Taiwan, Phrase)",
                "Traditional → Traditional (Hong Kong)",
                "Traditional → Simplified",
                "Traditional → Traditional (Taiwan)",
                "Traditional (Taiwan) → Simplified",
                "Traditional (Taiwan, Phrase) → Simplified",
            ),
        ]
        count = 0
        trans.inp.config(font=default_font)
        trans.out.config(font=default_font)
        for i in trans.trans_buttons:
            i.config(text=converter_labels[lang][count], font=default_font)
            count += 1
        trans.window.title(window_title)
        trans.window.iconbitmap(icon_file)
        trans.window.mainloop()

    bl = [
        Button(sub_window, text=tool_labels[lang][0], command=locate, font=default_font),
        Button(sub_window, text=tool_labels[lang][1], command=timestamp, font=default_font),
        Button(sub_window, text=tool_labels[lang][2], command=statis, font=default_font),
        Button(sub_window, text=tool_labels[lang][3], command=hot, font=default_font),
        Button(sub_window, text=tool_labels[lang][4], command=converter, font=default_font),
    ]
    for i in bl:
        i.pack()


def login_qrcode() -> None:
    if requests_available:
        open_qr_login(loading_window, requests, rq.Session, headers,
                      current_menu["login"][0], lang, default_font, dpi_scale)


def login_cookies() -> None:
    if requests_available:
        prompt_cookie_login(loading_window, requests, rq.Session, headers, window_title, lang)


def check_integrity() -> None:
    check = tkinter.Toplevel(loading_window)
    check.title(window_title)
    check.iconbitmap(icon_file)
    check_labels = [
        {
            "rq": {True: "已安装", False: "未安装，程序无法正常运行！"},
            "pgl": {True: "存在", False: "不存在，繁体中文下无法无缝转换文本"},
            "ue": {True: "存在", False: "不存在，查询用户时无彩蛋。"},
            "init": {
                True: "存在且合法",
                False: "不存在或不合法，将使用系统默认语言。",
            },
            "log": {True: "存在", False: "不存在，程序内无法查看更新日志。"},
            "frn": {True: "存在", False: "不存在，程序无法正常运行！"},
            "avbv": {True: "存在", False: "不存在，无法使用av、bv转换功能。"},
        },
        {
            "rq": {
                True: "Installed",
                False: "Not installed, the program cannot run properly!",
            },
            "pgl": {
                True: "Installed",
                False: "Not existing, text cannot be seamlessly converted to traditional Chinese",
            },
            "ue": {True: "Exists", False: "Not existing"},
            "init": {
                True: "Exists and valid",
                False: "Missing or invalid; the system default language will be used.",
            },
            "log": {
                True: "Exists",
                False: "Not existing, unable to view update logs within the program.",
            },
            "frn": {
                True: "Exists",
                False: "Not existing, the program cannot run properly!",
            },
            "avbv": {
                True: "Exists",
                False: "Not existing. Cannot use the AV ID and BV ID conversion functions.",
            },
        },
        {
            "rq": {True: "已安裝", False: "未安裝，程式無法正常執行！"},
            "pgl": {True: "已安裝", False: "不存在，繁體中文下無法無縫轉換文字"},
            "ue": {True: "存在", False: "不存在，查詢使用者時無彩蛋。"},
            "init": {
                True: "存在且合法",
                False: "不存在或不合法，將使用系統預設語言。",
            },
            "log": {True: "存在", False: "不存在，程式內無法查看更新日誌。"},
            "frn": {True: "存在", False: "不存在，程式無法正常執行！"},
            "avbv": {True: "存在", False: "不存在，無法使用 av、bv 轉換功能。"},
        },
        {
            "rq": {
                True: "Installed",
                False: "Not installed, the program cannot run properly!",
            },
            "pgl": {
                True: "Installed",
                False: "Not existing, text cannot be seamlessly converted to traditional Chinese",
            },
            "ue": {True: "Exists", False: "Not existing"},
            "init": {
                True: "Exists and valid",
                False: "Missing or invalid; the system default language will be used.",
            },
            "log": {
                True: "Exists",
                False: "Not existing, unable to view update logs within the program.",
            },
            "frn": {
                True: "Exists",
                False: "Not existing, the program cannot run properly!",
            },
            "avbv": {
                True: "Exists",
                False: "Not existing. Cannot use the AV ID and BV ID conversion functions.",
            },
        },
        {
            "rq": {
                True: "Installed",
                False: "Not installed, the program cannot run properly!",
            },
            "pgl": {
                True: "Installed",
                False: "Not existing, text cannot be seamlessly converted to traditional Chinese",
            },
            "ue": {True: "Exists", False: "Not existing"},
            "init": {
                True: "Exists and valid",
                False: "Missing or invalid; the system default language will be used.",
            },
            "log": {
                True: "Exists",
                False: "Not existing, unable to view update logs within the program.",
            },
            "frn": {
                True: "Exists",
                False: "Not existing, the program cannot run properly!",
            },
            "avbv": {
                True: "Exists",
                False: "Not existing. Cannot use the AV ID and BV ID conversion functions.",
            },
        },
        {
            "rq": {
                True: "Installed",
                False: "Not installed, the program cannot run properly!",
            },
            "pgl": {
                True: "Installed",
                False: "Not existing, text cannot be seamlessly converted to traditional Chinese",
            },
            "ue": {True: "Exists", False: "Not existing"},
            "init": {
                True: "Exists and valid",
                False: "Missing or invalid; the system default language will be used.",
            },
            "log": {
                True: "Exists",
                False: "Not existing, unable to view update logs within the program.",
            },
            "frn": {
                True: "Exists",
                False: "Not existing, the program cannot run properly!",
            },
            "avbv": {
                True: "Exists",
                False: "Not existing. Cannot use the AV ID and BV ID conversion functions.",
            },
        },
        {
            "rq": {
                True: "Installed",
                False: "Not installed, the program cannot run properly!",
            },
            "pgl": {
                True: "Installed",
                False: "Not existing, text cannot be seamlessly converted to traditional Chinese",
            },
            "ue": {True: "Exists", False: "Not existing"},
            "init": {
                True: "Exists and valid",
                False: "Missing or invalid; the system default language will be used.",
            },
            "log": {
                True: "Exists",
                False: "Not existing, unable to view update logs within the program.",
            },
            "frn": {
                True: "Exists",
                False: "Not existing, the program cannot run properly!",
            },
            "avbv": {
                True: "Exists",
                False: "Not existing. Cannot use the AV ID and BV ID conversion functions.",
            },
        },
        {
            "rq": {
                True: "Installed",
                False: "Not installed, the program cannot run properly!",
            },
            "pgl": {
                True: "Installed",
                False: "Not existing, text cannot be seamlessly converted to traditional Chinese",
            },
            "ue": {True: "Exists", False: "Not existing"},
            "init": {
                True: "Exists and valid",
                False: "Missing or invalid; the system default language will be used.",
            },
            "log": {
                True: "Exists",
                False: "Not existing, unable to view update logs within the program.",
            },
            "frn": {
                True: "Exists",
                False: "Not existing, the program cannot run properly!",
            },
            "avbv": {
                True: "Exists",
                False: "Not existing. Cannot use the AV ID and BV ID conversion functions.",
            },
        },
        {
            "rq": {
                True: "Installed",
                False: "Not installed, the program cannot run properly!",
            },
            "pgl": {
                True: "Installed",
                False: "Not existing, text cannot be seamlessly converted to traditional Chinese",
            },
            "ue": {True: "Exists", False: "Not existing"},
            "init": {
                True: "Exists and valid",
                False: "Missing or invalid; the system default language will be used.",
            },
            "log": {
                True: "Exists",
                False: "Not existing, unable to view update logs within the program.",
            },
            "frn": {
                True: "Exists",
                False: "Not existing, the program cannot run properly!",
            },
            "avbv": {
                True: "Exists",
                False: "Not existing. Cannot use the AV ID and BV ID conversion functions.",
            },
        },
        {
            "rq": {
                True: "Installed",
                False: "Not installed, the program cannot run properly!",
            },
            "pgl": {
                True: "Installed",
                False: "Not existing, text cannot be seamlessly converted to traditional Chinese",
            },
            "ue": {True: "Exists", False: "Not existing"},
            "init": {
                True: "Exists and valid",
                False: "Missing or invalid; the system default language will be used.",
            },
            "log": {
                True: "Exists",
                False: "Not existing, unable to view update logs within the program.",
            },
            "frn": {
                True: "Exists",
                False: "Not existing, the program cannot run properly!",
            },
            "avbv": {
                True: "Exists",
                False: "Not existing. Cannot use the AV ID and BV ID conversion functions.",
            },
        },
        {
            "rq": {
                True: "Installed",
                False: "Not installed, the program cannot run properly!",
            },
            "pgl": {
                True: "Installed",
                False: "Not existing, text cannot be seamlessly converted to traditional Chinese",
            },
            "ue": {True: "Exists", False: "Not existing"},
            "init": {
                True: "Exists and valid",
                False: "Missing or invalid; the system default language will be used.",
            },
            "log": {
                True: "Exists",
                False: "Not existing, unable to view update logs within the program.",
            },
            "frn": {
                True: "Exists",
                False: "Not existing, the program cannot run properly!",
            },
            "avbv": {
                True: "Exists",
                False: "Not existing. Cannot use the AV ID and BV ID conversion functions.",
            },
        },
        {
            "rq": {
                True: "Installed",
                False: "Not installed, the program cannot run properly!",
            },
            "pgl": {
                True: "Installed",
                False: "Not existing, text cannot be seamlessly converted to traditional Chinese",
            },
            "ue": {True: "Exists", False: "Not existing"},
            "init": {
                True: "Exists and valid",
                False: "Missing or invalid; the system default language will be used.",
            },
            "log": {
                True: "Exists",
                False: "Not existing, unable to view update logs within the program.",
            },
            "frn": {
                True: "Exists",
                False: "Not existing, the program cannot run properly!",
            },
            "avbv": {
                True: "Exists",
                False: "Not existing. Cannot use the AV ID and BV ID conversion functions.",
            },
        },
        {
            "rq": {
                True: "Installed",
                False: "Not installed, the program cannot run properly!",
            },
            "pgl": {
                True: "Installed",
                False: "Not existing, text cannot be seamlessly converted to traditional Chinese",
            },
            "ue": {True: "Exists", False: "Not existing"},
            "init": {
                True: "Exists and valid",
                False: "Missing or invalid; the system default language will be used.",
            },
            "log": {
                True: "Exists",
                False: "Not existing, unable to view update logs within the program.",
            },
            "frn": {
                True: "Exists",
                False: "Not existing, the program cannot run properly!",
            },
            "avbv": {
                True: "Exists",
                False: "Not existing. Cannot use the AV ID and BV ID conversion functions.",
            },
        },
    ]
    title = [
        [
            "requests模块：\t",
            "OpenCC模块：\t",
            "UsersEgg.py：\t",
            "initialize.txt：\t",
            "lognew.py：\t",
            "foreign.py：\t",
            "avbv.py：\t",
        ],
        [
            "requests Module: \t",
            "OpenCC Module: \t",
            "UsersEgg.py: \t",
            "initialize.txt: \t",
            "lognew.py: \t",
            "foreign.py: \t",
            "avbv.py: \t",
        ],
        [
            "requests模块：\t",
            "OpenCC模块：\t",
            "UsersEgg.py：\t",
            "initialize.txt：\t",
            "lognew.py：\t",
            "foreign.py：\t",
            "avbv.py：\t",
        ],
        [
            "requests Module: \t",
            "OpenCC Module: \t",
            "UsersEgg.py: \t",
            "initialize.txt: \t",
            "lognew.py: \t",
            "foreign.py: \t",
            "avbv.py: \t",
        ],
        [
            "requests Module: \t",
            "OpenCC Module: \t",
            "UsersEgg.py: \t",
            "initialize.txt: \t",
            "lognew.py: \t",
            "foreign.py: \t",
            "avbv.py: \t",
        ],
        [
            "requests Module: \t",
            "OpenCC Module: \t",
            "UsersEgg.py: \t",
            "initialize.txt: \t",
            "lognew.py: \t",
            "foreign.py: \t",
            "avbv.py: \t",
        ],
        [
            "requests Module: \t",
            "OpenCC Module: \t",
            "UsersEgg.py: \t",
            "initialize.txt: \t",
            "lognew.py: \t",
            "foreign.py: \t",
            "avbv.py: \t",
        ],
        [
            "requests Module: \t",
            "OpenCC Module: \t",
            "UsersEgg.py: \t",
            "initialize.txt: \t",
            "lognew.py: \t",
            "foreign.py: \t",
            "avbv.py: \t",
        ],
        [
            "requests Module: \t",
            "OpenCC Module: \t",
            "UsersEgg.py: \t",
            "initialize.txt: \t",
            "lognew.py: \t",
            "foreign.py: \t",
            "avbv.py: \t",
        ],
        [
            "requests Module: \t",
            "OpenCC Module: \t",
            "UsersEgg.py: \t",
            "initialize.txt: \t",
            "lognew.py: \t",
            "foreign.py: \t",
            "avbv.py: \t",
        ],
        [
            "requests Module: \t",
            "OpenCC Module: \t",
            "UsersEgg.py: \t",
            "initialize.txt: \t",
            "lognew.py: \t",
            "foreign.py: \t",
            "avbv.py: \t",
        ],
        [
            "requests Module: \t",
            "OpenCC Module: \t",
            "UsersEgg.py: \t",
            "initialize.txt: \t",
            "lognew.py: \t",
            "foreign.py: \t",
            "avbv.py: \t",
        ],
        [
            "requests Module: \t",
            "OpenCC Module: \t",
            "UsersEgg.py: \t",
            "initialize.txt: \t",
            "lognew.py: \t",
            "foreign.py: \t",
            "avbv.py: \t",
        ],
    ]
    titll = [Label(check, text=q, font=(font_family, 12), fg="black") for q in title[lang]]
    row = 0
    for i in titll:
        i.grid(row=row, column=0)
        row += 1
    Label(
        check,
        text=check_labels[lang]["rq"][requests_available],
        font=(font_family, 12),
        fg="black" if requests_available else "red",
    ).grid(row=0, column=1)
    Label(
        check,
        text=check_labels[lang]["pgl"][bool(opencc_available)],
        font=(font_family, 12),
        fg="black" if opencc_available else "purple" if lang != 2 else "orange",
    ).grid(row=1, column=1)
    Label(
        check,
        text=check_labels[lang]["ue"][egg_available],
        font=(font_family, 12),
        fg="black" if egg_available else "purple",
    ).grid(row=2, column=1)
    Label(
        check,
        text=check_labels[lang]["init"][bool(init_file_exists)],
        font=(font_family, 12),
        fg="black" if init_file_exists else "purple",
    ).grid(row=3, column=1)
    Label(
        check,
        text=check_labels[lang]["log"][not bool(log_error)],
        font=(font_family, 12),
        fg="black" if not log_error else "purple",
    ).grid(row=4, column=1)
    Label(
        check,
        text=check_labels[lang]["frn"][foreign_available],
        font=(font_family, 12),
        fg="black" if foreign_available else "red",
    ).grid(row=5, column=1)
    Label(
        check,
        text=check_labels[lang]["avbv"][avbv_available],
        font=(font_family, 12),
        fg="black" if avbv_available else "orange",
    ).grid(row=6, column=1)


def about_program() -> None:  # 关于此程序
    outsmall()
    output_text.insert(INSERT, about_texts[lang])
    output_text.configure(state=DISABLED)


def view_changelog() -> None:  # 更新日志
    if log_error == 0:
        outpt()
        output_text.insert(INSERT, dll[lang])
        output_text.configure(state=DISABLED)
    else:
        showwarning(title=window_title, message=foreign.logmissing[lang])


def change_language() -> None:  # 更改语言
    global lang, button_map, current_menu, window_title, default_font, font_family
    bac = lang
    lang_selector_prompt = foreign.chooselang[lang] + LANG_DESCRIPTION
    lang = askinteger(title=window_title, prompt=lang_selector_prompt)
    if lang == None:
        lang = bac
        return None
    if not 0 <= lang < len(menu_items):
        lang = bac
    for i in k:
        current_menu = menu_items[lang]
        font_family = get_font_family(lang, font_variant)
        default_font = (font_family, 9)
        button_map[i].configure(text=current_menu[i][0], font=default_font)
        window_title = window_titles[lang]
    status_label.config(text=status_labels[lang] + version, font=(font_family, 14))
    loading_window.title(window_title)


def change_font() -> None:  # 更改字体
    global font_variant, default_font, window_title, font_family
    bac = font_variant
    font_variant = askinteger(title=window_title, prompt=foreign.choosefont[lang])
    if font_variant == None:
        font_variant = bac
        return None
    if font_variant in [i for i in range(4)]:
        pass
    elif font_variant == -1:
        fontset = askstring(title=window_title, prompt=foreign.setfont[lang])
        if fontset in [None,'']:
            return None
    else:
        showwarning(title=window_title, message=foreign.fontwarn[lang])
        font_variant = bac
    font_family = get_font_family(lang, font_variant) if font_variant >= 0 else fontset
    default_font = (font_family, 9)
    status_label.config(font=(font_family, 14))
    for i in k:
        default_font = (font_family, 9)
        button_map[i].configure(font=default_font)
        window_title = window_titles[lang]


def quit_program() -> None:  # 退出
    confirm_quit=askokcancel(title=window_title, message='是否退出？')
    if confirm_quit:
        showinfo(title=window_title, message=foreign.thank[lang])
        loading_window.destroy()
        sys.exit()
        quit()


u_year, u_month, u_day = 2026, 3, 14  # 更新日期
about_texts = [
    f"""程序开发：CQ-COMPLEX
开发者B站首页：https://space.bilibili.com/347752309
开发者QQ：2311804153
QQ交流群：240742269
程序版本：{version}
更新日期：{u_year}年{u_month}月{u_day}日
由于B站官方已要求 SocialSisterYi 将其 B 站 API 收集项目下架，本程序已基本失去继续开发的可能，目前仅做必要维护。
Gitee项目地址：https://gitee.com/cq-complex/TH-Bilibili-Toolbox
API 提供鸣谢：SocialSisterYi""",
    f"""Program Developing: CQ-COMPLEX
Developer's Bilibili home page: https://space.bilibili.com/347752309
Developer's QQ: 2311804153
Developer's QQ communicating group: 240742269
Program version: {version}
Update date: {u_month}/{u_day}/{u_year}
Since Bilibili has asked SocialSisterYi to take down the API collection project, this program can no longer be developed further and is now in maintenance-only mode.
Gitee project address: https://gitee.com/cq-complex/TH-Bilibili-Toolbox
At present, all languages except Chinese Simplified, English and Chinese Traditional rely on mechanical translation. If there is any error, welcome to correct it!
If some functions expire, please tell me in time so that I will try to get them fixed as soon as possible!
Acknowledgement of providing API: SocialSisterYi""",
    f"""程式開發：CQ-COMPLEX
開發者B站主頁：https://space.bilibili.com/347752309
開發者QQ：2311804153
QQ交流群：240742269
程式版本號：{version}
更新日期：{u_year}年{u_month}月{u_day}日
由於B站官方已要求 SocialSisterYi 將其 B 站 API 收集專案下架，本程式已基本失去繼續開發的可能，目前僅做必要維護。
Gitee專案地址：https://gitee.com/cq-complex/TH-Bilibili-Toolbox
目前除簡體中文、英語、繁體中文之外的語言全部使用機械翻譯，如有錯誤，歡迎指正！
若有部分功能失效，請及時聯絡開發者，將會盡快盡力修復！
API提供鳴謝：SocialSisterYi""",
    f"""プログラム開発: CQ-COMPLEX
開発者 Bilibiliホームページ: https://space.bilibili.com/347752309
開発者QQ:2311804153
QQコミュニケーショングループ:240742269
プログラムバージョン: {version}
更新日: {u_year}年{u_month}月{u_day}日
Bilibili の要請により SocialSisterYi の API 収集プロジェクトが公開停止となったため、本プログラムはこれ以上の開発が難しくなり、現在は保守のみ行っています。
Giteeプロジェクトアドレス：https://gitee.com/cq-complex/TH-Bilibili-Toolbox
現在、簡体字中国語、英語、繁体字中国語を除くすべての言語は機械翻訳に依存しています。
一部の機能が正常に動作しない場合は、早めにお知らせください。できるだけ早く修正いたします。
API提供の謝辞:SocialSisterYi""",
    f"""Programmentwicklung: CQ-COMPLEX
Homepage des Entwicklers Bilibili: https://space.bilibili.com/347752309
QQ des Entwicklers: 2311804153
QQ-Kommunikationsgruppe des Entwicklers: 240742269
Programmversion: {version}
Aktualisierungszeitpunkt: {u_day}/{u_month}/{u_year}
Da Bilibili SocialSisterYi aufgefordert hat, das API-Sammelprojekt zu entfernen, kann dieses Programm nicht weiterentwickelt werden; es wird jetzt nur noch gewartet.
Gitee-Projektadresse: https://gitee.com/cq-complex/TH-Bilibili-Toolbox
Derzeit beruhen alle Sprachen außer vereinfachtem Chinesisch, Englisch und traditionellem Chinesisch auf maschineller Übersetzung. Bei Fehlern freuen wir uns über Korrekturen!
Wenn einige Funktionen ablaufen, teilen Sie mir dies bitte rechtzeitig mit, damit ich versuchen werde, sie so schnell wie möglich zu beheben!
Bestätigung der Bereitstellung der API: SocialSisterYi""",
    f"""Développement du programme : CQ-COMPLEX
Page d’accueil du développeur Bilibili : https://space.bilibili.com/347752309
QQ du développeur : 2311804153
Groupe de communication QQ du développeur : 240742269
Version du programme : {version}
Heure de mise à jour : {u_day}/{u_month}/{u_year}
Bilibili ayant demandé à SocialSisterYi de retirer son projet de collecte d’API, ce programme ne peut plus être développé et n’est désormais maintenu qu’en mode correctif.
Adresse du projet Gitee : https://gitee.com/cq-complex/TH-Bilibili-Toolbox
À l’heure actuelle, toutes les langues, à l’exception du chinois simplifié, de l’anglais et du chinois traditionnel, reposent sur la traduction mécanique. S’il y a une erreur, n’hésitez pas à la corriger !
Si certaines fonctions expirent, merci de m’en informer à temps afin que j’essaie de les corriger le plus rapidement possible !
Reconnaissance de la fourniture de l’API : SocialSisterYi""",
    f"""การพัฒนาโปรแกรม: CQ-COMPLEX
โฮมเพจ Bilibili ของนักพัฒนาซอฟต์แวร์: https://space.bilibili.com/347752309
QQ ของนักพัฒนาซอฟต์แวร์: 2311804153
กลุ่มการสื่อสาร QQ ของนักพัฒนา: 240742269
เวอร์ชันของโปรแกรม: {version}
เวลาอัพเดท: {u_month}/{u_day}/{u_year}
เนื่องจาก Bilibili ได้ขอให้ SocialSisterYi นำโครงการรวบรวม API ออก โปรแกรมนี้จึงไม่สามารถพัฒนาต่อได้แล้ว ปัจจุบันอยู่ในโหมดซ่อมบำรุงเท่านั้น
ที่อยู่โครงการ Gitee: https://gitee.com/cq-complex/TH-Bilibili-Toolbox
ในปัจจุบันทุกภาษายกเว้นภาษาจีนประยุกต์อังกฤษและจีนดั้งเดิมพึ่งพาการแปลเชิงกล หากมีข้อผิดพลาดใด ๆ ยินดีที่จะแก้ไข!
หากฟังก์ชั่นบางอย่างหมดอายุโปรดบอกฉันทันเวลาเพื่อที่ฉันจะพยายามแก้ไขโดยเร็วที่สุด!
รับทราบการให้บริการ API: SocialSisterYi""",
    f"""프로그램 개발: CQ-COMPLEX
개발자의 Bilibili 홈페이지: https://space.bilibili.com/347752309
개발자의 QQ: 2311804153
개발자의 QQ 커뮤니케이션 그룹: 240742269
프로그램 버전: {version}
업데이트 시간: {u_year}년 {u_month}월 {u_day}일
Bilibili의 요청으로 SocialSisterYi의 API 수집 프로젝트가 내려가면서 이 프로그램은 더 이상 개발할 수 없게 되어 현재는 유지보수만 진행합니다.
Gitee 프로젝트 주소: https://gitee.com/cq-complex/TH-Bilibili-Toolbox
현재 중국어 간체, 영어 및 중국어 번체를 제외한 모든 언어는 기계 번역에 의존합니다. 오류가 있으면 수정을 환영합니다!
일부 기능이 만료되면 가능한 한 빨리 수정하도록 제 시간에 알려주십시오!
API 제공 승인: SocialSisterYi""",
    f"""Разработка программы: CQ-COMPLEX
Домашняя страница разработчика Bilibili: https://space.bilibili.com/347752309
QQ разработчика: 2311804153
Коммуникационная группа разработчика QQ: 240742269
Версия программы: {version}
Время обновления: {u_month}/{u_day}/{u_year}
Поскольку Bilibili потребовала от SocialSisterYi удалить проект сбора API, дальнейшая разработка этой программы невозможна — теперь она только поддерживается.
Адрес проекта Gitee: https://gitee.com/cq-complex/TH-Bilibili-Toolbox
В настоящее время все языки, кроме китайского упрощенного, английского и китайского традиционного, полагаются на механический перевод. Если есть какая-либо ошибка, добро пожаловать, чтобы исправить ее!
Если срок действия каких-то функций истекает, пожалуйста, сообщите мне об этом вовремя, чтобы я постарался исправить их как можно скорее!
Подтверждение предоставления API: SocialSisterYi""",
    f"""Phát triển chương trình: CQ-COMPLEX
Trang chủ Bilibili của nhà phát triển: https://space.bilibili.com/347752309
QQ của nhà phát triển: 2311804153
Nhóm giao tiếp QQ của nhà phát triển: 240742269
Phiên bản chương trình: {version}
Thời gian cập nhật: {u_month}/{u_day}/{u_year}
Do Bilibili đã yêu cầu SocialSisterYi gỡ dự án thu thập API, chương trình này không thể phát triển tiếp và hiện chỉ được bảo trì.
Địa chỉ dự án Gitee: https://gitee.com/cq-complex/TH-Bilibili-Toolbox
Hiện tại, tất cả các ngôn ngữ ngoại trừ tiếng Trung giản thể, tiếng Anh và tiếng Trung phồn thể đều dựa vào bản dịch cơ học. Nếu có bất kỳ lỗi nào, chào mừng bạn đến sửa nó!
Nếu một số chức năng hết hạn, vui lòng cho tôi biết kịp thời để tôi sẽ cố gắng sửa chúng càng sớm càng tốt!
Xác nhận cung cấp API: SocialSisterYi""",
    f"""Desenvolvimento de programas: CQ-COMPLEX
Página inicial do desenvolvedor Bilibili: https://space.bilibili.com/347752309
QQ do desenvolvedor: 2311804153
Grupo de comunicação QQ do desenvolvedor: 240742269
Versão do programa: {version}
Data de actualização: {u_day}/{u_month}/{u_year}
Como a Bilibili pediu a SocialSisterYi para retirar o projeto de recolha de API, este programa já não pode ser desenvolvido e passa a ter apenas manutenção.
Endereço do projeto Gitee: https://gitee.com/cq-complex/TH-Bilibili-Toolbox
Atualmente, todos os idiomas, exceto chinês simplificado, inglês e chinês tradicional, dependem de tradução mecânica. Se houver algum erro, bem-vindo para corrigi-lo!
Se algumas funções expirarem, por favor me diga a tempo para que eu vou tentar corrigi-las o mais rápido possível!
Reconhecimento de fornecer API: SocialSisterYi""",
    f"""Desarrollo del programa: CQ-COMPLEX
Página de inicio de Bilibili para desarrolladores: https://space.bilibili.com/347752309
QQ del desarrollador: 2311804153
Grupo de comunicación de QQ del desarrollador: 240742269
Versión del programa: {version}
Fecha de actualización: {u_day}/{u_month}/{u_year}
Como Bilibili pidió a SocialSisterYi retirar su proyecto de recopilación de API, este programa ya no puede seguir desarrollándose y ahora solo recibe mantenimiento.
Dirección del proyecto Gitee: https://gitee.com/cq-complex/TH-Bilibili-Toolbox
En la actualidad, todos los idiomas, excepto el chino simplificado, el inglés y el chino tradicional, dependen de la traducción mecánica. Si hay algún error, ¡bienvenido a corregirlo!
Si algunas funciones caducan, por favor dígame a tiempo para que intente solucionarlas lo antes posible.
Agradecimiento por facilitar la API: SocialSisterYi""",
    f"""Pengembangan Program: CQ-COMPLEX
Halaman beranda Bilibili pengembang: https://space.bilibili.com/347752309
QQ Pengembang: 2311804153
Grup komunikasi QQ pengembang: 240742269
Versi program: {version}
Tanggal pembaruan: {u_day}/{u_month}/{u_year}
Karena Bilibili meminta SocialSisterYi menurunkan proyek pengumpulan API, program ini tidak dapat dikembangkan lebih lanjut dan kini hanya dipelihara.
Alamat proyek Gitee: https://gitee.com/cq-complex/TH-Bilibili-Toolbox
Saat ini, semua bahasa kecuali Cina Sederhana, Inggris dan Cina Tradisional bergantung pada terjemahan mekanis. Jika ada kesalahan, selamat datang untuk memperbaikinya!
Jika beberapa fungsi kedaluwarsa, tolong beri tahu saya tepat waktu sehingga saya akan mencoba memperbaikinya sesegera mungkin!
Ucapan terima kasih atas penyediaan API: SocialSisterYi""",
]
menu_items = [
    {
        1: ("查询用户信息", query_user_info),
        2: ("查询昵称是否可用", check_nickname),
        3: ("查询视频信息", query_video_info),
        4: ("查询专栏信息", query_column_info),
        5: ("查询影视信息", query_media_info),
        6: ("AV号转BV号", convert_av_to_bv),
        7: ("BV号转AV号", convert_bv_to_av),
        8: ("获取APP开屏壁纸", get_wallpaper),
        9: ("查询视频评论", query_video_comments),
        10: ("查询其他评论", query_other_comments),
        11: ("搜索视频（请先登录）", search_video),
        12: ("搜索其他（请先登录）(D)", search_other),
        13: ("获取单视频推荐列表", get_recommendations),
        14: ("查询音频信息", query_audio_info),
        15: ("查询直播间信息（直播间ID）", query_liveroom_info),
        16: ("查询用户对应直播间信息", query_user_liveroom),
        17: ("获取最新视频排行榜", get_ranking),
        18: ("获取入站必刷视频", get_must_see),
        19: ("查看用户粉丝实时变动数据", view_fan_changes),
        "lu": ("登录用户信息", logged_user_info),
        "luop": ("登录用户操作", logged_user_operations),
        "locate": ("其他工具", other_tools),
        "login": ("登录（二维码扫码）", login_qrcode),
        "login2": ("登录（Cookies）", login_cookies),
        "check": ("检查文件、模块完整性", check_integrity),
        "ab": ("关于此程序", about_program),
        "lg": ("更新日志", view_changelog),
        "lang": ("更改语言", change_language),
        "font": ("更改字体", change_font),
        "cc": ("关闭程序", quit_program),
    },
    {
        1: ("Query user information", query_user_info),
        2: ("Check if nickname is available", check_nickname),
        3: ("Query video information", query_video_info),
        4: ("Query article information", query_column_info),
        5: ("Query movie/TV information", query_media_info),
        6: ("Convert AVID to BVID", convert_av_to_bv),
        7: ("Convert BVID to AVID", convert_bv_to_av),
        8: ("Get Bilibili app splash screen wallpapers", get_wallpaper),
        9: ("Query video comments", query_video_comments),
        10: ("Query other types of comments", query_other_comments),
        11: ("Search videos (login required)", search_video),
        12: ("Search other types (login required) (in development)", search_other),
        13: ("Get the recommendation list of a video", get_recommendations),
        14: ("Query audio information", query_audio_info),
        15: ("Query live streaming room information (Room ID)", query_liveroom_info),
        16: ("Query a user's live streaming room", query_user_liveroom),
        17: ("Get the latest video ranking", get_ranking),
        18: ("Get must-see videos", get_must_see),
        19: ("See the real-time fan count of an account", view_fan_changes),
        "lu": ("Logged-in user information", logged_user_info),
        "luop": ("ログイン中のユーザー操作", logged_user_operations),
        "locate": ("その他のツール", other_tools),
        "login": ("Log in (QR code)", login_qrcode),
        "login2": ("Log in (Cookies)", login_cookies),
        "check": ("ファイルとモジュールの整合性を確認", check_integrity),
        "ab": ("About the program", about_program),
        "lg": ("Update log", view_changelog),
        "lang": ("Change language", change_language),
        "font": ("Change font", change_font),
        "cc": ("Exit", quit_program),
    },
    {
        1: ("查詢使用者資訊", query_user_info),
        2: ("查詢暱稱是否可用", check_nickname),
        3: ("查詢影片資訊", query_video_info),
        4: ("查詢專欄資訊", query_column_info),
        5: ("查詢影視資訊", query_media_info),
        6: ("AV號轉BV號", convert_av_to_bv),
        7: ("BV號轉AV號", convert_bv_to_av),
        8: ("獲取APP開屏桌布", get_wallpaper),
        9: ("查詢影片評論", query_video_comments),
        10: ("查詢其他評論", query_other_comments),
        11: ("搜尋影片（請先登入）", search_video),
        12: ("搜尋其他（請先登入）(D)", search_other),
        13: ("獲取單影片推薦列表", get_recommendations),
        14: ("查詢音訊資訊", query_audio_info),
        15: ("查詢直播間資訊（直播間ID）", query_liveroom_info),
        16: ("查詢使用者對應直播間資訊", query_user_liveroom),
        17: ("獲取最新影片排行榜", get_ranking),
        18: ("獲取入站必刷影片", get_must_see),
        19: ("檢視使用者粉絲實時變動資料", view_fan_changes),
        "lu": ("已登入使用者資訊", logged_user_info),
        "luop": ("已登入使用者操作", logged_user_operations),
        "locate": ("其他工具", other_tools),
        "login": ("登入（掃描 QR Code）", login_qrcode),
        "login2": ("登入（Cookies）", login_cookies),
        "check": ("檢查檔案、模組完整性", check_integrity),
        "ab": ("關於此程式", about_program),
        "lg": ("更新日誌", view_changelog),
        "lang": ("更改語言", change_language),
        "font": ("更改字型", change_font),
        "cc": ("關閉程式", quit_program),
    },
    {
        1: ("ユーザーの情報の照会", query_user_info),
        2: ("ニックネームが利用可能かどうかを確認する", check_nickname),
        3: ("動画の情報照会", query_video_info),
        4: ("コラム情報の照会", query_column_info),
        5: ("映画・ドラマ情報の照会", query_media_info),
        6: ("AVID から BVID への変換", convert_av_to_bv),
        7: ("BVID から AVID への変換", convert_bv_to_av),
        8: ("アプリ起動画面の壁紙を取得", get_wallpaper),
        9: ("動画のコメントを問い合わせる", query_video_comments),
        10: ("他種のコメントを問い合わせる", query_other_comments),
        11: ("動画の検索(ログインが必要)", search_video),
        12: ("他のタイプの検索 (ログインが必要) (開発中)", search_other),
        13: ("ビデオのレコメンデーションリストの取得", get_recommendations),
        14: ("音声情報の問い合わせ", query_audio_info),
        15: ("ライブ配信ルームのお問い合わせ(ルームID)", query_liveroom_info),
        16: ("ユーザーのライブ配信ルームへの問い合わせ", query_user_liveroom),
        17: ("最新の動画ランキングの取得", get_ranking),
        18: ("必見の動画を入手する", get_must_see),
        19: ("アカウントのファン数をリアルタイムで確認する", view_fan_changes),
        "lu": ("ログイン中のユーザー情報", logged_user_info),
        "luop": ("Aktionen des angemeldeten Benutzers", logged_user_operations),
        "locate": ("Weitere Werkzeuge", other_tools),
        "login": ("ログイン（QRコード）", login_qrcode),
        "login2": ("ログイン (Cookies)", login_cookies),
        "check": ("Integrität von Dateien und Modulen prüfen", check_integrity),
        "ab": ("プログラムについて", about_program),
        "lg": ("更新ログ", view_changelog),
        "lang": ("言語の変更", change_language),
        "font": ("フォントの変更", change_font),
        "cc": ("終了", quit_program),
    },
    {
        1: ("Abfrage von Informationen eines Benutzers", query_user_info),
        2: ("Prüfen Sie, ob der Spitzname verfügbar ist", check_nickname),
        3: ("Abrufen von Informationen zu einem Video", query_video_info),
        4: ("Abfrage von Informationen zu einem Artikel", query_column_info),
        5: ("Informationen zu einem Film oder einer Serie abfragen", query_media_info),
        6: ("Konvertieren von AVID in BVID", convert_av_to_bv),
        7: ("Konvertieren von BVID in AVID", convert_bv_to_av),
        8: ("App-Startbildschirm-Hintergründe abrufen", get_wallpaper),
        9: ("Abfrage von Kommentaren zu einem Video", query_video_comments),
        10: ("Anfordern von Kommentaren anderer Art", query_other_comments),
        11: ("Suchen von Videos (Anmeldung erforderlich)", search_video),
        12: ("Suche nach anderen Typen (Anmeldung erforderlich) (Entwicklung)", search_other),
        13: ("Abrufen der Empfehlungsliste eines Videos", get_recommendations),
        14: ("Abrufen von Informationen zu einem Audio", query_audio_info),
        15: ("Abfrage von Informationen zu einem Live-Streaming-Raum (Raum-ID)", query_liveroom_info),
        16: ("Abfrage des Live-Streaming-Raums eines Benutzers", query_user_liveroom),
        17: ("Abrufen der neuesten Video-Rankings", get_ranking),
        18: ("Sehenswerte Videos erhalten", get_must_see),
        19: ("Die Follower-Anzahl eines Kontos in Echtzeit anzeigen", view_fan_changes),
        "lu": ("Informationen zum angemeldeten Benutzer", logged_user_info),
        "luop": ("Opérations de l’utilisateur connecté", logged_user_operations),
        "locate": ("Autres outils", other_tools),
        "login": ("Einloggen (QR-Code)", login_qrcode),
        "login2": ("Einloggen (Cookies)", login_cookies),
        "check": ("Vérifier l’intégrité des fichiers et des modules", check_integrity),
        "ab": ("Über das Programm", about_program),
        "lg": ("Aktualisierungsprotokoll", view_changelog),
        "lang": ("Ändern der Sprache", change_language),
        "font": ("Schriftarten ändern", change_font),
        "cc": ("Beenden", quit_program),
    },
    {
        1: ("Demander des informations à un utilisateur", query_user_info),
        2: ("Vérifier si un pseudo est disponible", check_nickname),
        3: ("Demander des informations sur une vidéo", query_video_info),
        4: ("Demander des informations sur un article", query_column_info),
        5: ("Demander des informations sur un film ou une série", query_media_info),
        6: ("Conversion d’AVID en BVID", convert_av_to_bv),
        7: ("Conversion de BVID en AVID", convert_bv_to_av),
        8: ("Obtenir les fonds d’écran de démarrage de l’application Bilibili", get_wallpaper),
        9: ("Demander des commentaires sur une vidéo", query_video_comments),
        10: ("Solliciter des commentaires d’autres types", query_other_comments),
        11: ("Recherche de vidéos (connexion requise)", search_video),
        12: (
            "Recherche d’autres types (connexion requise) (en cours de développement)",
            search_other,
        ),
        13: ("Obtenir la liste de recommandations d’une vidéo", get_recommendations),
        14: ("Demander des informations sur un audio", query_audio_info),
        15: (
            "Demander des informations sur une salle de diffusion en direct (ID de salle)",
            query_liveroom_info,
        ),
        16: ("Demander la salle de diffusion en direct d’un utilisateur", query_user_liveroom),
        17: ("Obtenir les derniers classements vidéo", get_ranking),
        18: ("Obtenir des vidéos incontournables", get_must_see),
        19: ("Voir le nombre de fans en temps réel d’un compte", view_fan_changes),
        "lu": ("Informations sur l’utilisateur connecté", logged_user_info),
        "luop": ("การดำเนินการของผู้ใช้ที่เข้าสู่ระบบ", logged_user_operations),
        "locate": ("เครื่องมืออื่น ๆ", other_tools),
        "login": ("Connexion (code QR)", login_qrcode),
        "login2": ("Connexion (Cookies)", login_cookies),
        "check": ("ตรวจสอบความสมบูรณ์ของไฟล์และโมดูล", check_integrity),
        "ab": ("À propos du programme", about_program),
        "lg": ("Mettre à jour le journal", view_changelog),
        "lang": ("Changer de langue", change_language),
        "font": ("Modification des polices", change_font),
        "cc": ("Quitter", quit_program),
    },
    {
        1: ("การสอบถามข้อมูลของผู้ใช้", query_user_info),
        2: ("ตรวจสอบว่ามีชื่อเล่นหรือไม่", check_nickname),
        3: ("การสอบถามข้อมูลของวิดีโอ", query_video_info),
        4: ("การสอบถามข้อมูลของคอลัมน์", query_column_info),
        5: ("สอบถามข้อมูลของโปรแกรม", query_media_info),
        6: ("การแปลง AVID เป็น BVID", convert_av_to_bv),
        7: ("การแปลง BVID เป็น AVID", convert_bv_to_av),
        8: ("รับวอลเปเปอร์ APP ของโฮมไซต์", get_wallpaper),
        9: ("การสอบถามความคิดเห็นของวิดีโอ", query_video_comments),
        10: ("สอบถามความคิดเห็นประเภทอื่น ๆ", query_other_comments),
        11: ("การค้นหาวิดีโอ (ต้องเข้าสู่ระบบ)", search_video),
        12: ("การค้นหาประเภทอื่น (ต้องเข้าสู่ระบบ) (กําลังพัฒนา)", search_other),
        13: ("การรับรายการคําแนะนําของวิดีโอ", get_recommendations),
        14: ("สอบถามข้อมูลของเสียง", query_audio_info),
        15: ("สอบถามข้อมูลห้องสตรีมมิงแบบสด (รหัสห้อง)", query_liveroom_info),
        16: ("สอบถามห้องสตรีมมิงแบบสดของผู้ใช้", query_user_liveroom),
        17: ("รับการจัดอันดับวิดีโอล่าสุด", get_ranking),
        18: ("การรับวิดีโอที่ต้องดู", get_must_see),
        19: ("การดูจํานวนแฟนคลับแบบเรียลไทม์ของบัญชี", view_fan_changes),
        "lu": ("ข้อมูลผู้ใช้ที่เข้าสู่ระบบ", logged_user_info),
        "luop": ("로그인한 사용자 작업", logged_user_operations),
        "locate": ("기타 도구", other_tools),
        "login": ("เข้าสู่ระบบด้วยคิวอาร์โค้ด", login_qrcode),
        "login2": ("การเข้าสู่ระบบ (Cookies)", login_cookies),
        "check": ("파일 및 모듈 무결성 확인", check_integrity),
        "ab": ("เกี่ยวกับโปรแกรม", about_program),
        "lg": ("บันทึกการอัปเดต", view_changelog),
        "lang": ("การเปลี่ยนภาษา", change_language),
        "font": ("การเปลี่ยนแบบอักษร", change_font),
        "cc": ("ทางออก", quit_program),
    },
    {
        1: ("사용자 정보 조회", query_user_info),
        2: ("닉네임을 사용할 수 있는지 확인", check_nickname),
        3: ("동영상 정보 조회하기", query_video_info),
        4: ("칼럼 정보 조회하기", query_column_info),
        5: ("프로그램 정보 조회", query_media_info),
        6: ("AVID를 BVID로 변환", convert_av_to_bv),
        7: ("BVID를 AVID로 변환", convert_bv_to_av),
        8: ("홈페이지의 APP 월페이퍼 가져오기", get_wallpaper),
        9: ("동영상에 대한 댓글 문의하기", query_video_comments),
        10: ("다른 유형의 의견 조회", query_other_comments),
        11: ("동영상 검색하기(로그인 필요)", search_video),
        12: ("다른 타입 검색하기(로그인 필요) (개발중)", search_other),
        13: ("동영상의 추천 목록 가져오기", get_recommendations),
        14: ("오디오 정보 조회", query_audio_info),
        15: ("라이브 스트리밍 룸 정보 조회하기(Room ID)", query_liveroom_info),
        16: ("사용자의 라이브 스트리밍 룸 조회하기", query_user_liveroom),
        17: ("최신 동영상 랭킹 조회", get_ranking),
        18: ("꼭 봐야 할 동영상 얻기", get_must_see),
        19: ("계정의 실시간 팬 수 보기", view_fan_changes),
        "lu": ("로그인한 사용자 정보", logged_user_info),
        "luop": ("Действия вошедшего пользователя", logged_user_operations),
        "locate": ("Другие инструменты", other_tools),
        "login": ("로그인(QR 코드)", login_qrcode),
        "login2": ("로그인(Cookies)", login_cookies),
        "check": ("Проверить целостность файлов и модулей", check_integrity),
        "ab": ("프로그램 소개", about_program),
        "lg": ("업데이트 로그", view_changelog),
        "lang": ("언어 변경", change_language),
        "font": ("글꼴 변경", change_font),
        "cc": ("종료", quit_program),
    },
    {
        1: ("Запрос информации о пользователе", query_user_info),
        2: ("Проверьте, доступен ли никнейм", check_nickname),
        3: ("Запросить информацию о видео", query_video_info),
        4: ("Запрос информации о статье", query_column_info),
        5: ("Запросить информацию о фильме или сериале", query_media_info),
        6: ("Конвертация AVID в BVID", convert_av_to_bv),
        7: ("Конвертация BVID в AVID", convert_bv_to_av),
        8: ("Получить обои экрана запуска приложения Bilibili", get_wallpaper),
        9: ("Запрос комментариев к видео", query_video_comments),
        10: ("Запрос комментариев других типов", query_other_comments),
        11: ("Поиск видео (требуется вход в систему)", search_video),
        12: ("Поиск по другим типам (требуется вход) (в разработке)", search_other),
        13: ("Получить рекомендательный список видео", get_recommendations),
        14: ("Запросить информацию об аудио", query_audio_info),
        15: (
            "Запрос информации о комнате для прямых трансляций (идентификатор комнаты)",
            query_liveroom_info,
        ),
        16: ("Запрос комнаты прямой трансляции пользователя", query_user_liveroom),
        17: ("Получите последние рейтинги видео", get_ranking),
        18: ("Получить обязательные к просмотру видео", get_must_see),
        19: (
            "Просмотр количества поклонников учетной записи в режиме реального времени",
            view_fan_changes,
        ),
        "lu": ("Информация о вошедшем пользователе", logged_user_info),
        "luop": ("Thao tác của người dùng đã đăng nhập", logged_user_operations),
        "locate": ("Công cụ khác", other_tools),
        "login": ("Войти по QR-коду", login_qrcode),
        "login2": ("Войти (Cookies)", login_cookies),
        "check": ("Kiểm tra tính toàn vẹn của tệp và mô-đun", check_integrity),
        "ab": ("О программе", about_program),
        "lg": ("Журнал обновлений", view_changelog),
        "lang": ("Изменение языка", change_language),
        "font": ("Изменение шрифтов", change_font),
        "cc": ("Выход", quit_program),
    },
    {
        1: ("Hỏi thông tin của người dùng", query_user_info),
        2: ("Kiểm tra xem biệt hiệu có sẵn không", check_nickname),
        3: ("Hỏi thông tin của video", query_video_info),
        4: ("Yêu cầu thông tin của một bài viết", query_column_info),
        5: ("Hỏi thông tin của một bộ phim/sê-ri", query_media_info),
        6: ("Chuyển đổi AVID sang BVID", convert_av_to_bv),
        7: ("Chuyển đổi BVID sang AVID", convert_bv_to_av),
        8: ("Lấy hình nền màn hình khởi động của ứng dụng Bilibili", get_wallpaper),
        9: ("Yêu cầu nhận xét của video", query_video_comments),
        10: ("Hỏi ý kiến của các loại khác", query_other_comments),
        11: ("Tìm kiếm video (Yêu cầu đăng nhập)", search_video),
        12: ("Tìm kiếm các loại khác (Yêu cầu đăng nhập) (Đang phát triển)", search_other),
        13: ("Nhận danh sách đề xuất của video", get_recommendations),
        14: ("Hỏi thông tin về âm thanh", query_audio_info),
        15: ("Hỏi thông tin về phòng phát trực tiếp (ID phòng)", query_liveroom_info),
        16: ("Hỏi phòng phát trực tiếp của người dùng", query_user_liveroom),
        17: ("Nhận thứ hạng video mới nhất", get_ranking),
        18: ("Nhận video phải xem", get_must_see),
        19: ("Xem số lượng người hâm mộ theo thời gian thực của một tài khoản", view_fan_changes),
        "lu": ("Thông tin người dùng đã đăng nhập", logged_user_info),
        "luop": ("Operações do utilizador com sessão iniciada", logged_user_operations),
        "locate": ("Outras ferramentas", other_tools),
        "login": ("Đăng nhập bằng mã QR", login_qrcode),
        "login2": ("Đăng nhập (Cookies)", login_cookies),
        "check": ("Verificar a integridade dos ficheiros e módulos", check_integrity),
        "ab": ("Về chương trình", about_program),
        "lg": ("Nhật ký cập nhật", view_changelog),
        "lang": ("Thay đổi ngôn ngữ", change_language),
        "font": ("Thay đổi phông chữ", change_font),
        "cc": ("Thoát", quit_program),
    },
    {
        1: ("Consultar informações de um utilizador", query_user_info),
        2: ("Verificar se a alcunha está disponível", check_nickname),
        3: ("Consultar informações de um vídeo", query_video_info),
        4: ("Consultar informações de um artigo", query_column_info),
        5: ("Consultar informações de um filme ou série", query_media_info),
        6: ("Converter AVID para BVID", convert_av_to_bv),
        7: ("Converter BVID para AVID", convert_bv_to_av),
        8: ("Obter papéis de parede do ecrã de arranque da app Bilibili", get_wallpaper),
        9: ("Consultar comentários de um vídeo", query_video_comments),
        10: ("Consultar comentários de outros tipos", query_other_comments),
        11: ("Procurar vídeos (obrigatório Login)", search_video),
        12: ("Procurar outros tipos (Login-obrigatório) (Desenvolvimento)", search_other),
        13: ("Obter a lista de recomendações de um vídeo", get_recommendations),
        14: ("Perguntar a informação de um áudio", query_audio_info),
        15: (
            "Consultar informações de uma sala de transmissão ao vivo (ID do quarto)",
            query_liveroom_info,
        ),
        16: ("Consultar a sala de streaming ao vivo de um usuário", query_user_liveroom),
        17: ("Obtenha as últimas classificações de vídeos", get_ranking),
        18: ("Obter vídeos obrigatórios", get_must_see),
        19: ("Veja a quantidade de fãs em tempo real de uma conta", view_fan_changes),
        "lu": ("Informação do utilizador com sessão iniciada", logged_user_info),
        "luop": ("Operaciones del usuario con sesión iniciada", logged_user_operations),
        "locate": ("Otras herramientas", other_tools),
        "login": ("Iniciar sessão por código QR", login_qrcode),
        "login2": ("Iniciar sessão (Cookies)", login_cookies),
        "check": ("Comprobar la integridad de los archivos y módulos", check_integrity),
        "ab": ("Sobre o programa", about_program),
        "lg": ("Actualizar o registo", view_changelog),
        "lang": ("Mudar o idioma", change_language),
        "font": ("Mudar os tipos de letra", change_font),
        "cc": ("Sair", quit_program),
    },
    {
        1: ("Consultar información de un usuario", query_user_info),
        2: ("Compruebe si el apodo está disponible", check_nickname),
        3: ("Solicitar información de un vídeo", query_video_info),
        4: ("Consultar información de un artículo", query_column_info),
        5: ("Consultar información de una película o serie", query_media_info),
        6: ("Convertir AVID a BVID", convert_av_to_bv),
        7: ("Convertir BVID a AVID", convert_bv_to_av),
        8: ("Obtener fondos de pantalla de la pantalla de inicio de la app Bilibili", get_wallpaper),
        9: ("Consultar comentarios de un vídeo", query_video_comments),
        10: ("Consultar comentarios de otro tipo", query_other_comments),
        11: ("Buscar vídeos (es necesario iniciar sesión)", search_video),
        12: ("Buscar otros tipos (Requiere inicio de sesión) (En desarrollo)", search_other),
        13: ("Obtener una lista de recomendaciones de un vídeo", get_recommendations),
        14: ("Consultar información de un audio", query_audio_info),
        15: (
            "Solicitar información de una sala de transmisión en vivo (ID de sala)",
            query_liveroom_info,
        ),
        16: ("Consultar la sala de transmisión en vivo de un usuario", query_user_liveroom),
        17: ("Obtén las últimas clasificaciones de video", get_ranking),
        18: ("Consigue vídeos imprescindibles", get_must_see),
        19: ("Ver la cantidad de fans en tiempo real de una cuenta", view_fan_changes),
        "lu": ("Información del usuario con sesión iniciada", logged_user_info),
        "luop": ("Operaciones del usuario con sesión iniciada", logged_user_operations),
        "locate": ("Otras herramientas", other_tools),
        "login": ("Iniciar sesión con código QR", login_qrcode),
        "login2": ("Inicio de sesión (Cookies)", login_cookies),
        "check": ("Comprobar la integridad de los archivos y módulos", check_integrity),
        "ab": ("Sobre el programa", about_program),
        "lg": ("Registro de actualizaciones", view_changelog),
        "lang": ("Cambiar idioma", change_language),
        "font": ("Cambiar fuentes", change_font),
        "cc": ("Salir", quit_program),
    },
    {
        1: ("Menanyakan informasi pengguna", query_user_info),
        2: ("Periksa apakah nama panggilan tersedia", check_nickname),
        3: ("Menanyakan informasi video", query_video_info),
        4: ("Menanyakan informasi artikel", query_column_info),
        5: ("Menanyakan informasi film/serial", query_media_info),
        6: ("Konversi AVID ke BVID", convert_av_to_bv),
        7: ("Konversi BVID ke AVID", convert_bv_to_av),
        8: ("Dapatkan wallpaper layar pembuka aplikasi Bilibili", get_wallpaper),
        9: ("Menanyakan komentar video", query_video_comments),
        10: ("Menanyakan komentar jenis lain", query_other_comments),
        11: ("Cari video (Login diperlukan)", search_video),
        12: ("Cari jenis lain (Login-diperlukan) (Mengembangkan)", search_other),
        13: ("Mendapatkan daftar rekomendasi video", get_recommendations),
        14: ("Menanyakan informasi audio", query_audio_info),
        15: ("Menanyakan informasi ruang live streaming (ID Kamar)", query_liveroom_info),
        16: ("Menanyakan ruang streaming langsung pengguna", query_user_liveroom),
        17: ("Dapatkan peringkat video terbaru", get_ranking),
        18: ("Mendapatkan video yang wajib ditonton", get_must_see),
        19: ("Lihat jumlah penggemar real-time dari sebuah akun", view_fan_changes),
        "lu": ("Info pengguna yang sudah masuk", logged_user_info),
        "luop": ("Operasi pengguna yang sudah masuk", logged_user_operations),
        "locate": ("Alat lainnya", other_tools),
        "login": ("Masuk dengan kode QR", login_qrcode),
        "login2": ("Masuk (Cookies)", login_cookies),
        "check": ("Periksa integritas file dan modul", check_integrity),
        "ab": ("Tentang program ini", about_program),
        "lg": ("Log pembaruan", view_changelog),
        "lang": ("Ganti bahasa", change_language),
        "font": ("Mengubah font", change_font),
        "cc": ("Keluar", quit_program),
    },
]
current_menu = menu_items[lang]
loading_window.title(window_title)
lvid1 = [str(i) for i in range(-2, 10)]
welcome_texts = [
    f"欢迎使用{window_title}\n" + "开发者B站首页：https://space.bilibili.com/347752309",
    f"Welcome to use {window_title}\n"
    + "Developer's Bilibili space: https://space.bilibili.com/347752309",
    f"歡迎使用{window_title}\n" + "開發者B站首頁：https://space.bilibili.com/347752309",
    f"{window_title} へようこそ\n"
    + "開発者のBilibiliスペース：https://space.bilibili.com/347752309",
    f"Willkommen bei {window_title}\n"
    + "Bilibili-Seite des Entwicklers: https://space.bilibili.com/347752309",
    f"Bienvenue sur {window_title}\n"
    + "Espace Bilibili du développeur : https://space.bilibili.com/347752309",
    f"ยินดีต้อนรับสู่การใช้งาน {window_title}\n"
    + "พื้นที่ Bilibili ของนักพัฒนา: https://space.bilibili.com/347752309",
    f"{window_title} 사용을 환영합니다\n"
    + "개발자의 Bilibili 공간: https://space.bilibili.com/347752309",
    f"Добро пожаловать в {window_title}\n"
    + "Пространство разработчика Bilibili: https://space.bilibili.com/347752309",
    f"Chào mừng bạn đến sử dụng {window_title}\n"
    + "Không gian Bilibili của nhà phát triển: https://space.bilibili.com/347752309",
    f"Bem-vindo ao {window_title}\n"
    + "Espaço Bilibili do desenvolvedor: https://space.bilibili.com/347752309",
    f"Bienvenido a usar {window_title}\n"
    + "Enlace del desarrollador al espacio Bilibili: https://space.bilibili.com/347752309",
    f"Selamat menggunakan {window_title}\n"
    + "Tautan ruang Bilibili pengembang: https://space.bilibili.com/347752309",
]
button_map = {}
s = 0
k = [i for i in current_menu]
grid_row = MENU_START_ROW
bto_count = MENU_START_ROW
bto_column = 0
for i in current_menu:
    bto = Button(loading_window, text=current_menu[i][0], command=current_menu[i][1], font=default_font)
    bto.grid(row=bto_count, column=bto_column, padx=round(MENU_COLUMN_PAD * dpi_scale))
    if bto_count == 12:
        bto_count = 2
        bto_column += 1
    button_map[k[s]] = bto
    s += 1
    bto_count += 1
loading_window.protocol("WM_DELETE_WINDOW", quit_program)  # 更改右上角关闭按钮的功能
showwarning(title=window_title, message="由于B站官方已要求Social Sister Yi大佬将他的B站API项目下架，本应用程序已几乎失去继续开发的可能性，因此本程序将不再维护！" + 
     "\nDue to Bilibili's remove request to SocialSisterYi's API collect project, this program will permanently stop update!")
showinfo(title=window_title, message=welcome_texts[lang])
# button_map[17].configure(state=DISABLED)
loading_window.mainloop()
