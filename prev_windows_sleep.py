import ctypes, time

# https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate

try: 
    while True:      
        ctypes.windll.kernel32.SetThreadExecutionState(0x00000002)
        print("Press Ctrl+C to quit")
        time.sleep(1)        
except KeyboardInterrupt:
    print("Quitting")
