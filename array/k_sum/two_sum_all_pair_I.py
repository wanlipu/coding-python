class Solution(object):
    def allPairs(self, array, target):
        """
        input: int[] array, int target
        return: int[][]
        """
        # write your solution here

        record = []
        length = len(array)

        for i in range(length):
            for j in range(i + 1, length):
                if array[i] + array[j] == target:
                    record.append([i, j])
        return record

if __name__ == "__main__":

    example = Solution()

    array = [1, 2, 5, 9, 111, 5]
    target = 10
    print('exist or not: ' + str(example.allPairs(array, target)) + '\n')
    # print('exist or not: ' + str(example.allPairs(array, target)) + '\n')