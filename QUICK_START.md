# 🚀 Quick Start Guide - AI Fake News Detector

## How to Access the Application

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Start the Server

```bash
python app.py
```

### Step 3: Open the Application

**Click or copy this link to open in your browser:**

👉 **http://localhost:5000** 👈

Or open your browser and navigate to: `http://localhost:5000`

---

## ✅ What You'll See

Once you open the link, you'll see:
- 🏠 The main dashboard with the AI Fake News Detector
- 🔐 Login/Signup options
- 🛡️ Security indicators showing the app is safe

---

## 📱 Features Available

- **Text Analysis** - Detect fake news in articles
- **Image Detection** - Analyze images for manipulation
- **Audio Detection** - Check audio files for deepfakes
- **Video Detection** - Verify video authenticity
- **User History** - Track your analysis history
- **Profile Management** - Manage your account

---

## 🔧 Troubleshooting

### Port Already in Use?
If you get an error that port 5000 is already in use:

```bash
# Kill the process using port 5000
# On Linux/Mac:
lsof -ti:5000 | xargs kill -9

# On Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

Then run `python app.py` again.

### Can't Access the Link?
Make sure:
1. The server is running (you should see "Starting Fake News Detector API...")
2. You're using the correct URL: http://localhost:5000
3. Your firewall isn't blocking the connection

---

## 🌐 Access from Other Devices

To access from another device on the same network:

1. Find your local IP address:
   ```bash
   # On Linux/Mac:
   hostname -I
   
   # On Windows:
   ipconfig
   ```

2. Use the IP address instead of localhost:
   ```
   http://YOUR_IP_ADDRESS:5000
   ```
   Example: `http://192.168.1.100:5000`

---

## 🚀 Public Access

To share your app with others over the internet, check out:
- **Deployment Guide**: See `DEPLOYMENT.md`
- **Quick Public URL**: Use `run_public.py` for a temporary public link

---

**Need Help?** Check the main README.md or HOW_TO_RUN.md for more details.
