wordA = 'blue'
wordB = 'lbeu'

def is_anagram(wordA, wordB):
    sorted_wordA = sorted(wordA)
    sorted_wordB = sorted(wordB)
    return sorted_wordA == sorted_wordB

result = is_anagram(wordA,wordB)

print(result)


