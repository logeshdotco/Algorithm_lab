def pattern_matching(text, pattern):
  n = len(text)
  m = len(pattern)
  occurrences = []
  for i in range(n - m + 1):
    j = 0
    while j < m:
      if text[i + j] != pattern[j]:
        break
      j += 1
    if j == m:
      occurrences.append(i)
  return occurrences
text = "ababdjsdsbabdbdabababa"
pattern = "ababa"
occurrences = pattern_matching(text, pattern)
print(f"Pattern Matching: Pattern found at indices", occurrences)
