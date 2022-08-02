def get_string_word_statistics(s: str):
    """
    Return various statistics about words in string s.

    Question 5.5
    Words are defined as a continuous sequence of characters belonging to the English alphabet and/or hyphens.
    :param s: a string.
    :precondition: The string will only contain letters in the English alphabet (either case), numbers, commas, periods,
                   and hyphens.
    :return: the longest word or an empty string if no words are found. If ties are found, the first word by
             alphabetical order will be returned.

    Technically the order will be determined by Python's sorted method. Words as defined above could start with hyphens,
    which will be alphabetically precede any other letters.
    """
    chars_to_clean = "0123456789,."
    for c in chars_to_clean:
        s = s.replace(c, "")
    longest_words = [""]
    current_word = ""
    for c in s:
        if c == " ":
            # word ends
            if len(current_word) > len(longest_words[0]):
                longest_words = [current_word]
            elif len(current_word) == len(longest_words[0]):
                longest_words.append(current_word)
            current_word = ""
        else:
            current_word += c

    # for last word
    if len(current_word) > len(longest_words[0]):
        longest_words = [current_word]
    elif len(current_word) == len(longest_words[0]):
        longest_words.append(current_word)
    print(longest_words)
    return [sorted(longest_words, key=str.lower)[0]]


def get_string_letter_statistics(s: str):
    """
    Return various statistics about letters in string s.

    Question 5.1, 5.2, 5.3, 5.4
    Only considers letters in the English alphabet.
    :param s: a string.
    :return: various statistics about letters in string s
    """
    ALPHABET_LENGTH = 26
    # array tracks letter counts, 0 to 25 for a to z, 26 to 51 for A to Z
    letter_count_arr = [0 for _ in range(ALPHABET_LENGTH * 2)]

    # count the letters
    for c in s:
        ascii_value = ord(c)
        if ord("A") <= ascii_value <= ord("Z") or ord("a") <= ascii_value <= ord("z"):
            if ascii_value > ord("Z"):
                # assigns the array positions 0 to 25 inclusive to letters a to z
                letter_count_arr[ascii_value - ord("a")] += 1
            else:
                # assigns the array positions 26 to 51 inclusive to letters A to Z
                letter_count_arr[ascii_value - ord("A") + ALPHABET_LENGTH] += 1

    case_insensitive_letter_count_arr = [lower + upper for lower, upper in
                                         zip(letter_count_arr[0:ALPHABET_LENGTH], letter_count_arr[ALPHABET_LENGTH:])]

    # Question 5.1
    # Thought not explicitly stated, sample input 1 suggests that this should be case insensitive
    # Your question also suggests that there must be at least one letter in the sentence. This will work either way.
    unique_letter_count = sum([1 if count else 0 for count in case_insensitive_letter_count_arr])

    # Question 5.2
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    for c in VOWELS:
        vowel_count += case_insensitive_letter_count_arr[ord(c) - ord("a")]

    # Question 5.3
    uppercase_count = sum(letter_count_arr[26:])

    # Question 5.4
    most_common_letter_count = max(case_insensitive_letter_count_arr)

    return unique_letter_count, vowel_count, uppercase_count, most_common_letter_count


def output_string_statistics(sentence: str):
    """
    Print statistics about input string "sentence".

    Question 5
    The precondition is created to keep the solution reasonable.
    :param sentence: A string up to 1024 characters long.
    :precondition: The string will only contain letters in the English alphabet (either case), numbers, commas, periods,
                   and hyphens.
    """
    statistic_functions = [get_string_letter_statistics, get_string_word_statistics]
    statistics = []
    for func in statistic_functions:
        statistics.extend(func(sentence))

    for i, stat in enumerate(statistics):
        print(f"{i + 1}. {stat}")


if __name__ == '__main__':
    sample_input = "The quick brown fox, named Roxanne, jumped over Bruno, a lazy dog. "
    sample_input2 = "The 2019 All-Star Competition is at Wayne Hills HS in Wayne, New Jersey. "
    output_string_statistics(sample_input)
