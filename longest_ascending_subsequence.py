class Solution(object):
    def longest(self, array):
        """
        input: int[] array
        return: int
        """
        # write your solution here
        if len(array) == 1:
            return 1
        if len(array) == 0:
            return 0

        record = [1] * len(array)

        j = 0
        i = 1
        while i < len(array):
            while j < i:
                if array[j] < array[i]:
                    if record[i] < record[j] + 1:
                        record[i] = record[j] + 1
                j += 1
            j = 0
            i += 1
        return max(record)

if __name__ == "__main__":
    example = Solution()

    test = [1, 2, 3, 4, -1, 7, 8, 0]
    print('array is: ' + str(test))
    print('the length of longest subsequences: ' + str(example.longest(test)) + '\n')

    test = [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]
    print('array is: ' + str(test))
    print('the length of longest subsequences: ' + str(example.longest(test)) + '\n')