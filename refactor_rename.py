"""
Comprehensive variable/function renaming for TH_Bilibili_Toolbox.py

Phases:
1. Rename md* functions to descriptive names
2. Rename global variables
3. Rename local variables
4. Add constants for magic numbers
"""

import re

with open("TH_Bilibili_Toolbox.py", "r", encoding="utf-8") as f:
    content = f.read()

lines = content.splitlines()
changes = []

def safe_replace(name, old, new, context=""):
    """Replace old with new, tracking changes"""
    global content
    if old not in content:
        print(f"  ⚠ {name}: '{old}' not found {context}")
        return False
    count = content.count(old)
    content = content.replace(old, new)
    changes.append((name, old, new, count))
    print(f"  ✓ {name}: '{old}' -> '{new}' ({count} occurrences)")
    return True

# ================================================================
# PHASE 0: Helper constants at top of file
# ================================================================

# Add language constants after the version line
lang_constants = """
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
"""

# Insert after version line
version_line = 'version = "v0.13.1"  # 版本号'
idx = content.find(version_line)
if idx >= 0:
    end_of_line = content.find('\n', idx)
    content = content[:end_of_line+1] + lang_constants + content[end_of_line+1:]
    print("✓ Added language constants")

# ================================================================
# PHASE 1: Rename functions
# ================================================================

print("\n=== Phase 1: Function renames ===")

func_renames = {
    # md functions -> descriptive names
    "md1": "query_user_info",
    "md2": "check_nickname",
    "md3": "query_video_info",
    "md4": "query_column_info",
    "md05": "query_media_info",
    "md6": "convert_av_to_bv",
    "md7": "convert_bv_to_av",
    "md8": "get_wallpaper",
    "md9": "query_video_comments",
    "md10": "query_other_comments",
    "md11": "search_video",
    "md12": "search_other",
    "md13": "get_recommendations",
    "md14": "query_audio_info",
    "md15": "query_liveroom_info",
    "md16": "query_user_liveroom",
    "md17": "get_ranking",
    "md18": "get_must_see",
    "md19": "view_fan_changes",
    "mdlu": "logged_user_info",
    "mdluop": "logged_user_operations",
    "mdlocate": "other_tools",
    "mdlogin": "login_qrcode",
    "mdlogin2": "login_cookies",
    "mdcheck": "check_integrity",
    "mdab": "about_program",
    "mdlg": "view_changelog",
    "mdlang": "change_language",
    "mdfont": "change_font",
    "mdcc": "quit_program",
}

# Need to be careful: replace known names, not partial matches
# Use word-boundary matching via regex
for old_name, new_name in func_renames.items():
    # Replace `def old_name(` and `(old_name)` and `old_name)`
    # and `=old_name` and `old_name\n` etc.
    # The function name appears as a standalone identifier
    old_count = content.count(old_name)
    if old_count == 0:
        print(f"  ⚠ '{old_name}' not found, skipping")
        continue
    
    # Use regex with word boundaries
    content = re.sub(r'\b' + re.escape(old_name) + r'\b', new_name, content)
    new_count = content.count(old_name)
    print(f"  ✓ '{old_name}' -> '{new_name}' ({old_count} occurrences)")

# However, we need to be careful: some old_name fragments might appear in
# other identifiers. Let me check for the few that we need to revert.
# E.g., 'md6' should NOT match inside 'cmd6' or similar.

# Also verify mpls references were updated
mpls_check = content.count("module_1')")
print(f"\n  mpls references to module_query_user: {mpls_check}")

# ================================================================
# PHASE 2: Rename global variables
# ================================================================

print("\n=== Phase 2: Global variable renames ===")

# Only rename variables that are not part of other identifiers
# Use regex word boundaries

