class Solution(object):
    def longest(self, array):
        """
        input: int[] array
        return: int
        """
        # write your solution here
        if len(array) == 0:
            return 0

        table = [0] * (len(array) + 1)
        for i in range(1, len(array) + 1):
            if array[i - 1] == 1:
                table[i] = table[i - 1] + 1
        return max(table)

if __name__ == "__main__":
    example = Solution()

    test = [1, 1, 3, 4, -1, 7, 8, 0]
    print('array is: ' + str(test))
    print('the length of longest subsequences: ' + str(example.longest(test)) + '\n')

    test = [1, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]
    print('array is: ' + str(test))
    print('the length of longest subsequences: ' + str(example.longest(test)) + '\n')
