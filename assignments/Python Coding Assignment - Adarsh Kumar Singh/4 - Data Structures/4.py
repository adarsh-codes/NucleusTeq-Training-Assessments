def count_word_frequency(word_list):
    frequency = {}
    for word in word_list:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

words = ["cat", "dog", "cat", "mouse", "dog", "cat"]
result = count_word_frequency(words)
print(result)
