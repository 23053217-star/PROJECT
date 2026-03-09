import psutil

# List of known/suspicious keylogger process names
suspicious_processes = [
    "keylogger.exe",
    "winlogon.exe",  # example, normally a system process, be careful
    "kl.exe",
    "spybot.exe",
    "perfectkeylogger.exe"
]

def detect_keylogger():
    detected = []
    for proc in psutil.process_iter(['name']):
        try:
            process_name = proc.info['name'].lower()
            if process_name in suspicious_processes:
                detected.append(process_name)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    if detected:
        print("Potential keylogger(s) detected:", ', '.join(detected))
    else:
        print("No keylogger processes detected.")

if __name__ == "__main__":
    detect_keylogger()
