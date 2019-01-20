class Solution(object):
    def minJump(self, array):
        """
        input: int[] array
        return: int
        """
        # write your solution here

        record = [float('Inf')] * len(array)

        record[0] = 0

        for i in range(1, len(array)):
            for j in range(i):
                if array[j] >= i - j and record[j] + 1 < record[i]:
                    record[i] = record[j] + 1

        if record[len(array) - 1] == float('Inf'):
            return -1
        else:
            return record[len(array) - 1]


if __name__ == "__main__":

    example = Solution()

    source = [0, 1, 2, 3]
    print('the minimal jumps needed to jump to the end of the array is : ' + str(example.minJump(source)) + '\n')

    source = [1, 1, 1, 1, 1]
    print('the minimal jumps needed to jump to the end of the array is : ' + str(example.minJump(source)) + '\n')

    source = [1, 2, 1, 1, 0, 1]
    print('the minimal jumps needed to jump to the end of the array is : ' + str(example.minJump(source)) + '\n')

    source = [100, 0, 0, 0, 0, 0, 0]
    print('the minimal jumps needed to jump to the end of the array is : ' + str(example.minJump(source)) + '\n')

    source = [0]
    print('the minimal jumps needed to jump to the end of the array is : ' + str(example.minJump(source)) + '\n')
