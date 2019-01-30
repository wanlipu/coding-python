class Solution(object):
    def editDistance(self, one, two):
        """
        input: string one, string two
        return: int
        """
        # write your solution here

        if len(one) == len(two) == 0:
            return 0
        elif len(one) == 0:
            return len(two)
        elif len(two) == 0:
            return len(one)
        elif one == two:
            return 0

        record = [[0] * (len(one) + 1) for i in range(len(two) + 1)]

        for i in range(len(two) + 1):
            for j in range(len(one) + 1):
                if i == 0:
                    record[i][j] = j
                elif j == 0:
                    record[i][j] = i
                elif two[i - 1] == one[j - 1]:
                    record[i][j] = record[i - 1][j - 1]
                else:
                    record[i][j] = 1 + min(record[i - 1][j - 1], record[i][j - 1], record[i - 1][j])
        print(record)
        return record[len(two)][len(one)]

if __name__ == "__main__":
    example = Solution()

    source = 'abc'
    target = 'abc'
    print('edit distance: ' + str(example.editDistance(source, target)) + '\n')

    source = ''
    target = ''
    print('edit distance: ' + str(example.editDistance(source, target)) + '\n')

    source = 'abbcdddeffg'
    target = 'bcbbcdf'
    print('edit distance: ' + str(example.editDistance(source, target)) + '\n')

    source = 'snow'
    target = 'nowadays'
    print('edit distance: ' + str(example.editDistance(source, target)) + '\n')


    source = 'snow'
    target = 'nowadays'
    print('edit distance: ' + str(example.editDistance(target, source)) + '\n')

    source = 's'
    target = 'nowadays'
    print('edit distance: ' + str(example.editDistance(source, target)) + '\n')
