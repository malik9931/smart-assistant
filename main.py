import tkinter as tk
from tkinter import scrolledtext
from intent_detector import detect_intent
from system_tasks import *
from llm_handler import ask_openai

# Main GUI Class
class SmartAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Assistant")
        self.root.geometry("600x500")

        self.input_label = tk.Label(root, text="Enter your command:")
        self.input_label.pack(pady=5)

        self.input_entry = tk.Entry(root, width=70)
        self.input_entry.pack(pady=5)

        self.send_button = tk.Button(root, text="Send", command=self.process_command)
        self.send_button.pack(pady=5)

        self.output_display = scrolledtext.ScrolledText(root, height=15, wrap=tk.WORD)
        self.output_display.pack(pady=5)

        self.status_label = tk.Label(root, text="Status: Ready", anchor="w")
        self.status_label.pack(fill=tk.X, padx=5, pady=5)

    def log(self, message):
        self.output_display.insert(tk.END, message + "\n")
        self.output_display.see(tk.END)

    def set_status(self, status):
        self.status_label.config(text=f"Status: {status}")

    def process_command(self):
        command = self.input_entry.get()
        self.log(f"> {command}")
        self.set_status("Processing...")

        intent = detect_intent(command)

        try:
            if intent == "googleSearch":
                query = command.split("for")[-1].strip()
                google_search(query)
                self.log("Opened Google Search")

            elif intent == "youtubeSearch":
                query = command.split("for")[-1].strip()
                youtube_search(query)
                self.log("Opened YouTube Search")

            elif intent == "screenShot":
                take_screenshot()
                self.log("Screenshot taken")

            elif intent == "lowerBrightness":
                decrease_brightness()
                self.log("Brightness decreased")

            elif intent == "higherBrightness":
                increase_brightness()
                self.log("Brightness increased")

            elif intent == "highVolume":
                increase_volume()
                self.log("Volume increased")

            elif intent == "lowVolume":
                decrease_volume()
                self.log("Volume decreased")

            elif intent == "startWordProject":
                open_word()
                self.log("Microsoft Word launched")

            elif intent == "downloadMusic":
                self.log("Music download not implemented yet.")

            else:
                response = ask_openai(command)
                self.log("AI: " + response)

        except Exception as e:
            self.log("Error: " + str(e))

        self.set_status("Ready")

# Run the App
if __name__ == '__main__':
    root = tk.Tk()
    app = SmartAssistantApp(root)
    root.mainloop()
