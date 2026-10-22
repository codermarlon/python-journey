def word_frequency(text):
    word_list = text.split()
    word_count = {}
    lower_case_word_list = [word.lower() for word in word_list]
    for word in lower_case_word_list:
      word_count[word] = word_count.get(word, 0) + 1
    return word_count
# 2
def largest(numbers):
    if not numbers:
        return None
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    return highest
# 3
def merge_dicts(a, b):
    for key in b:
        a[key] = a.get(key, 0) + b.get(key, 0)
    return a
# 4
def unique_sorted(items):
    removed_duplicates = set(items)
    return sorted(removed_duplicates)
# 5
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers)/len(numbers)

# 6
def invert_dict(d):
    inverted = {}
    for key, value in d.items():
       inverted[value] = key
    return inverted
# 7
def group_by_length(words):
    grouped_words = {}
    same_len_words = []
    lengths_list = set(len(word) for word in words)

    for length in lengths_list:
        for word in words:
            if length == len(word):
                same_len_words.append(word)
            grouped_words[length] = same_len_words
        same_len_words = []
    return grouped_words
# 8
def top_n(freq, n):
    freq_list = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return freq_list[:n]
# 9
def is_palindrome(text):
    text_list = [letter.lower() for letter in text  if letter != " "]
    text_reverse = text_list[::-1]
    return text_list == text_reverse
# 10
def cart_total(items):
    total_cost = 0
    for item in items:
        item_cost = item['price'] * item['qty']
        total_cost += item_cost
    return total_cost
