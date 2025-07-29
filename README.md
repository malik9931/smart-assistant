# 🧠 Smart Assistant Desktop App

A desktop-based intelligent assistant built with Python and Tkinter. It understands natural language commands, performs useful system actions, and answers questions using a connected LLM (OpenAI or Gemini).

---

## ✨ Features

- Modern and simple GUI using Tkinter
- Natural language intent detection
- Execute system tasks such as:
  - Google and YouTube search
  - Taking screenshots
  - Adjusting brightness and volume
  - Launching Microsoft Word
- Fallback to AI (LLM) for general questions
- Displays status log with each user interaction
- Keeps a full log in `assistant_log.txt`

---

## 📁 Project Structure

```bash
.
├── main.py               # Main GUI application
├── intent_detector.py    # Handles intent detection
├── system_tasks.py       # Executes OS-level actions
├── llm_handler.py        # Communicates with OpenAI or Gemini
├── assistant_log.txt     # Local log of actions and responses
└── requirements.txt      # Required dependencies
```

🚀 How to Run
Install Python 3.8 or above.

Add your API key in llm_handler.py for either:

OpenAI (openai.api_key)

Google Gemini (genai.configure)

Install the dependencies:
pip install -r requirements.txt

Run the assistant:
python main.py

💬 Supported Commands
Intent	Example	Action Taken
googleSearch	"Search for the best laptops on Google"	Opens Google search tab
youtubeSearch	"Search for relaxing music on YouTube"	Opens YouTube search tab
screenShot	"Take a screenshot"	Saves screenshot
lowerBrightness	"Reduce screen brightness"	Decreases screen brightness
higherBrightness	"Increase brightness"	Increases screen brightness
highVolume	"Increase the volume"	Turns up system volume
lowVolume	"Turn down the volume"	Turns down system volume
startWordProject	"Start Word"	Opens Microsoft Word
downloadMusic	"Download music from ..."	Not implemented yet
Other Questions	"What is the capital of Japan?"	Answered by AI (LLM)

📝 Logging
All commands and responses are stored in:
assistant_log.txt
This is useful for debugging and reviewing assistant behavior.

🔒 Security Notes
No system-level destructive operations are allowed.

Review the code before enabling or deploying sensitive features.

Make sure your API key is kept secret and not pushed to public repositories.

📈 Roadmap (To Do)
Add voice input/output support

Integrate TTS (Text to Speech)

Add browser automation support

Smart app launcher (customizable apps)

📃 License
This project is open-source and provided under the MIT License.
