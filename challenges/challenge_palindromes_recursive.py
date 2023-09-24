def is_palindrome_recursive(word, low_index, high_index):
    wordLower = word.lower()
    size = len(wordLower)
    if size == 0:
        return False

    if low_index == high_index:
        inverted_word = wordLower[::-1]
        if inverted_word == wordLower:
            return True
        else:
            return False
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index)