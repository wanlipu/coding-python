class Solution(object):
    def longest(self, array):
        """
        input: int[] array
        return: int
        """
        # write your solution here
        if not array:
            return 0
        if len(array) == 0:
            return 0

        lngest = 1
        current = 1

        for i in range(1, len(array)):
            if array[i] > array[i-1]:
                current += 1
                if current > lngest:
                    lngest = current
            else:
                current = 1

        return lngest



if __name__ == "__main__":
    example = Solution()

    test = [1, 2, 3, 4, -1, 7, 8, 0]
    print('array is: ' + str(test))
    print('the length of longest subsequences: ' + str(example.longest(test)) + '\n')

    test = [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]
    print('array is: ' + str(test))
    print('the length of longest subsequences: ' + str(example.longest(test)) + '\n')
