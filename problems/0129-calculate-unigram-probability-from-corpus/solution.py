def unigram_probability(corpus: str, word: str) -> float:
    # Your code here
    tokens = corpus.split() #breaks words and also end and start since separated by space
    total = len(tokens)

    count = tokens.count(word)
    res = count/total

    return round(res, 4)
  

