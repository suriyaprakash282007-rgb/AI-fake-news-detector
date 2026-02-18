@echo off
:: ============================================================
:: GPT-5.2 DETECTIVE - RUN WITHOUT VS CODE
:: ============================================================
:: This opens a NEW command window that runs independently!
:: You can close VS Code after running this.
:: ============================================================

echo.
echo  ============================================================
echo   GPT-5.2 DETECTIVE - INDEPENDENT SERVER STARTER
echo  ============================================================
echo.
echo   Starting server in a NEW window...
echo   You can close VS Code after this!
echo.

:: Start a completely new, independent command window
start "GPT-5.2 Detective Server" cmd /k "cd /d \"c:\Users\suriy\OneDrive\Documents\suriya prakash vs\fake_news_detector\" && echo Starting Flask Server... && start /B \"\" \"C:\Users\suriy\OneDrive\Documents\suriya prakash vs\CareerGuidanceChatbot\.venv\Scripts\python.exe\" app.py && timeout /t 5 /nobreak > nul && echo. && echo ============================================ && echo Flask server running on localhost:5000 && echo ============================================ && echo. && echo Starting Cloudflare Tunnel... && echo Look for your PUBLIC URL below: && echo. && \"C:\Program Files (x86)\cloudflared\cloudflared.exe\" tunnel --url http://localhost:5000"

echo.
echo   Server window opened!
echo   You can now close this window AND VS Code.
echo   The server will keep running in the other window.
echo.
timeout /t 5
exit
