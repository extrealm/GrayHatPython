from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        pass
    
    def load(self, path_to_exe):
        creation_flags = DEBUG_PROCESS
        
        si = STARTUPINFO()
        pi = PROCESS_INFORMATION()
        
        si.dwFlags      = 0x1;
        si.wShowWindow  = 1;
        
        si.cb = sizeof(si)
        
        if kernel32.CreateProcessA(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   None,
                                   creation_flags,
                                   None,
                                   None,
                                   byref(si),
                                   byref(pi)):
            print("test")
        else:
            print("[*] Error: 0x%08x." % kernel32.GetLastError())
