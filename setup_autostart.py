"""
===============================================================================
ADD TO WINDOWS STARTUP
===============================================================================
This script adds the Fake News Detector server to Windows Startup
so it runs automatically when you turn on your computer!

Run this ONCE to set up auto-start.
===============================================================================
"""

import os
import sys
import winreg

def add_to_startup():
    """Add the server to Windows startup"""
    
    # Paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    batch_file = os.path.join(script_dir, "START_SERVER.bat")
    
    # Registry key for startup
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    app_name = "GPT52Detective"
    
    try:
        # Open registry key
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        
        # Add the startup entry
        winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, f'"{batch_file}"')
        
        winreg.CloseKey(key)
        
        print("=" * 60)
        print("✅ SUCCESS! Server added to Windows Startup!")
        print("=" * 60)
        print("\nThe Fake News Detector will now start automatically")
        print("every time you turn on your computer!")
        print("\nTo remove from startup, run: remove_from_startup.py")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nTry running this script as Administrator.")

def remove_from_startup():
    """Remove from Windows startup"""
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    app_name = "GPT52Detective"
    
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(key, app_name)
        winreg.CloseKey(key)
        print("✅ Removed from Windows Startup!")
    except FileNotFoundError:
        print("ℹ️ Not in startup (already removed)")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🛡️  GPT-5.2 DETECTIVE - STARTUP MANAGER")
    print("=" * 60)
    print("\nOptions:")
    print("1. Add to Windows Startup (auto-start on boot)")
    print("2. Remove from Windows Startup")
    print("3. Exit")
    
    choice = input("\nEnter choice (1/2/3): ").strip()
    
    if choice == "1":
        add_to_startup()
    elif choice == "2":
        remove_from_startup()
    else:
        print("Exiting...")
    
    input("\nPress Enter to close...")
