"""
🌐 Secure Public Server for AI Fake News Detector
=================================================
This script runs your website with a FREE HTTPS public URL
accessible from ANY device worldwide (mobile, PC, Mac, etc.)

NO SIGNUP REQUIRED - Uses Cloudflare Tunnel (Argo)

Features:
- ✅ HTTPS Secure Connection (padlock icon in browser)
- ✅ Works from any WiFi/Internet worldwide
- ✅ Accessible from Mobile, PC, Mac, any device
- ✅ FREE - No payment required
- ✅ No registration/signup needed
"""

import subprocess
import sys
import time
import threading
import webbrowser

def run_flask():
    """Run Flask server"""
    print("\n🚀 Starting Flask Server...")
    subprocess.run([
        sys.executable, 
        "app.py"
    ])

def run_cloudflare_tunnel():
    """Run Cloudflare Tunnel for public HTTPS URL"""
    time.sleep(3)  # Wait for Flask to start
    
    print("\n🌐 Starting Cloudflare Tunnel...")
    print("=" * 60)
    print("⏳ Creating secure HTTPS public URL...")
    print("=" * 60)
    
    try:
        from flask_cloudflared import run_with_cloudflared
        # This will print the public URL
        process = subprocess.Popen(
            ["cloudflared", "tunnel", "--url", "http://localhost:5000"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        public_url = None
        for line in iter(process.stdout.readline, ''):
            print(line, end='')
            if 'trycloudflare.com' in line.lower() or '.cloudflare' in line.lower():
                # Extract URL
                import re
                urls = re.findall(r'https://[^\s]+', line)
                if urls:
                    public_url = urls[0]
                    print("\n" + "=" * 60)
                    print("✅ YOUR SECURE PUBLIC URL (HTTPS):")
                    print(f"🔗 {public_url}")
                    print("=" * 60)
                    print("\n📱 Share this URL with anyone!")
                    print("   Works on: Mobile, PC, Mac, Any Device")
                    print("   Works on: Any WiFi, Any Internet Connection")
                    print("   🔒 SECURE: Has HTTPS padlock")
                    print("\n⚠️  Keep this terminal open to keep the URL active")
                    print("=" * 60)
                    
    except Exception as e:
        print(f"Error: {e}")
        print("\nTrying alternative method...")

if __name__ == "__main__":
    print("=" * 60)
    print("🛡️  AI FAKE NEWS DETECTOR - SECURE PUBLIC SERVER")
    print("   Powered by GPT-5.2-Codex")
    print("=" * 60)
    
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    # Run cloudflare tunnel in main thread
    run_cloudflare_tunnel()
