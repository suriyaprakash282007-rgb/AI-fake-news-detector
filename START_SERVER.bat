@echo off
title GPT-5.2 Detective - STANDALONE SERVER
color 0E
cls

echo.
echo  ===========================================================
echo    GPT-5.2 DETECTIVE - FAKE NEWS DETECTOR
echo    STANDALONE SERVER (Works WITHOUT VS Code!)
echo  ===========================================================
echo.
echo  INSTRUCTIONS:
echo  - You can CLOSE VS Code after starting this
echo  - Keep BOTH windows open to keep server running
echo  - Share the URL with anyone in the world!
echo.

set "PROJECT_DIR=%~dp0"
set "PYTHON=C:\Users\suriy\OneDrive\Documents\suriya prakash vs\CareerGuidanceChatbot\.venv\Scripts\python.exe"
set "CLOUDFLARED=C:\Program Files (x86)\cloudflared\cloudflared.exe"

cd /d "%PROJECT_DIR%"

echo  [1/3] Checking Python...
"%PYTHON%" --version
if %ERRORLEVEL% neq 0 (
    echo ERROR: Python not found!
    pause
    exit /b 1
)
echo.

echo  [2/3] Starting Flask Server in SEPARATE window...
echo        (Keep that green window open!)
start "GPT-5.2 Flask Server" cmd /k "color 0A & echo. & echo  ========================================== & echo   FLASK SERVER - KEEP THIS WINDOW OPEN! & echo  ========================================== & echo. & cd /d "%PROJECT_DIR%" & "%PYTHON%" app.py"

echo.
echo  [3/3] Waiting 5 seconds for Flask to initialize...
timeout /t 5 /nobreak > nul

echo.
echo  ===========================================================
echo    STARTING CLOUDFLARE TUNNEL - LOOK FOR YOUR URL!
echo    Your URL will look like: https://xxxxx.trycloudflare.com
echo    Share this URL with ANYONE to access your website!
echo  ===========================================================
echo.

"%CLOUDFLARED%" tunnel --url http://localhost:5000

pause
