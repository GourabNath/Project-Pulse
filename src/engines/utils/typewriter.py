def stream_markdown(text: str, delay: float = 0.015):
    import time
    from IPython.display import display, Markdown
    """
    Stream markdown text in a ChatGPT-like typing effect.
    
    Parameters
    ----------
    text : str
        Markdown content to render
    delay : float
        Delay between characters
    """

    rendered = ""
    handle = display(Markdown(""), display_id=True)

    for char in text:
        rendered += char
        handle.update(Markdown(rendered))
        time.sleep(delay)
