from promptflow import tool

# Sample code echo input by yield in Python tool node

@tool
def stream_response(paragraph: str) -> str:
    for word in paragraph.split():
        yield word + " "