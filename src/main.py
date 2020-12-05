import ctypes
import sys

from src.domain.difficulty import Difficulty
from src.Minesweeper import Minesweeper

if sys.platform.startswith('win'):
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("minesweeper")

minesweeper = Minesweeper(Difficulty.EASY)
