@echo off
:: ============================================================
:: GPT-5.2 DETECTIVE - STANDALONE SERVER
:: This runs COMPLETELY INDEPENDENT of VS Code!
:: ============================================================

:: Hide this window and run everything in background
if "%1"=="HIDDEN" goto :RUN_HIDDEN

:: First run - launch hidden version
start /MIN cmd /c "%~f0" HIDDEN
exit

:RUN_HIDDEN
title GPT-5.2 Detective Server (Running)
cd /d "c:\Users\suriy\OneDrive\Documents\suriya prakash vs\fake_news_detector"

:: Kill any existing processes on port 5000
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :5000 ^| findstr LISTENING') do taskkill /F /PID %%a 2>nul

:: Start Flask server
start /B "Flask" "C:\Users\suriy\OneDrive\Documents\suriya prakash vs\CareerGuidanceChatbot\.venv\Scripts\python.exe" app.py

:: Wait for Flask to start
timeout /t 5 /nobreak > nul

:: Start Cloudflare tunnel and keep window open
echo.
echo ============================================================
echo   GPT-5.2 DETECTIVE SERVER IS RUNNING!
echo ============================================================
echo.
echo   Waiting for public URL...
echo.

"C:\Program Files (x86)\cloudflared\cloudflared.exe" tunnel --url http://localhost:5000

pause
