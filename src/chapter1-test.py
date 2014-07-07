from ctypes import *
libc = cdll.msvcrt
msg = "test"
libc.printf(msg);