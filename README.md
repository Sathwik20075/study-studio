# File Toolkit
Web app: convert (image/PDF/docs/video), compress, scanned-copy effect, crop, sticker maker, video trim.

## Run
Needs Python 3.10+, `ffmpeg`, and LibreOffice (`soffice`) for Word/Excel/PPT conversion.

    pip install -r requirements.txt
    uvicorn backend.app:app --reload      # open http://localhost:8000

Or: `docker build -t file-toolkit . && docker run -p 8000:8000 file-toolkit`

## Notes
- Sticker: draw around the object, or leave blank for auto cut-out (uses `rembg` if installed, else OpenCV GrabCut).
- Video trim: "fast" copies streams without re-encoding (quick, but cuts land on keyframes).
- Formats: JPG, PNG, WebP, BMP, TIFF, GIF, HEIC (input), PDF, DOC/DOCX/XLS/XLSX/PPT/PPTX/ODT/RTF/TXT, MP4/MOV/AVI/MKV/WebM.

## Windows PC
- Quick: double-click `start.bat` (needs Python; it installs ffmpeg and dependencies, then opens the app in your browser).
- Single download: push to GitHub, then create a Release (tag e.g. `v1.0`, any title) and publish it. After a few minutes `FileToolkit-Windows.zip` appears under the release's Assets (you can also run "Build Windows app" manually from the Actions tab and download it there) (contains `FileToolkit.exe` + `ffmpeg.exe`). Word/Excel/PPT conversion also needs LibreOffice installed.

## Phones (hosted)
Deploy the Dockerfile to a host (Render, Railway, Fly.io). Limits: env `MAX_UPLOAD_MB` (default 100) and `RATE_PER_MIN` (default 30 per IP).
The site is an installable PWA: Android Chrome -> menu -> Install app; iPhone Safari -> Share -> Add to Home Screen.
