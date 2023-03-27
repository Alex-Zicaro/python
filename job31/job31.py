def next_word(word):
    word = list(word)
    n = len(word)
    i = n - 2
    while i >= 0 and word[i] >= word[i + 1]:
        i -= 1
    if i < 0:
        return None
    j = n - 1
    while word[j] <= word[i]:
        j -= 1
    word[i], word[j] = word[j], word[i]
    left, right = i + 1, n - 1
    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1
    return ''.join(word)