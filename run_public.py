"""
🌐 PUBLIC DEPLOYMENT SCRIPT
Run this file to make your Fake News Detector accessible from ANY device worldwide!

This script will:
1. Start the Flask server
2. Create a public tunnel using ngrok
3. Give you a URL you can share with anyone

FIRST TIME SETUP:
1. Go to https://dashboard.ngrok.com/signup (FREE)
2. Get your authtoken from: https://dashboard.ngrok.com/get-started/your-authtoken
3. Run: ngrok config add-authtoken YOUR_TOKEN_HERE
4. Then run this script!
"""

import subprocess
import sys
import os
import time
import threading
import webbrowser

# Change to script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def start_flask():
    """Start the Flask server"""
    print("🚀 Starting Flask server...")
    subprocess.run([sys.executable, "app.py"])

def start_ngrok():
    """Start ngrok tunnel"""
    time.sleep(3)  # Wait for Flask to start
    
    try:
        from pyngrok import ngrok
        
        # Create tunnel
        print("\n🌐 Creating public tunnel...")
        public_url = ngrok.connect(5000)
        
        print("\n" + "=" * 60)
        print("✅ YOUR WEBSITE IS NOW LIVE!")
        print("=" * 60)
        print(f"\n🔗 PUBLIC URL: {public_url}")
        print(f"\n📱 Share this link to access from ANY device:")
        print(f"   - Mobile phones (iOS/Android)")
        print(f"   - Tablets")
        print(f"   - Other computers (PC/Mac/Linux)")
        print(f"   - Anywhere with internet!")
        print("\n" + "=" * 60)
        print("⚠️  Keep this terminal open to keep the website running")
        print("    Press Ctrl+C to stop the server")
        print("=" * 60)
        
        # Open in browser
        webbrowser.open(str(public_url))
        
        # Keep running
        ngrok_process = ngrok.get_ngrok_process()
        ngrok_process.proc.wait()
        
    except Exception as e:
        print(f"\n❌ Ngrok Error: {e}")
        print("\n📝 MANUAL SETUP REQUIRED:")
        print("1. Sign up at: https://dashboard.ngrok.com/signup (FREE)")
        print("2. Get your authtoken from: https://dashboard.ngrok.com/get-started/your-authtoken")
        print("3. Run this command:")
        print("   ngrok config add-authtoken YOUR_TOKEN_HERE")
        print("4. Then run this script again!")
        print("\n🔄 ALTERNATIVE: Use the local URL for now:")
        print("   http://localhost:5000")
        print("   (Only accessible on THIS computer)")

if __name__ == "__main__":
    print("=" * 60)
    print("🌐 GPT-5.2-Codex FAKE NEWS DETECTOR - PUBLIC DEPLOYMENT")
    print("=" * 60)
    
    # Check if models exist
    if not os.path.exists("fake_news_model.pkl"):
        print("⚠️  ML models not found. Training now...")
        subprocess.run([sys.executable, "train_advanced_model.py"])
    
    # Start Flask in a thread
    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()
    
    # Start ngrok
    start_ngrok()
