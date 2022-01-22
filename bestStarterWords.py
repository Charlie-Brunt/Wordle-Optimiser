import matplotlib.pyplot as plt
import numpy as np
from wordStatistics import letterFrequency, letterProbability, normalisedScores, wordScores

with open('answers_wordlist.txt') as f:
    answers = f.readlines()
with open('complete_wordlist.txt') as f:
    words = f.readlines()

frequencies = letterFrequency(answers)
probabilities = letterProbability(frequencies)
wordScoreList = normalisedScores(wordScores(words, probabilities))

for i in range(20):
    print(f"[{i+1}]", wordScoreList[i][0], round(wordScoreList[i][1], 1))
print(f"[{wordScoreList.index(wordScoreList[-1])+1}]", wordScoreList[-1][0], round(wordScoreList[-1][1], 1))

while True:
    checkWord = input("Rate your starter word: ")
    validWord = False
    for i in wordScoreList:
        if i[0] == checkWord:
            print(f"[{wordScoreList.index(i)+1} of 12972]", i[0], round(i[1], 1))
            validWord = True
    if not validWord:
        print(f"'{checkWord}' not in Wordle dictionary.")