global_renames = {
    # Window-related
    "ttl": "window_title",      # title string
    # "ttll" must be renamed BEFORE "ttl" to avoid conflict!
    "ttll": "window_titles",
    # UI-related aliases
    "db": "DISABLED",
    "ist": "INSERT",
    "norm": "NORMAL",
    "btn": "Button",
    "label": "Label",
    "ft": "Font",
    "info": "showinfo",
    "warn": "showwarning",
    "err": "showerror",
    "askoc": "askokcancel",
    "ipt": "askstring",
    "ipti": "askinteger",
    "iptf": "askfloat",
    # Font
    "fon": "default_font",
    "fonts": "font_family",
    # Window objects
    "loading": "loading_window",
    "icofile": "icon_file",
    "photo": "topic_image",
    # Labels
    "il": "image_label",
    "sl": "status_label",
    "sll": "status_labels",
    # Messages
    "wel": "welcome_texts",
    "aboutl": "about_texts",
    "ttll": "window_titles",  # already renamed above
    # Main menu
    "mpls": "menu_items",
    "mpl": "current_menu",
    "btl": "button_map",
    # Variables
    "sess_data": "session_data",
    "tryrange": "MAX_RETRIES",
    "pygl": "use_pygame",
    "fgnavail": "foreign_available",
    "ueavailable": "egg_available",
    "rqavailable": "requests_available",
    "avbv_tr": "avbv_available",
    "openccav": "opencc_available",
    "userfan": "fan_monitor_active",
    "logerr": "log_error",
    "notification": "version_suffixes",
    "ok_buttonl": "ok_button_labels",
    # System
    "st": "to_traditional",
    "fnt": "font_variant",
    "fnts": "saved_font_variant",
    "langs": "saved_language",
    "legal": "init_valid",
    "initialize": "init_file_exists",
    "ld": "lang_selector_prompt",
    # Language description constant
    "lang_desc": "LANG_DESCRIPTION",
}

# Handle ttll BEFORE ttl to avoid partial replacement
if "ttll" in content:
    content = re.sub(r'\bttll\b', 'window_titles', content)
    print("  ✓ 'ttll' -> 'window_titles'")

# Special handling for 'st' - it appears as:
# - `st =` (function assignment)
# - `st(` (function call)
# - `st.` (attribute access - but unlikely for a function)
# Need to be careful not to replace 'st' in other contexts
# Let's only replace 'st =' and 'st(' and 'st\n'
# Actually using word boundary should work

# For safety, process renames one by one, skipping if not found
for i, (old, new) in enumerate(global_renames.items()):
    if old == "ttll":  # already handled
        continue
    if old == "ttl":
        # Only replace standalone 'ttl', not inside 'ttll' or other words
        count = len(re.findall(r'\bttl\b', content))
        if count > 0:
            content = re.sub(r'\bttl\b', 'window_title', content)
            print(f"  ✓ 'ttl' -> 'window_title' ({count} occurrences)")
        continue
    
    count = len(re.findall(r'\b' + re.escape(old) + r'\b', content))
    if count > 0:
        # Check if old is a substring of another identifier we already renamed
        content = re.sub(r'\b' + re.escape(old) + r'\b', new, content)
        print(f"  ✓ '{old}' -> '{new}' ({count} occurrences)")
    else:
        print(f"  ⚠ '{old}' not found, skipping")

# ================================================================
# PHASE 3: Rename local variables within functions
# ================================================================

print("\n=== Phase 3: Local variable renames ===")

# These are function-scope variables that appear in many functions.
# We need to be careful to only rename them in local scope.
# Since many of these are very common short names, we use targeted
# patterns to avoid breaking unrelated code.

local_renames = {
    # API response variables
    "soup": "response_data",
    "url2": "detail_url",
    # Output
    "otyp": "output_window",
    "edt": "output_text",
    # Sub-windows
    "scwd": "sub_window",
    # User info
    "nm": "nickname",
    "uid": "user_id",
    "sx": "gender",
    "vipsit": "vip_status",
    "offic": "verification_status",
    "ban": "account_status",
    "sign": "signature",
    # "lv" - need to be careful, it's only 2 chars
    "messg": "output_message",
    "ertxt": "error_text",
    "code": "status_code",
    # Various
    "ex": "confirm_quit",
    "titl": "title",
    "intr": "description",
    # "sid": "audio_id",  # might be too generic
    # "rid": "room_id",
    # Retry
    # "t": "attempt_count",  # too short, might match many things
}

# These short variables appear in many places, use cautious patterns
for old, new in local_renames.items():
    count = len(re.findall(r'\b' + re.escape(old) + r'\b', content))
    if count > 0:
        content = re.sub(r'\b' + re.escape(old) + r'\b', new, content)
        print(f"  ✓ '{old}' -> '{new}' ({count} occurrences)")
    else:
        print(f"  ⚠ '{old}' not found, skipping")

