import webbrowser
import pyautogui
import screen_brightness_control as sbc
import subprocess

# Open a Google search in browser
def google_search(query: str):
    webbrowser.open(f"https://www.google.com/search?q={query}")

# Open YouTube search
def youtube_search(query: str):
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

# Take screenshot and save it
def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")

# Brightness control

def increase_brightness():
    try:
        sbc.set_brightness("+10")
    except:
        pass

def decrease_brightness():
    try:
        sbc.set_brightness("-10")
    except:
        pass

# Volume control (simple example using Windows nircmd or pycaw if installed)
def increase_volume():
    subprocess.call(["nircmd.exe", "changesysvolume", "2000"])

def decrease_volume():
    subprocess.call(["nircmd.exe", "changesysvolume", "-2000"])

# Open Microsoft Word

def open_word():
    try:
        subprocess.Popen(["start", "winword"], shell=True)
    except FileNotFoundError:
        raise Exception("Microsoft Word not found.")
