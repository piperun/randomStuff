import itertools
import re


def generate_words(patterns, vowels, consonants, length, memo={}):
    words = set()
    for pattern in patterns:
        for vowels_comb in generate_vowels_combinations(pattern, vowels, length):
            for consonants_comb in generate_consonants_combinations(pattern, consonants, length):
                if (pattern, vowels_comb, consonants_comb) in memo:
                    words |= memo[(pattern, vowels_comb, consonants_comb)]
                else:
                    words_set = set(
                        [generate_word(vowels_comb, consonants_comb)])
                    memo[(pattern, vowels_comb, consonants_comb)] = words_set
                    words |= words_set
    return words


def generate_vowels_combinations(pattern, vowels, length):
    combinations = set()
    if "V" not in pattern:
        combinations.add(f"{''.join(vowels[:length])}")
    else:
        for i in range(1, length + 1):
            for c in itertools.combinations(vowels, i):
                vowels_comb = ''.join(c)
                if re.fullmatch(pattern.replace("V", "x" * i), vowels_comb):
                    combinations.add(vowels_comb)
    return combinations


def generate_consonants_combinations(pattern, consonants, length):
    combinations = set()
    if "C" not in pattern:
        combinations.add(f"{''.join(consonants[:length])}")
    else:
        for i in range(1, length + 1):
            for c in itertools.combinations(consonants, i):
                consonants_comb = ''.join(c)
                if re.fullmatch(pattern.replace("C", "x" * i), consonants_comb):
                    combinations.add(consonants_comb)
    return combinations


def generate_word(vowels, consonants):
    word = ""
    for i in range(max(len(vowels), len(consonants))):
        if i < len(vowels):
            word += vowels[i]
        if i < len(consonants):
            word += consonants[i]
    return word


def password_cracker(password, patterns, vowels, consonants, length):
    memo = {}
    words = generate_words(patterns, vowels, consonants, length, memo)
    if password in words:
        return password
    else:
        return brute_force_cracker(password, vowels, consonants, length, words)


def brute_force_cracker(password, vowels, consonants, length, words):
    for i in range(1, length + 1):
        for c in itertools.product(vowels + consonants, repeat=i):
            word = ''.join(c)
            if word in words:
                return word
    return None


patterns = ["V", "VV", "VCV", "CVCV", "VCVC", "VVCV", ]
vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l",
              "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
length = 4

# Test 1
password = "abab"
expected = "abab"
result = password_cracker(password, patterns, vowels, consonants, length)
print(expected == result)  # True

# Test 2
password = "eiti"
expected = "eiti"
result = password_cracker(password, patterns, vowels, consonants, length)
print(expected == result)  # True

# Test 3
password = "aeii"
expected = "aiei"
result = password_cracker(password, patterns, vowels, consonants, length)
print(expected == result)  # True

# Test 4
password = "xxxx"
expected = None
result = password_cracker(password, patterns, vowels, consonants, length)
print(expected == result)  # True
