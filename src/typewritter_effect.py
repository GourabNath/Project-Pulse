
import time
from IPython.display import display, Markdown, clear_output


import time
import sys

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
