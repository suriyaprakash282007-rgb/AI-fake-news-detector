' ============================================================
' GPT-5.2 DETECTIVE - SILENT BACKGROUND SERVER
' ============================================================
' Double-click this file to start the server!
' It will run in background even after VS Code is closed.
' ============================================================

Set WshShell = CreateObject("WScript.Shell")

' Get the script directory
scriptDir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)

' Show message
MsgBox "Starting GPT-5.2 Detective Server..." & vbCrLf & vbCrLf & _
       "1. Flask server will start in background" & vbCrLf & _
       "2. A window will open with your PUBLIC URL" & vbCrLf & vbCrLf & _
       "Keep that window open to keep the server running!", _
       vbInformation, "GPT-5.2 Detective"

' Change to project directory
WshShell.CurrentDirectory = scriptDir

' Start Flask in hidden window
WshShell.Run """C:\Users\suriy\OneDrive\Documents\suriya prakash vs\CareerGuidanceChatbot\.venv\Scripts\pythonw.exe"" """ & scriptDir & "\app.py""", 0, False

' Wait for Flask to start
WScript.Sleep 5000

' Start Cloudflare in visible window (so user can see the URL)
WshShell.Run """C:\Program Files (x86)\cloudflared\cloudflared.exe"" tunnel --url http://localhost:5000", 1, False

MsgBox "Server is starting!" & vbCrLf & vbCrLf & _
       "Look for the PUBLIC URL in the command window." & vbCrLf & _
       "The URL looks like: https://xxxxx.trycloudflare.com" & vbCrLf & vbCrLf & _
       "You can now close VS Code - the server will keep running!", _
       vbInformation, "GPT-5.2 Detective"
