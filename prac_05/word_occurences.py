def main():
    """Count occurrences of words in a string and display results."""
    text = input("Text: ")
    words = text.split()
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
