
def print_multiple_lines(texts):
    from src.engines.utils.typewriter import stream_markdown
    for t in texts:
      stream_markdown(t)
