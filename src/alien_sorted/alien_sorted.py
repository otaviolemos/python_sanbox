class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        numberOfWords = len(words)
        for i in range(numberOfWords-1):
            word1 = words[i]
            word2 = words[i+1]
            indexInWords = 0
            while (indexInWords <= len(word1)-1):
                if indexInWords > len(word2)-1:
                    return False
                valueOfLetterInWord1 = order.find(word1[indexInWords])
                valueOfLetterInWord2 = order.find(word2[indexInWords])
                if valueOfLetterInWord1 < valueOfLetterInWord2:
                    break
                if valueOfLetterInWord1 > valueOfLetterInWord2:
                    return False
                indexInWords += 1
        return True