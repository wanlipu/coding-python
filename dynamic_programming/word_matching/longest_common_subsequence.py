class Solution(object):
    def longest(self, source, target):
        """
        input: string source, string target
        return: int
        """
        # write your solution here
        if len(source) == 0 or len(target) == 0:
            return 0

        #table = [[0] * len(target)] * len(source) # all rows will change at the same time, bug
        table = []
        for i in range(len(source)):
            table.append([0]*len(target))

        for i in range(len(source)):
            for j in range(len(target)):
                if i == 0:
                    if j == 0:
                        if source[i] == target[j]:
                            table[i][j] = 1
                    else:
                        if source[i] == target[j]:
                            table[i][j] = 1
                        else:
                            table[i][j] = table[i][j-1]
                else:
                    if j == 0:
                        if source[i] == target[j]:
                            table[i][j] = 1
                        else:
                            table[i][j] = table[i-1][j]
                    else:
                        if source[i] == target[j]:
                            table[i][j] = table[i-1][j-1] + 1
                        else:
                            table[i][j] = max(table[i-1][j], table[i][j-1])
        print(table)

        return max(max(table))

    def longest_2(self, source, target):
        """
        input: string source, string target
        return: int
        """
        #table = [[0] * len(target)] * len(source) # all rows will change at the same time, bug
        table = []
        for i in range(len(source)+1):
            table.append([0]*(len(target)+1))

        for i in range(len(source)):
            for j in range(len(target)):
                if source[i] == target[j]:
                    table[i+1][j+1] = table[i][j] + 1
                else:
                    table[i+1][j+1] = max(table[i][j+1], table[i+1][j])
        # print(table)

        return max(max(table))


if __name__ == "__main__":
    example = Solution()

    source = [1, 2, 3, 4, -1, 7, 8, 0]
    target = [1]
    print('the length of longest subsequences: ' + str(example.longest(source, target)) + '\n')

    source = [1, 2, 3, 4, -1, 7, 8, 0]
    target = [1, 2, 3, 0]
    print('the length of longest subsequences: ' + str(example.longest(source, target)) + '\n')

    source = 'abbcdddeffg'
    target = 'bcbbcdf'
    print('the length of longest subsequences: ' + str(example.longest(source, target)) + '\n')
