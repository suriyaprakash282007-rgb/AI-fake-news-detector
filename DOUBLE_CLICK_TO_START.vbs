' ============================================================
' GPT-5.2 DETECTIVE - START SERVER (Works without VS Code!)
' ============================================================
' 
' HOW TO USE:
' 1. Close VS Code completely
' 2. Double-click this file from Windows Explorer
' 3. Two windows will open - keep them open!
' 4. Look for your PUBLIC URL in the second window
'
' ============================================================

Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Get script directory
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)
pythonExe = "C:\Users\suriy\OneDrive\Documents\suriya prakash vs\CareerGuidanceChatbot\.venv\Scripts\python.exe"
cloudflaredExe = "C:\Program Files (x86)\cloudflared\cloudflared.exe"
appFile = scriptDir & "\app.py"

' Create batch file for Flask server
Set flaskBatch = fso.CreateTextFile(scriptDir & "\temp_flask.bat", True)
flaskBatch.WriteLine "@echo off"
flaskBatch.WriteLine "title GPT-5.2 Detective - Flask Server"
flaskBatch.WriteLine "color 0A"
flaskBatch.WriteLine "echo."
flaskBatch.WriteLine "echo  ============================================"
flaskBatch.WriteLine "echo   FLASK SERVER - Keep this window open!"
flaskBatch.WriteLine "echo  ============================================"
flaskBatch.WriteLine "echo."
flaskBatch.WriteLine "cd /d """ & scriptDir & """"
flaskBatch.WriteLine """" & pythonExe & """ """ & appFile & """"
flaskBatch.WriteLine "pause"
flaskBatch.Close

' Create batch file for Cloudflare tunnel
Set tunnelBatch = fso.CreateTextFile(scriptDir & "\temp_tunnel.bat", True)
tunnelBatch.WriteLine "@echo off"
tunnelBatch.WriteLine "title GPT-5.2 Detective - PUBLIC URL"
tunnelBatch.WriteLine "color 0B"
tunnelBatch.WriteLine "echo."
tunnelBatch.WriteLine "echo  ============================================"
tunnelBatch.WriteLine "echo   WAITING FOR PUBLIC URL..."
tunnelBatch.WriteLine "echo   Keep this window open!"
tunnelBatch.WriteLine "echo  ============================================"
tunnelBatch.WriteLine "echo."
tunnelBatch.WriteLine "timeout /t 5 /nobreak > nul"
tunnelBatch.WriteLine """" & cloudflaredExe & """ tunnel --url http://localhost:5000"
tunnelBatch.WriteLine "pause"
tunnelBatch.Close

' Show instructions
MsgBox "GPT-5.2 Detective Server" & vbCrLf & vbCrLf & _
       "Two windows will open:" & vbCrLf & _
       "1. Flask Server (green) - runs the website" & vbCrLf & _
       "2. Tunnel (blue) - shows your PUBLIC URL" & vbCrLf & vbCrLf & _
       "Keep BOTH windows open!" & vbCrLf & _
       "You can close VS Code after clicking OK.", _
       vbInformation, "Starting Server..."

' Start Flask server in new window
WshShell.Run """" & scriptDir & "\temp_flask.bat""", 1, False

' Wait then start tunnel in new window
WScript.Sleep 5000
WshShell.Run """" & scriptDir & "\temp_tunnel.bat""", 1, False

MsgBox "Server Started!" & vbCrLf & vbCrLf & _
       "Look for your URL in the BLUE window." & vbCrLf & _
       "It will look like: https://xxxxx.trycloudflare.com" & vbCrLf & vbCrLf & _
       "Share that URL with anyone!" & vbCrLf & _
       "Works on mobile, PC, Mac - anywhere!", _
       vbInformation, "Success!"
