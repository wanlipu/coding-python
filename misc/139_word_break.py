class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        length = len(s)
        if length == 0:
            return True

        record = [False] * (length + 1)
        record[0] = True
        if s[0] in wordDict:
            record[1] = True

        for i in range(2, length + 1):
            for j in range(1, i + 1):
                if s[j - 1:i + 1 - 1] in wordDict and record[j - 1]:
                    record[i] = True
                    # continue
        return record[-1]


if __name__ == "__main__":

    example = Solution()

    source = 'hellokitty'
    aDict = ['hello', 'kitty']
    print('could the string be broken into words: ' + str(example.wordBreak(source, aDict)) + '\n')

    source = 'helloakitty'
    aDict = ['hello', 'kitty']
    print('could the string be broken into words: ' + str(example.wordBreak(source, aDict)) + '\n')

    source = 'helloakitty'
    aDict = ['hello', 'kitty', 'a']
    print('could the string be broken into words: ' + str(example.wordBreak(source, aDict)) + '\n')

