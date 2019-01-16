class Solution(object):
    def largestSum(self, array):
        """
        input: int[] array
        return: int
        """
        # write your solution here
        record = [0] * len(array)

        for i in range(len(array)):
            if i == 0:
                record[i] = array[i]
            else:
                record[i] = max(record[i - 1] + array[i], array[i])
        return max(record)

if __name__ == "__main__":
    example = Solution()

    test = [1, 2, 3, 4, -1, 7, 8, 0]
    print('array is: ' + str(test))
    print('the length of longest subsequences: ' + str(example.largestSum(test)) + '\n')

    test = [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]
    print('array is: ' + str(test))
    print('the length of longest subsequences: ' + str(example.largestSum(test)) + '\n')