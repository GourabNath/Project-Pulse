import time
import sys

def thinking_animation():
    messages = [
        "Thinking.",
        "Thinking..",
        "Thinking...",
    ]
    
    for msg in messages:
        sys.stdout.write("\r" + msg)
        sys.stdout.flush()
        time.sleep(1)
    
    # Clear line
    sys.stdout.write("\r" + " " * 50 + "\r")


def analyzing_animation():
    messages = [
        "Analyzing.",
        "Analyzing..",
        "Analyzing...",
    ]
    
    for msg in messages:
        sys.stdout.write("\r" + msg)
        sys.stdout.flush()
        time.sleep(1.2)
    
    # Clear line
    sys.stdout.write("\r" + " " * 50 + "\r")
