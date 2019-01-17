class Solution(object):
    def largestProduct(self, array):
        """
        input: int[] array
        return: int
        """
        # write your solution here
        record = []
        for i in range(len(array)):
         record.append([0] * len(array))

        for i in range(len(array)):
            record[i][i] = array[i]
            for j in range(i+1, len(array)):
                record[i][j] = record[i][j-1]*array[j]

        return max([max(item) for item in record])

if __name__ == "__main__":
    example = Solution()

    test = [1, 2, 3, 4, -1, 7, 8, 0]
    print('array is: ' + str(test))
    print('the length of longest subsequences: ' + str(example.largestProduct(test)) + '\n')

    test = [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]
    print('array is: ' + str(test))
    print('the length of longest subsequences: ' + str(example.largestProduct(test)) + '\n')