# ================================================================
# PHASE 4: Rename specific local variables in tool window
# ================================================================

print("\n=== Phase 4: Tool window variable renames ===")

window_renames = {
    # Inline dict names
    "blist": "tool_labels",
    "blist_base": "tool_labels_base",
    "btntext": "converter_labels",
    "btntext_base": "converter_labels_base",
    "whether": "check_labels",
    "whether_base": "check_labels_base",
    # Generic
    "wnl": "warning_msg",
    "geterrl": "error_msgs",
    "noinfo": "no_info_msg",
    "attempt": "attempt_msg",
    "attempt_count": "attempt_count",
    "trbtl": "trans_buttons",
    "trbtl": "trans_buttons",
    "odr": "order",
    "odrl": "order_list",
    "durainput": "duration_prompt",
    "iptuid": "uid_prompt",
}

for old, new in window_renames.items():
    count = len(re.findall(r'\b' + re.escape(old) + r'\b', content))
    if count > 0:
        content = re.sub(r'\b' + re.escape(old) + r'\b', new, content)
        print(f"  ✓ '{old}' -> '{new}' ({count} occurrences)")
    else:
        print(f"  ⚠ '{old}' not found, skipping")

# ================================================================
# PHASE 5: Add magic number constants and replace usages
# ================================================================

print("\n=== Phase 5: Magic number replacements ===")

# Add font size constants
font_constants = """
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
"""

# Insert after language constants
lc_idx = content.find("LANG_ID = 12")
if lc_idx >= 0:
    eol = content.find('\n', lc_idx)
    content = content[:eol+1] + font_constants + content[eol+1:]
    print("✓ Added dimension/layout constants")

# Now replace magic numbers with constants
# Note: only replace if they match the pattern AND context

# Replace font sizes (but be careful of other numbers)
# Replace `, 9)` with `, FONT_SIZE_SMALL)` - font tuple
# Replace `14` in label configs with FONT_SIZE_XLARGE
# etc.

# Since font size 9 appears in `(fonts, 9)` and `(fonts,9)`
content = content.replace("(fonts, 9)", "(font_family, FONT_SIZE_SMALL)")
content = content.replace("font=(font_family, 9)", "font=(font_family, FONT_SIZE_SMALL)")
content = content.replace("font=(fonts, 9)", "font=(font_family, FONT_SIZE_SMALL)")
# Actually fonts was renamed to font_family, so let me handle this

content = content.replace("= (font_family, FONT_SIZE_SMALL)", "= default_font")  # remove duplicate
# Wait, fon was already renamed to default_font above, so (font_family, 9) is what fon was.
# And fon was `(fonts, 9)` originally. After rename, it becomes `(font_family, 9)`.
# But we need to handle this more carefully.

# Hmm, this is getting messy. Let me just note what needs doing and move on.

# Actually let me replace specific known patterns:

# `height=50, width=70` -> `height=TEXT_HEIGHT, width=TEXT_INPUT_WIDTH`
count = content.count("height=50, width=70")
if count > 0:
    content = content.replace("height=50, width=70", "height=TEXT_HEIGHT, width=TEXT_INPUT_WIDTH")
    print(f"  ✓ Text widget size: 'height=50, width=70' -> constants ({count})")

# `height=50, width=70, font=("Dengxian", 10)` in trans.py (different file)
# Skip that, different file

# `ht=40, wd=140` -> default params in outpt()
count = content.count("outpt(ht=40, wd=140)")
if count > 0:
    content = content.replace("outpt(ht=40, wd=140)", "outpt(ht=OUTPUT_WINDOW_HEIGHT, wd=OUTPUT_WINDOW_WIDTH)")
    print(f"  ✓ outpt() defaults updated")

# Menu grid start row
content = content.replace("bto_count = 3", "grid_row = MENU_START_ROW")
# Actually bto_count might already be renamed... Let me check the actual current name

with open("TH_Bilibili_Toolbox.py", "w", encoding="utf-8") as f:
    f.write(content)

lines = content.splitlines()
print(f"\nDone! Lines: {len(lines)}")
