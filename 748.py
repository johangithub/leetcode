class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        from collections import Counter
        d = Counter([x.lower() for x in licensePlate if x.isalpha()])
        words.sort(key=len)
        for word in words:
            d2 = Counter(word)
            if all([letter in d2 and d2[letter]>=d[letter] for letter in d]):
                return word
            
