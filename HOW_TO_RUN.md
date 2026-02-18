# 🛡️ GPT-5.2 Detective - AI Fake News Detector

## Running the Server WITHOUT VS Code

You can run this website permanently, even after closing VS Code!

---

## 🚀 Quick Start (Easiest Method)

### Option 1: Double-Click to Start
1. Close VS Code (if you want)
2. Go to the `fake_news_detector` folder
3. **Double-click `CLICK_TO_START.bat`**
4. Wait for the public URL to appear
5. Share the URL with anyone!

---

## 📁 Available Launcher Files

| File | Description |
|------|-------------|
| `CLICK_TO_START.bat` | 🎯 **Recommended** - Simple one-click start |
| `START_SERVER.bat` | Alternative starter with more details |
| `START_BACKGROUND.bat` | Runs minimized in background |
| `run_permanent_server.pyw` | Python launcher (double-click to run) |

---

## 🔄 Auto-Start on Windows Boot

Want the server to start automatically when you turn on your computer?

1. Run `setup_autostart.py`
2. Choose option `1` to add to startup
3. Your server will now start every time Windows boots!

To remove: Run `setup_autostart.py` and choose option `2`

---

## 🖥️ Create Desktop Shortcut

1. Run `create_desktop_shortcut.py`
2. A shortcut will appear on your Desktop
3. Double-click it anytime to start the server!

---

## 📱 How It Works

1. **Flask Server** runs on `localhost:5000`
2. **Cloudflare Tunnel** creates a secure HTTPS public URL
3. The URL changes each time you restart (free tier limitation)
4. Anyone with the URL can access your website!

---

## ⚠️ Important Notes

- Keep the command window OPEN to keep the server running
- The public URL changes each time you restart
- For a permanent URL, consider deploying to Render.com or Railway.app
- HTTPS is automatically enabled (green padlock)

---

## 🔧 Troubleshooting

### Server won't start?
- Make sure no other server is running on port 5000
- Check that Python is installed correctly
- Run the .bat file as Administrator

### No public URL appearing?
- Wait 10-15 seconds for Cloudflare to connect
- Check your internet connection
- Try running `CLICK_TO_START.bat` again

### "Python not found" error?
- The path to Python may have changed
- Edit the .bat file and update the Python path

---

## 📞 Support

This is a student project powered by GPT-5.2-Codex.
For issues, check the error messages in the command window.

---

**Enjoy your AI Fake News Detector!** 🎉
