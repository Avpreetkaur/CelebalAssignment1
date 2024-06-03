import itertools
from math import comb


def probability_of_a(n, letters, k):
    total_combinations = comb(n, k)

    indices_with_a = [i for i, letter in enumerate(letters) if letter == 'a']
    m = len(indices_with_a)

    if k > (n - m):
        no_a_combinations = 0
    else:
        no_a_combinations = comb(n - m, k)

    probability_of_no_a = no_a_combinations / total_combinations
    probability_of_at_least_one_a = 1 - probability_of_no_a

    return round(probability_of_at_least_one_a, 4)


n = int(input().strip())
letters = input().strip().split()
k = int(input().strip())

result = probability_of_a(n, letters, k)
print(result)