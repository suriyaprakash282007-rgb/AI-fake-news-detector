#!/usr/bin/env python3
"""
Universal Launcher for AI Fake News Detector
Works on Windows, Mac, and Linux
"""

import os
import sys
import subprocess
import webbrowser
import time
import socket

def check_port_in_use(port=5000):
    """Check if a port is already in use"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', port))
    sock.close()
    return result == 0

def print_banner():
    """Print a nice banner"""
    print("\n" + "="*60)
    print("🛡️  AI FAKE NEWS DETECTOR")
    print("="*60)
    print()

def main():
    print_banner()
    
    # Check if port is already in use
    if check_port_in_use(5000):
        print("⚠️  WARNING: Port 5000 is already in use!")
        print("   The server might already be running.")
        print()
        response = input("Do you want to open the app in your browser anyway? (y/n): ")
        if response.lower() == 'y':
            print("\n🌐 Opening app in browser...")
            webbrowser.open('http://localhost:5000')
            print("✅ Done! Check your browser.")
        return
    
    print("📦 Starting the server...")
    print()
    
    # Start the Flask app in the background
    try:
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        app_path = os.path.join(script_dir, 'app.py')
        
        # Start the server
        if sys.platform == 'win32':
            # Windows: use START to run in background
            subprocess.Popen([sys.executable, app_path], 
                           creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            # Linux/Mac: use nohup
            subprocess.Popen([sys.executable, app_path],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
        
        print("✅ Server is starting...")
        print()
        print("⏳ Waiting for server to be ready...")
        
        # Wait for the server to start
        max_attempts = 30
        for i in range(max_attempts):
            time.sleep(1)
            if check_port_in_use(5000):
                print("✅ Server is ready!")
                print()
                break
        else:
            print("⚠️  Server took too long to start.")
            print("   Please check for errors and try running: python app.py")
            return
        
        # Open the browser
        print("🌐 Opening app in your browser...")
        print()
        print("="*60)
        print("📍 APP URL: http://localhost:5000")
        print("="*60)
        print()
        
        webbrowser.open('http://localhost:5000')
        
        print("✅ Success! The app should open in your browser.")
        print()
        print("💡 TIP: Keep this window open while using the app.")
        print("   Press Ctrl+C to stop the server.")
        print()
        
        # Keep the script running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n⏹️  Shutting down server...")
            print("✅ Server stopped. Goodbye!")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print()
        print("Please try running manually: python app.py")

if __name__ == '__main__':
    main()
