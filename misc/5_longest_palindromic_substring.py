class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        length = len(s)
        if length <= 1:
            return s

        record = [[(0, '')] * length for _ in range(length)]

        for i in range(length):
            record[i][i] = (1, s[i])

        for width in range(1, length):
            for i in range(length - width):
                j = i + width
                if s[i] == s[j] and record[i + 1][j - 1][0] == j - i - 1:
                    record[i][j] = (record[i + 1][j - 1][0] + 2, s[i] + record[i + 1][j - 1][1] + s[j])
                else:
                    record[i][j] = (0, '')
        max_length = 0
        string = ''
        # print (record)
        for i in range(length):
            for j in range(i, length):
                if record[i][j][0] > max_length:
                    max_length = record[i][j][0]
                    string = record[i][j][1]

        return string

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        # reduce memory usage
        if not s:
            return ''
        length = len(s)
        if length <= 1:
            return s

        record = [[0] * length for _ in range(length)]

        for i in range(length):
            record[i][i] = 1

        max_length = 1
        string = s[0]

        for width in range(1, length):
            for i in range(length - width):
                j = i + width
                if s[i] == s[j] and record[i + 1][j - 1] == j - i - 1:
                    record[i][j] = record[i + 1][j - 1] + 2
                    if record[i][j] > max_length:
                        string = s[i:j + 1]
                else:
                    record[i][j] = 0

        return string


if __name__ == "__main__":

    example = Solution()

    source = ''
    print('the longest Palindrome substring: ' + str(example.longestPalindrome(source)) + '\n')

    source = 'a'
    print('the longest Palindrome substring: ' + str(example.longestPalindrome(source)) + '\n')

    source = 'abcdba'
    print('the longest Palindrome substring: ' + str(example.longestPalindrome(source)) + '\n')

    source = 'abccbqqqa'
    print('the longest Palindrome substring: ' + str(example.longestPalindrome(source)) + '\n')

    source = 'abccbqa'
    print('the longest Palindrome substring: ' + str(example.longestPalindrome(source)) + '\n')

    source = 'abcabccba'
    print('the longest Palindrome substring: ' + str(example.longestPalindrome(source)) + '\n')

    source = 'abcbdbqa'
    print('the longest Palindrome substring: ' + str(example.longestPalindrome(source)) + '\n')

    source = 'abcdefabccbamnopxyda'
    print('the longest Palindrome substring: ' + str(example.longestPalindrome(source)) + '\n')
    print('the longest Palindrome substring: ' + str(example.longestPalindrome2(source)) + '\n')
