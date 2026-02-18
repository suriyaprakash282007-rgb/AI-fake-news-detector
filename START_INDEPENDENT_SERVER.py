import subprocess
import sys
import os
import time
import re

"""
===============================================================================
GPT-5.2 DETECTIVE - INDEPENDENT SERVER LAUNCHER
===============================================================================
This script runs the website COMPLETELY INDEPENDENT of VS Code!

HOW TO USE:
1. Double-click this file from Windows Explorer
2. The server will start in its own window
3. Close VS Code - the server keeps running!
4. Copy the public URL and share with anyone

The server runs until you close the server window.
===============================================================================
"""

# Paths
SCRIPT_DIR = r"c:\Users\suriy\OneDrive\Documents\suriya prakash vs\fake_news_detector"
PYTHON_EXE = r"C:\Users\suriy\OneDrive\Documents\suriya prakash vs\CareerGuidanceChatbot\.venv\Scripts\python.exe"
CLOUDFLARED = r"C:\Program Files (x86)\cloudflared\cloudflared.exe"

def main():
    os.chdir(SCRIPT_DIR)
    
    print("=" * 60)
    print("🛡️  GPT-5.2 DETECTIVE - STARTING SERVER")
    print("=" * 60)
    print("\nThis window will keep the server running.")
    print("You can close VS Code - the server will continue!\n")
    
    # Start Flask server in background
    print("🚀 Starting Flask server...")
    flask_proc = subprocess.Popen(
        [PYTHON_EXE, "app.py"],
        cwd=SCRIPT_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    time.sleep(4)
    
    if flask_proc.poll() is not None:
        print("❌ Flask failed to start!")
        input("Press Enter to exit...")
        return
    
    print("✅ Flask server running on localhost:5000\n")
    
    # Start Cloudflare tunnel
    print("🌐 Starting Cloudflare tunnel...")
    print("   Waiting for public URL...\n")
    print("-" * 60)
    
    tunnel_proc = subprocess.Popen(
        [CLOUDFLARED, "tunnel", "--url", "http://localhost:5000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    
    try:
        for line in iter(tunnel_proc.stdout.readline, ''):
            # Look for the URL
            if 'trycloudflare.com' in line.lower():
                urls = re.findall(r'https://[^\s|]+', line)
                if urls:
                    url = urls[0].strip('|').strip()
                    print("\n" + "=" * 60)
                    print("🎉 SUCCESS! YOUR WEBSITE IS LIVE!")
                    print("=" * 60)
                    print(f"\n🔗 PUBLIC URL: {url}\n")
                    print("📱 Share this URL - works on ANY device!")
                    print("🔒 HTTPS Secure - Green padlock enabled!")
                    print("\n" + "=" * 60)
                    print("⚠️  KEEP THIS WINDOW OPEN!")
                    print("   You can close VS Code - server keeps running!")
                    print("   Press Ctrl+C to stop the server.")
                    print("=" * 60 + "\n")
            elif 'INF' in line:
                print(f"   {line.strip()}")
                
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down...")
    finally:
        flask_proc.terminate()
        tunnel_proc.terminate()
        print("✅ Server stopped.")

if __name__ == "__main__":
    main()
    input("\nPress Enter to close...")
