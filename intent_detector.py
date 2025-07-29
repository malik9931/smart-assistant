def detect_intent(command: str) -> str:
    command = command.lower()

    if "search" in command and "google" in command:
        return "googleSearch"
    elif "youtube" in command:
        return "youtubeSearch"
    elif "screenshot" in command:
        return "screenShot"
    elif "brightness" in command:
        if "lower" in command:
            return "lowerBrightness"
        elif "increase" in command or "higher" in command:
            return "higherBrightness"
    elif "volume" in command:
        if "high" in command or "increase" in command:
            return "highVolume"
        elif "low" in command or "decrease" in command:
            return "lowVolume"
    elif "word" in command:
        return "startWordProject"
    elif "download music" in command:
        return "downloadMusic"
    else:
        return "askLLM"
