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
            record.append([(0, True, '')] * len(input))

        for i in range(len(input)):
            record[i][i] = (1, True, input[i])

        for j in range(1, len(input)):
            for i in range(0, len(input)-j):
                # print(record)
                if input[i] == input[i+j]:
                    if record[i+1][i+j-1][1]:
                        record[i][i+j] = (record[i+1][i+j-1][0]+2, True, input[i]+record[i+1][i+j-1][2]+input[i])
                    else:
                        record[i][i + j] = (0, False, '')
                else:
                    record[i][i + j] = (0, False, '')
        # print(record)
        if max([max(item) for item in record])[0] == 1:
            return input[0]

        return max([max(item) for item in record])[2]

if __name__ == "__main__":

    example = Solution()

    source = ''
    print('the length of Palindrome substring: ' + str(example.longestPalindrome(source)) + '\n')

    source = 'a'
    print('the length of Palindrome substring: ' + str(example.longestPalindrome(source)) + '\n')

    source = 'abc'
    print('the length of Palindrome substring: ' + str(example.longestPalindrome(source)) + '\n')

    source = 'abccb'
    print('the length of Palindrome substring: ' + str(example.longestPalindrome(source)) + '\n')