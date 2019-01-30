class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        if not word1 and not word2:
            return 0
        elif not word1:
            return len(word2)
        elif not word2:
            return len(word1)

        if len(word1) == len(word2) == 0:
            return 0

        if word1 == word2:
            return 0

        record = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    record[i][j] = record[i - 1][j - 1] + 1
                else:
                    record[i][j] = max(record[i - 1][j], record[i][j - 1])

        comm_num = max([max(item) for item in record])

        return len(word1) + len(word2) - 2 * comm_num


if __name__ == "__main__":
    example = Solution()

    source = 'abc'
    target = 'abc'
    print('delete operation for two strings: ' + str(example.minDistance(source, target)) + '\n')

    source = ''
    target = ''
    print('delete operation for two strings: ' + str(example.minDistance(source, target)) + '\n')

    source = 'abbcdddeffg'
    target = 'bcbbcdf'
    print('delete operation for two strings: ' + str(example.minDistance(source, target)) + '\n')

    source = 'snow'
    target = 'nowadays'
    print('delete operation for two strings: ' + str(example.minDistance(source, target)) + '\n')
