
from src.engines.utils.typewriter import stream_markdown
def print_multiple_lines(texts):
    for t in texts:
      stream_markdown(t)
