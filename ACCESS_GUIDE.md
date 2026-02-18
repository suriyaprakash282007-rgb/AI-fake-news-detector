# 🎯 Access the AI Fake News Detector - Multiple Options

Choose the method that works best for you:

---

## 🚀 Option 1: One-Click Launch (Easiest!)

**Use the universal launcher script:**

```bash
python start.py
```

This will:
- ✅ Start the server automatically
- ✅ Check if the port is available
- ✅ Open your browser automatically
- ✅ Show you the URL

---

## 🌐 Option 2: Manual Start + Browser Link

**Step 1:** Start the server
```bash
python app.py
```

**Step 2:** Open in your browser
- Click: [http://localhost:5000](http://localhost:5000)
- Or copy/paste: `http://localhost:5000`

---

## 🎨 Option 3: Visual Launcher Page

**Double-click or open this file in your browser:**
- `OPEN_APP.html`

This gives you a beautiful launch page with:
- Server status checker
- Big launch button
- Quick setup instructions
- URL display

---

## 📱 Option 4: Access from Mobile/Other Devices

**Step 1:** Find your computer's IP address
```bash
# On Linux/Mac:
hostname -I

# On Windows:
ipconfig
```

**Step 2:** On your mobile device, visit:
```
http://YOUR_IP_ADDRESS:5000
```
Example: `http://192.168.1.100:5000`

---

## 🌍 Option 5: Public Internet Access

Want to share with friends or access from anywhere?

**Use the public launcher:**
```bash
python run_public.py
```

This creates a temporary public HTTPS URL that works from anywhere!

---

## 📚 Need More Help?

Check these files for detailed instructions:
- `QUICK_START.md` - Quick start guide
- `README.md` - Full documentation
- `HOW_TO_RUN.md` - Detailed running instructions
- `DEPLOYMENT.md` - Deploy to cloud platforms

---

## 🔧 Troubleshooting

### "Port 5000 already in use"
```bash
# Kill the process on port 5000
lsof -ti:5000 | xargs kill -9  # Mac/Linux
```

### "Module not found" errors
```bash
pip install -r requirements.txt
```

### Can't access the link
Make sure:
1. Server is running (you see "Starting Fake News Detector API...")
2. Using correct URL: http://localhost:5000
3. Firewall isn't blocking port 5000

---

**Choose any option above and start detecting fake news! 🛡️**
