@echo off
title GPT-5.2 Detective - Quick Start
mode con: cols=70 lines=30
color 0B

echo.
echo  ======================================================
echo   _____  _____ _____   _____  ___    ____       _   
echo  / ____|/ ____|  __ \ / ____|/ _ \  |___ \     | |  
echo ^| ^|  __^| ^|___ ^| ^|__) ^|^| ^|____^| ^| ^| ^|   __) ^|  __^| ^|_ 
echo ^| ^| ^|_ ^|  ___^||  ___/  \___ \^| ^| ^| ^|  ^|__ ^<  / _` __^|
echo ^| ^|__^| ^| ^|    ^| ^|     ____^) ^| ^|_^| ^|  ___) ^|^| ^|_ ^| ^|_ 
echo  \_____^|_^|    ^|_^|    ^|_____/ \___/  ^|____/  \__\__^|
echo.
echo           AI FAKE NEWS DETECTOR - SECURE SERVER
echo  ======================================================
echo.
echo   Starting your secure server...
echo   This works even after VS Code is closed!
echo.
echo  ======================================================
echo.

cd /d "c:\Users\suriy\OneDrive\Documents\suriya prakash vs\fake_news_detector"

echo  [Step 1/2] Starting Flask Server...
start /B /MIN "" "C:\Users\suriy\OneDrive\Documents\suriya prakash vs\CareerGuidanceChatbot\.venv\Scripts\python.exe" app.py
echo            Flask server starting...

timeout /t 4 /nobreak > nul
echo            Done!
echo.

echo  [Step 2/2] Creating Public HTTPS URL...
echo.
echo  ======================================================
echo   LOOK FOR YOUR URL BELOW (starts with https://)
echo  ======================================================
echo.

"C:\Program Files (x86)\cloudflared\cloudflared.exe" tunnel --url http://localhost:5000

echo.
echo  Server stopped.
pause
