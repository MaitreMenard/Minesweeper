import ctypes
import sys

from Minesweeper import Minesweeper

if sys.platform.startswith('win'):
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("minesweeper")

minesweeper = Minesweeper(9, 9, 10)
