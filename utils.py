def log_action(action, result):
    with open("log.txt", "a") as f:
        f.write(f"[{datetime.now()}] Action: {action}, Result: {result}\n")
