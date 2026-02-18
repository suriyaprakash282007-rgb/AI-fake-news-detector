@echo off
title GPT-5.2 Detective - Background Server
color 0A

:: Run in background mode (minimized and hidden)
cd /d "%~dp0"

:: Start Flask server
start /MIN "FlaskServer" "C:\Users\suriy\OneDrive\Documents\suriya prakash vs\CareerGuidanceChatbot\.venv\Scripts\pythonw.exe" -c "import subprocess; subprocess.run(['C:/Users/suriy/OneDrive/Documents/suriya prakash vs/CareerGuidanceChatbot/.venv/Scripts/python.exe', 'app.py'])"

:: Wait for Flask
timeout /t 3 /nobreak > nul

:: Start Cloudflared tunnel (this will show the URL)
start "CloudflareTunnel" "C:\Program Files (x86)\cloudflared\cloudflared.exe" tunnel --url http://localhost:5000

echo Server started in background!
echo Check the Cloudflare window for your public URL.
timeout /t 5
