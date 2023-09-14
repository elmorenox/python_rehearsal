"""
def get_average_test_score(test_scores):
    return sum(test_scores)/len(test_scores)

scores = [100.00, 33, 75, 65, 78.50, 101]

avg = get_average_test_score(scores)

print(avg)
"""

def same_first_last(int_list):
    if int_list[0] == int_list[-1]:
        print(f"{int_list[0]} is {int_list[-1]}")
    else: print(f"{int_list[0]} is not {int_list[-1]}")

def remove_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    word = word.lower()
    for vowel in vowels:
        if vowel in word:
            word = word.replace(vowel, "")
    
    return word