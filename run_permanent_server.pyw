"""
===============================================================================
GPT-5.2 DETECTIVE - PERMANENT SERVER LAUNCHER
===============================================================================
This script runs the Fake News Detector server permanently.
It can run even after VS Code is closed!

HOW TO USE:
1. Double-click this file OR
2. Right-click -> "Run with Python" OR
3. Add to Windows Startup for auto-start on boot

The server will run in the background and give you a public HTTPS URL.
===============================================================================
"""

import subprocess
import sys
import os
import time
import threading
import webbrowser

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_PATH = r"C:\Users\suriy\OneDrive\Documents\suriya prakash vs\CareerGuidanceChatbot\.venv\Scripts\python.exe"
CLOUDFLARED_PATH = r"C:\Program Files (x86)\cloudflared\cloudflared.exe"
APP_FILE = os.path.join(SCRIPT_DIR, "app.py")

def print_banner():
    print("\n" + "=" * 60)
    print("🛡️  GPT-5.2 DETECTIVE - AI FAKE NEWS DETECTOR")
    print("   Permanent Server Launcher")
    print("=" * 60)

def start_flask_server():
    """Start Flask server in background"""
    print("\n🚀 Starting Flask Server...")
    
    # Change to script directory
    os.chdir(SCRIPT_DIR)
    
    # Start Flask
    flask_process = subprocess.Popen(
        [PYTHON_PATH, APP_FILE],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
    )
    
    # Wait a bit for server to start
    time.sleep(3)
    
    if flask_process.poll() is None:
        print("   ✅ Flask Server is running on port 5000")
        return flask_process
    else:
        print("   ❌ Flask Server failed to start")
        return None

def start_cloudflare_tunnel():
    """Start Cloudflare tunnel for public HTTPS URL"""
    print("\n🌐 Starting Cloudflare Tunnel...")
    print("   Please wait for your public URL...\n")
    
    # Start cloudflared
    tunnel_process = subprocess.Popen(
        [CLOUDFLARED_PATH, "tunnel", "--url", "http://localhost:5000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    
    # Read output to find the URL
    public_url = None
    for line in iter(tunnel_process.stdout.readline, ''):
        print(f"   {line.strip()}")
        
        # Look for the tunnel URL
        if 'trycloudflare.com' in line.lower():
            import re
            urls = re.findall(r'https://[^\s|]+', line)
            if urls:
                public_url = urls[0].strip('|').strip()
                
                print("\n" + "=" * 60)
                print("🎉 SUCCESS! YOUR WEBSITE IS NOW LIVE!")
                print("=" * 60)
                print(f"\n🔗 PUBLIC SECURE URL:")
                print(f"   {public_url}")
                print("\n📱 Share this URL - Works on any device!")
                print("   ✓ Mobile, PC, Mac, Tablet")
                print("   ✓ Any WiFi or Internet connection")
                print("   ✓ HTTPS Secure (🔒 Padlock)")
                print("\n" + "=" * 60)
                print("⚠️  KEEP THIS WINDOW OPEN to keep the server running!")
                print("   Press Ctrl+C to stop the server")
                print("=" * 60 + "\n")
                
                # Open in browser
                webbrowser.open(public_url)
    
    return tunnel_process

def main():
    print_banner()
    
    # Check if required files exist
    if not os.path.exists(PYTHON_PATH):
        print(f"❌ Python not found at: {PYTHON_PATH}")
        input("Press Enter to exit...")
        sys.exit(1)
    
    if not os.path.exists(CLOUDFLARED_PATH):
        print(f"❌ Cloudflared not found at: {CLOUDFLARED_PATH}")
        input("Press Enter to exit...")
        sys.exit(1)
    
    if not os.path.exists(APP_FILE):
        print(f"❌ App file not found at: {APP_FILE}")
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Start Flask server
    flask_proc = start_flask_server()
    if flask_proc is None:
        input("Press Enter to exit...")
        sys.exit(1)
    
    try:
        # Start Cloudflare tunnel (this blocks and shows output)
        tunnel_proc = start_cloudflare_tunnel()
        
        # Wait for tunnel to finish (Ctrl+C to stop)
        tunnel_proc.wait()
        
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down server...")
    finally:
        # Cleanup
        if flask_proc:
            flask_proc.terminate()
        print("✅ Server stopped. Goodbye!")

if __name__ == "__main__":
    main()
