from typing import Sequence
from itertools import combinations

def read_sequences_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

final_lcs = {}

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    index = L[m][n]
    lcs_string = [''] * (index + 1)
    lcs_string[index] = ""

    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs_string)

def find_lcs_of_all_combinations(sequences):
    if not sequences:
        return ""

    longest_lcs = ""
    for seq1, seq2 in combinations(sequences, 2):
        current_lcs = lcs(seq1, seq2)
        final_lcs[seq1].append(current_lcs)
        if len(current_lcs) > len(longest_lcs):
            longest_lcs = current_lcs

    return longest_lcs

# Usage example
file_path = 'data.txt'  
sequences = read_sequences_from_file(file_path)

for seq in sequences:
  final_lcs[seq] = []

print(sequences)
longest_common_subsequence = find_lcs_of_all_combinations(sequences)

for lcs, sequence_pairs in final_lcs.items():        
  print(f"Common Subsequence: {lcs}")
  print(f"Sequence Pairs: {sequence_pairs}" )

print("Longest Common Subsequence:", longest_common_subsequence)
print(len(final_lcs))
print(len(sequences))

