# 🌐 Deployment Guide - Make Your Website Accessible Worldwide

This guide shows you how to make your **AI Fake News Detector** accessible from any device (mobile, PC, Mac) anywhere in the world.

---

## 🚀 Option 1: Quick Public URL (ngrok) - Recommended for Testing

### Step 1: Sign up for ngrok (FREE)
1. Go to: https://dashboard.ngrok.com/signup
2. Create a free account
3. Go to: https://dashboard.ngrok.com/get-started/your-authtoken
4. Copy your authtoken

### Step 2: Configure ngrok
Open PowerShell and run:
```powershell
# Replace YOUR_TOKEN with your actual authtoken
C:\Users\suriy\AppData\Local\Microsoft\WinGet\Packages\Ngrok.Ngrok_Microsoft.Winget.Source_8wekyb3d8bbwe\ngrok.exe config add-authtoken YOUR_TOKEN
```

### Step 3: Start Public Server
```powershell
cd "c:\Users\suriy\OneDrive\Documents\suriya prakash vs\fake_news_detector"
python run_public.py
```

You'll get a URL like: `https://xxxx-xx-xx-xxx-xx.ngrok-free.app`

Share this URL with anyone! ✅

---

## 🌍 Option 2: Permanent Free Hosting (Render.com) - Recommended for Production

### Step 1: Create GitHub Repository
```powershell
cd "c:\Users\suriy\OneDrive\Documents\suriya prakash vs\fake_news_detector"
git init
git add .
git commit -m "Initial commit - AI Fake News Detector"
```

### Step 2: Push to GitHub
1. Go to https://github.com/new
2. Create a new repository named `fake-news-detector`
3. Run:
```powershell
git remote add origin https://github.com/YOUR_USERNAME/fake-news-detector.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Render
1. Go to: https://render.com (sign up with GitHub - FREE)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: fake-news-detector
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt && python train_advanced_model.py`
   - **Start Command**: `gunicorn app:app`
5. Click "Create Web Service"

Your permanent URL will be: `https://fake-news-detector.onrender.com` ✅

---

## ☁️ Option 3: Railway.app (Easy & Fast)

1. Go to: https://railway.app
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. It auto-detects Python and deploys!

Your URL: `https://fake-news-detector.up.railway.app` ✅

---

## 🐍 Option 4: PythonAnywhere (Free Python Hosting)

1. Go to: https://www.pythonanywhere.com
2. Create a free account
3. Go to "Web" tab → "Add a new web app"
4. Choose "Flask" and Python 3.10
5. Upload your files or clone from GitHub
6. Set the WSGI file path to your app

Your URL: `https://yourusername.pythonanywhere.com` ✅

---

## 📱 Testing on Mobile Devices

### Same WiFi Network (No deployment needed):
1. Find your PC's IP address:
```powershell
ipconfig | findstr /i "IPv4"
```
2. Start Flask: `python app.py`
3. On mobile, go to: `http://YOUR_IP:5000`

Example: `http://192.168.1.100:5000`

---

## 📋 Files Ready for Deployment

Your project already has these deployment files:

| File | Purpose |
|------|---------|
| `Procfile` | Heroku/Render deployment |
| `render.yaml` | Render.com auto-config |
| `runtime.txt` | Python version |
| `requirements.txt` | Dependencies |
| `.gitignore` | Git ignore rules |

---

## 🔧 Troubleshooting

### "Port already in use"
```powershell
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Models not loading on cloud
Make sure `train_advanced_model.py` runs in the build command.

### CORS errors
Already handled! Flask-CORS is configured.

---

## 🎉 Summary

| Method | Speed | Permanence | Best For |
|--------|-------|------------|----------|
| ngrok | ⚡ Instant | Temporary | Testing, demos |
| Render | 5 min | Permanent & Free | Production |
| Railway | 3 min | Permanent | Quick deploy |
| PythonAnywhere | 10 min | Permanent & Free | Learning |

---

**Need help?** The project is ready to deploy - just follow the steps above!
