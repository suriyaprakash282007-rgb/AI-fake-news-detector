"""
🔒 SECURE PUBLIC SERVER - AI FAKE NEWS DETECTOR
================================================
One-click solution to make your website:
✅ Accessible from ANYWHERE in the world
✅ HTTPS Secure (green padlock)
✅ Works on Mobile, PC, Mac, any device
✅ Works on any WiFi/Internet connection

INSTRUCTIONS:
1. Sign up FREE at: https://dashboard.ngrok.com/signup
2. Copy your authtoken from: https://dashboard.ngrok.com/get-started/your-authtoken
3. Paste your token below where it says YOUR_AUTHTOKEN_HERE
4. Run this script: python run_https_server.py
"""

import os
import sys
import threading
import time
import webbrowser

# ============================================
# STEP 1: SET YOUR NGROK AUTHTOKEN HERE
# ============================================
# Get your FREE token at: https://dashboard.ngrok.com/signup
NGROK_AUTH_TOKEN = "YOUR_AUTHTOKEN_HERE"  # <-- PASTE YOUR TOKEN HERE
# ============================================


def check_and_setup_ngrok():
    """Setup ngrok with authtoken"""
    try:
        from pyngrok import ngrok, conf
        
        if NGROK_AUTH_TOKEN == "YOUR_AUTHTOKEN_HERE":
            print("\n" + "=" * 70)
            print("❌ ERROR: You need to set your ngrok authtoken!")
            print("=" * 70)
            print("\n📋 QUICK SETUP (Takes 1 minute):")
            print("\n   1. Go to: https://dashboard.ngrok.com/signup")
            print("      (Click the link, signup is FREE)")
            print("\n   2. After signup, go to: https://dashboard.ngrok.com/get-started/your-authtoken")
            print("      (Copy your authtoken)")
            print("\n   3. Open this file: run_https_server.py")
            print("      Find the line: NGROK_AUTH_TOKEN = \"YOUR_AUTHTOKEN_HERE\"")
            print("      Replace YOUR_AUTHTOKEN_HERE with your token")
            print("\n   4. Run this script again!")
            print("\n" + "=" * 70)
            
            # Open signup page
            print("\n🌐 Opening ngrok signup page...")
            webbrowser.open("https://dashboard.ngrok.com/signup")
            return False
        
        # Set the authtoken
        conf.get_default().auth_token = NGROK_AUTH_TOKEN
        print("✅ ngrok authentication configured!")
        return True
        
    except ImportError:
        print("Installing pyngrok...")
        os.system(f"{sys.executable} -m pip install pyngrok")
        return check_and_setup_ngrok()


def run_flask_server():
    """Import and run the Flask app"""
    # Change to the correct directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Import the Flask app
    from app import app
    
    # Run without debug mode for production
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)


def start_public_tunnel():
    """Start ngrok tunnel to create public HTTPS URL"""
    from pyngrok import ngrok
    
    print("\n🌐 Creating secure public tunnel...")
    
    # Create HTTPS tunnel
    public_url = ngrok.connect(5000, bind_tls=True)
    
    print("\n" + "=" * 70)
    print("🎉 SUCCESS! YOUR WEBSITE IS NOW LIVE ON THE INTERNET!")
    print("=" * 70)
    print(f"\n🔗 PUBLIC SECURE URL (HTTPS):")
    print(f"   {public_url.public_url}")
    print("\n📱 SHARE THIS LINK - Works on:")
    print("   ✓ Any Mobile Phone (iPhone, Android)")
    print("   ✓ Any Computer (PC, Mac, Linux)")
    print("   ✓ Any Tablet (iPad, Android Tablet)")
    print("   ✓ Any WiFi or Internet Connection")
    print("\n🔒 SECURITY:")
    print("   ✓ HTTPS Enabled (Green Padlock)")
    print("   ✓ Encrypted Connection")
    print("   ✓ No 'Not Secure' Warning")
    print("\n" + "=" * 70)
    print("⚠️  KEEP THIS WINDOW OPEN to keep the URL active!")
    print("   Press Ctrl+C to stop the server")
    print("=" * 70)
    
    # Open in browser
    webbrowser.open(public_url.public_url)
    
    return public_url


if __name__ == "__main__":
    print("=" * 70)
    print("🛡️  AI FAKE NEWS DETECTOR - SECURE PUBLIC SERVER")
    print("   Powered by GPT-5.2-Codex")
    print("=" * 70)
    
    # Step 1: Check ngrok setup
    if not check_and_setup_ngrok():
        sys.exit(1)
    
    # Step 2: Start Flask in background thread
    print("\n🚀 Starting Flask server...")
    flask_thread = threading.Thread(target=run_flask_server, daemon=True)
    flask_thread.start()
    
    # Wait for Flask to start
    time.sleep(3)
    
    # Step 3: Start public tunnel
    try:
        public_url = start_public_tunnel()
        
        # Keep the script running
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down server...")
        from pyngrok import ngrok
        ngrok.kill()
        print("✅ Server stopped. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure your authtoken is correct!")
