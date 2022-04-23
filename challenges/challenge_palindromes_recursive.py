def is_palindrome_recursive(word, low_index, high_index):
    try:
        if word[low_index] != word[high_index]:
            return False
        if low_index == high_index or low_index == high_index - 1:
            return True
    except IndexError:
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
