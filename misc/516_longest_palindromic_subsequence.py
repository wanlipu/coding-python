class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        length = len(s)
        if length <= 1:
            return length

        record = [[0] * length for _ in range(length)]

        for i in range(length):
            record[i][i] = 1

        for width in range(1, length):
            for i in range(length - width):
                j = i + width
                if s[i] == s[j]:
                    record[i][j] = record[i + 1][j - 1] + 2
                else:
                    record[i][j] = max(record[i + 1][j], record[i][j - 1])
        return record[0][-1]

if __name__ == "__main__":

    example = Solution()

    source = ''
    print('the length of Palindrome subsequence: ' + str(example.longestPalindromeSubseq(source)) + '\n')

    source = 'a'
    print('the length of Palindrome subsequence: ' + str(example.longestPalindromeSubseq(source)) + '\n')

    source = 'abcdba'
    print('the length of Palindrome subsequence: ' + str(example.longestPalindromeSubseq(source)) + '\n')

    source = 'abccbqqqa'
    print('the length of Palindrome subsequence: ' + str(example.longestPalindromeSubseq(source)) + '\n')

    source = 'abccbqa'
    print('the length of Palindrome subsequence: ' + str(example.longestPalindromeSubseq(source)) + '\n')

    source = 'abcabccba'
    print('the length of Palindrome subsequence: ' + str(example.longestPalindromeSubseq(source)) + '\n')

    source = 'abcbdbqa'
    print('the length of Palindrome subsequence: ' + str(example.longestPalindromeSubseq(source)) + '\n')

    source = 'abcdefghijklmnopxyda'
    print('the length of Palindrome subsequence: ' + str(example.longestPalindromeSubseq(source)) + '\n')
