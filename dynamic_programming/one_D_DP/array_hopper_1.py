class Solution(object):
    def canJump(self, array):
        """
        input: int[] array
        return: boolean
        """
        # write your solution here

        record = [float('Inf')] * len(array)

        # if array[0] == 0:
        #     return False

        record[0] = 0

        for i in range(1, len(array)):
            for j in range(i):
                if array[j] >= i - j and record[j] + 1 < record[i]:
                    record[i] = record[j] + 1

        return record[len(array) - 1] != float('Inf')


if __name__ == "__main__":

    example = Solution()

    source = [0, 1, 2, 3]
    print('can jump to the end of the array: ' + str(example.canJump(source)) + '\n')

    source = [1, 1, 1, 1, 1]
    print('can jump to the end of the array: ' + str(example.canJump(source)) + '\n')

    source = [1, 2, 1, 1, 0, 1]
    print('can jump to the end of the array: ' + str(example.canJump(source)) + '\n')

    source = [100, 0, 0, 0, 0, 0, 0]
    print('can jump to the end of the array: ' + str(example.canJump(source)) + '\n')

    source = [0]
    print('can jump to the end of the array: ' + str(example.canJump(source)) + '\n')
