import ctypes

print("Press Ctrl+C to quit")
try: 
    while True:        
        ctypes.windll.kernel32.SetThreadExecutionState(0x00000002)
except KeyboardInterrupt:
    print("Quitting")

# https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate



