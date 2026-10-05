@echo off
cd /d "%~dp0"
where python >nul 2>nul || (echo Python is not installed. Install it from https://www.python.org/downloads/ and tick "Add python.exe to PATH", then run this again. & pause & exit /b)
where ffmpeg >nul 2>nul || (echo Installing ffmpeg... & winget install -e --id Gyan.FFmpeg --accept-source-agreements --accept-package-agreements & echo Close this window and run start.bat again so ffmpeg is detected. & pause & exit /b)
if not exist .venv (python -m venv .venv)
call .venv\Scripts\activate
pip install -q -r requirements.txt
rem Optional for Word/Excel/PowerPoint conversion: winget install TheDocumentFoundation.LibreOffice
python launcher.py
pause
