import cx_Freeze
import sys

import numpy
import cv2

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Counting_GUI_v1.py", base = base, icon = 'lion.ico')]

cx_Freeze.setup(
    name = "Counting_GUI_v1.py",
    options = {"build_exe": {"packages":["tkinter",'pygame','PIL','time','datetime','winsound'], "include_files":['lion.ico', 'littlelion.png', 'onepiece.mp3']}},
    version = "0.01",
    description = "Counting_GUI_v1.py",
    executables = executables
    )
