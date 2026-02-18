"""
===============================================================================
CREATE DESKTOP SHORTCUT
===============================================================================
This script creates a shortcut on your Desktop to easily start the
Fake News Detector server anytime - no VS Code needed!
===============================================================================
"""

import os
import sys

try:
    import winshell
    from win32com.client import Dispatch
except ImportError:
    print("Installing required packages...")
    os.system(f'"{sys.executable}" -m pip install pywin32 winshell')
    import winshell
    from win32com.client import Dispatch

def create_desktop_shortcut():
    """Create a desktop shortcut for the server"""
    
    # Paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    batch_file = os.path.join(script_dir, "CLICK_TO_START.bat")
    desktop = winshell.desktop()
    shortcut_path = os.path.join(desktop, "GPT-5.2 Detective.lnk")
    
    # Create shortcut
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = batch_file
    shortcut.WorkingDirectory = script_dir
    shortcut.IconLocation = "C:\\Windows\\System32\\shell32.dll,13"  # Shield icon
    shortcut.Description = "Start GPT-5.2 Detective - AI Fake News Detector"
    shortcut.save()
    
    print("=" * 60)
    print("✅ DESKTOP SHORTCUT CREATED!")
    print("=" * 60)
    print(f"\nShortcut location: {shortcut_path}")
    print("\nYou can now:")
    print("  1. Close VS Code completely")
    print("  2. Double-click 'GPT-5.2 Detective' on your Desktop")
    print("  3. Your server will start and give you a public URL!")
    print("=" * 60)

if __name__ == "__main__":
    print("\n🛡️ Creating Desktop Shortcut for GPT-5.2 Detective...\n")
    try:
        create_desktop_shortcut()
    except Exception as e:
        print(f"Error: {e}")
        print("\nAlternative: Manually create shortcut to CLICK_TO_START.bat")
    
    input("\nPress Enter to close...")
