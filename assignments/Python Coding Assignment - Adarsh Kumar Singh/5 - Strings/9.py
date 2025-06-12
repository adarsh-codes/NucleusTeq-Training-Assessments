def longest_palindromic_substring(s):
    if not s or len(s) == 1:
        return s

    start = 0
    max_length = 1

    def expand_around_center(left, right):
        nonlocal start, max_length
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

    for i in range(len(s)):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)

    return s[start:start + max_length]

input_str = "babad"
print(longest_palindromic_substring(input_str))  
