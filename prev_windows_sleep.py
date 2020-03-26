import ctypes, time

print("Press Ctrl+C to quit")
# https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate
ctypes.windll.kernel32.SetThreadExecutionState(0x00000002)
try: 
    while True:        
        time.sleep(1)        
except KeyboardInterrupt:
    print("Quitting")
