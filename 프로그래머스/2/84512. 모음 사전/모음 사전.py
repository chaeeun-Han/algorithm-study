from itertools import permutations

def solution(word):
    alphabet = ['A', 'A', 'A', 'A', 'A', 'E', 'E', 'E', 'E', 'E', 'I',
                'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'U', 'U', 'U', 'U', 'U']
    dictionary = set()

    for length in range(1, 6):
        for per in permutations(alphabet, length):
            dictionary.add(''.join(list(per)))

    dictionary = list(dictionary)
    dictionary.sort()

    return dictionary.index(word) + 1