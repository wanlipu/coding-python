class Solution(object):
    def longestCommon(self, source, target):
        """
        input: string source, string target
        return: string
        """
        # write your solution here
        if len(source) * len(target) == 0:
            return ''

        record = []

        for i in range(len(source) + 1):
            record.append([(0, '')] * (len(target) + 1))

        for i in range(1, len(source) + 1):
            for j in range(1, len(target) + 1):
                if source[i - 1] == target[j - 1]:
                    record[i][j] = (record[i - 1][j - 1][0] + 1, record[i - 1][j - 1][1] + source[i - 1])

        return max([max(item) for item in record])[1]

if __name__ == "__main__":
    example = Solution()

    source = 'abc'
    target = 'abc'
    print('the length of longest string: ' + str(example.longestCommon(source, target)) + '\n')

    source = 'abcaaaaaaaaaaaaaaaaaaaaaaaad'
    target = 'abcccccccccccccccaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaad'
    print('the length of longest string: ' + str(example.longestCommon(source, target)) + '\n')

    source = 'abcaaaaaaaaaaaaaaaaaaaaaaaaddddddd'
    target = 'abcccccccccccccccaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadddddddd'
    print('the length of longest string: ' + str(example.longestCommon(source, target)) + '\n')
