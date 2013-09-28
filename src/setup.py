# exe file for windows

import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], 'init_script':'Console', "excludes": ["tkinter"]}

data_files=[
	'msvcp90.dll',
    'msvcr90.dll',
    'gdiplus.dll',
    'msvcm90.dll',
    'loli_exhentai.py',
    'loli_gelbooru.py',
    'loli_spam.py'
    ]

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "guifoo",
        version = "0.1",
        description = "Loli.",
        options = {"build_exe": build_exe_options},
        executables = [Executable("loli_gelbooru.py", base=base )])