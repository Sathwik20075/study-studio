import os, sys, threading, time, webbrowser
from pathlib import Path
import uvicorn
os.environ.setdefault('MAX_UPLOAD_MB', '4000')
os.environ.setdefault('RATE_PER_MIN', '100000')
from backend.app import app

if getattr(sys, "frozen", False):  # let the app find ffmpeg.exe placed next to the .exe
    os.environ["PATH"] = str(Path(sys.executable).parent) + os.pathsep + os.environ.get("PATH", "")

def open_browser():
    time.sleep(1.5)
    webbrowser.open("http://127.0.0.1:8000")

if __name__ == "__main__":
    threading.Thread(target=open_browser, daemon=True).start()
    print("File Toolkit running at http://127.0.0.1:8000  (close this window to quit)")
    uvicorn.run(app, host="127.0.0.1", port=8000)
