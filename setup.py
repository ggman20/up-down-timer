import cx_Freeze
import sys


# base = None

# if sys.platform == 'win64':
#     base = "Win64GUI"

executables = [cx_Freeze.Executable("Counting_GUI_v1.py", icon = 'lion.ico')]

cx_Freeze.setup(
    name = "Counting_GUI_v1.py",
    options = {"build_exe": {"packages":["tkinter",'pygame','PIL','time','datetime','winsound'], "include_files":['lion.ico', 'littlelion.png', 'onepiece.mp3']}},
    version = "0.01",
    description = "Counting_GUI_v1.py",
    executables = executables
    )
