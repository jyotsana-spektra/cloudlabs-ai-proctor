def generate_embedding(text: str):

    words = text.lower().split()

    return set(words)
