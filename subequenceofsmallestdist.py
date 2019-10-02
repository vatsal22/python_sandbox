class Solution(object):

    def findSequence(self, text, text_stripped, index, word):

        if text[index] in text_stripped:
            text_stripped.discard(text[index])
            word += text[index]

        if len(text_stripped) == 0:
            return word

        if(index == len(text)-2):
            s3 = text_stripped
            return self.findSequence(text, s3, index+1, word)

        s1, s2 = text_stripped
        word1 = self.findSequence(text, s1, index+1, word)
        word2 = self.findSequence(text, s2, index+2, word)

        return word1 if len(word1) < len(word2) else word2
        # return min(findSequence(text, text_stripped, index+1, word), findSequence(text, text_stripped, index+2, word))

    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        text_stripped = set(text)

        print(self.findSequence( text, text_stripped, 0, ""))


x = Solution()
x.smallestSubsequence("abc")
