class Solution(object):
    def longestPalindrome(self, input):
        """
        input: string input
        return: string
        """
        # write your solution here
        if len(input) == 0:
            return input
        # if len(input) == 1:
        #     return input

        record = []
        for i in range(len(input)):
            record.append([(0, '')] * len(input))

        for i in range(len(input)):
            record[i][i] = (1, input[i])

        for c in range(2, len(input)+1):
            for i in range(len(input)-c+1):
                j = i+c-1
                if input[i] == input[j]:
                    record[i][j] = (record[i+1][j-1][0]+2, input[i]+record[i+1][j-1][1]+input[i])
                else:
                    record[i][j] = tuple(max(record[i][j-1], record[i+1][j]))
        # print(record)
        if max([max(item) for item in record])[0] == 1:
            return input[0]

        # return max([max(item) for item in record])[2]
        return record[0][len(input)-1][1]


    def longestPalindrome_1(self, input):
        """
        input: string input
        return: string
        """
        # write your solution here
        if len(input) == 0:
            return input
        # if len(input) == 1:
        #     return input

        record = []
        for i in range(len(input)):
            record.append([(0, '')] * len(input))

        for i in range(len(input)):
            record[i][i] = (1, input[i])

        for j in range(1, len(input)):
            for i in range(0, len(input)-j):
                # print(record)
                if input[i] == input[i+j]:
                    record[i][i+j] = (record[i+1][i+j-1][0]+2, input[i]+record[i+1][i+j-1][1]+input[i])
                else:
                    record[i][i+j] = tuple(max(record[i][i+j-1], record[i+1][i+j]))
        # print(record)
        if max([max(item) for item in record])[0] == 1:
            return input[0]

        # return max([max(item) for item in record])[2]
        return record[0][len(input)-1][1]

if __name__ == "__main__":

    example = Solution()

    source = ''
    print('the length of Palindrome subsequence: ' + str(example.longestPalindrome(source)) + '\n')
    print('the length of Palindrome subsequence: ' + str(example.longestPalindrome_1(source)) + '\n')

    source = 'a'
    print('the length of Palindrome subsequence: ' + str(example.longestPalindrome(source)) + '\n')
    print('the length of Palindrome subsequence: ' + str(example.longestPalindrome_1(source)) + '\n')

    source = 'abcdba'
    print('the length of Palindrome subsequence: ' + str(example.longestPalindrome(source)) + '\n')
    print('the length of Palindrome subsequence: ' + str(example.longestPalindrome_1(source)) + '\n')

    source = 'abccbqqqa'
    print('the length of Palindrome subsequence: ' + str(example.longestPalindrome(source)) + '\n')
    print('the length of Palindrome subsequence: ' + str(example.longestPalindrome_1(source)) + '\n')

    source = 'abccbqa'
    print('the length of Palindrome subsequence: ' + str(example.longestPalindrome(source)) + '\n')
    print('the length of Palindrome subsequence: ' + str(example.longestPalindrome_1(source)) + '\n')

    source = 'abcabccba'
    print('the length of Palindrome subsequence: ' + str(example.longestPalindrome(source)) + '\n')
    print('the length of Palindrome subsequence: ' + str(example.longestPalindrome_1(source)) + '\n')

    source = 'abcbdbqa'
    print('the length of Palindrome subsequence: ' + str(example.longestPalindrome(source)) + '\n')
    print('the length of Palindrome subsequence: ' + str(example.longestPalindrome_1(source)) + '\n')

    source = 'abcdefghijklmnopxyda'
    print('the length of Palindrome subsequence: ' + str(example.longestPalindrome(source)) + '\n')
    print('the length of Palindrome subsequence: ' + str(example.longestPalindrome_1(source)) + '\n')
