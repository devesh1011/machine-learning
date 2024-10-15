def read_words_with_e(filename):
  """
  Reads words from a file and returns a list of words that contain the letter 'e'.

  Args:
    filename: The name of the file to read.

  Returns:
    A list of words that contain the letter 'e'.
  """
  words_with_e = []
  with open(filename, 'r') as f:
    for line in f:
      words = line.strip().split()
      for word in words:
        if 'e' in word:
          words_with_e.append(word)
  return words_with_e

# Example usage
words = read_words_with_e("python.txt")
print(f"Words with 'e': {words}")
