class Solution(object):
    def longest(self, arrayA, arrayB):
        """
        input: string source, string target
        return: int
        """
        #table = [[0] * len(target)] * len(source) # all rows will change at the same time, bug
        table = []
        for i in range(len(arrayA)+1):
            table.append([0]*(len(arrayB)+1))

        for i in range(len(arrayA)):
            for j in range(len(arrayB)):
                if arrayA[i] == arrayB[j]:
                    table[i+1][j+1] = table[i][j] + 1
                else:
                    table[i+1][j+1] = table[i+1][j]
        # for item in table:
        #     print(item)

        # print(max(table))
        # print(max(max(table)))
        # return max(max(table))  # bug can't use this to find the max element in 2d array
        return max(max(item) for item in table)


if __name__ == "__main__":
    example = Solution()

    source = 'abdbabfgd'
    target = 'betfdbfafr'
    print('the length of longest subsequences: ' + str(example.longest(source, target)) + '\n')

    source = 'abdbabfgdaaaa'
    target = 'betfdbfafr'
    print('the length of longest subsequences: ' + str(example.longest(source, target)) + '\n')

    source = 'abdbafrbfgdaaaa'
    target = 'betfdbfafr'
    print('the length of longest subsequences: ' + str(example.longest(source, target)) + '\n')
