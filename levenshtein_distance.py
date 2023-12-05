def read_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().strip('"') for line in file.readlines()]

def levenshtein_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # Insert
                                   dp[i][j - 1],      # Remove
                                   dp[i - 1][j - 1])  # Replace
    return dp[m][n]

def find_closest_words(input_word, dictionary_file):
    dictionary = read_dictionary(dictionary_file)
    distances = [(word, levenshtein_distance(input_word, word)) for word in dictionary]
    distances.sort(key=lambda x: x[1])
    return distances

dictionary_file = 'Dictionary.txt'  
input_word = 'exale' 
closest_words = find_closest_words(input_word, dictionary_file)
print("Words sorted by edit distance:", closest_words)
