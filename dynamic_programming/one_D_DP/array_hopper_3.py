class Solution(object):
    def minJump(self, array):
        """
        input: int[] array
        return: int
        """
        # write your solution here


        record_1 = [float('Inf')] * len(array)
        record_2 = [float('Inf')] * len(array)

        if len(array) == 1:
            if array[0] == 0:
                return -1
            else:
                return 1

        record_1[0] = 0
        if array[0] > len(array):
            return 1

        for i in range(1, len(array)):
            for j in range(i):
                if array[j] >= i - j and record_1[j] + 1 < record_1[i]:
                    record_1[i] = record_1[j] + 1
                if record_1[i] < float('inf') and array[i] >= len(array) - i:
                    if record_1[i] + 1 < record_2[i]:
                        record_2[i] = record_1[i] + 1

        # print(record_1)
        # print(record_2)

        if min(record_2) == float('Inf'):
            return -1
        else:
            return min(record_2)

if __name__ == "__main__":

    example = Solution()

    source = [0, 1, 2, 3]
    print('the minimal jumps needed to jump out of the array is : ' + str(example.minJump(source)) + '\n')

    source = [1, 1, 1, 1, 1]
    print('the minimal jumps needed to jump out of the array is : ' + str(example.minJump(source)) + '\n')

    source = [1, 2, 1, 1, 0, 1]
    print('the minimal jumps needed to jump out of the array is : ' + str(example.minJump(source)) + '\n')

    source = [100, 0, 0, 0, 0, 0, 0]
    print('the minimal jumps needed to jump out of the array is : ' + str(example.minJump(source)) + '\n')

    source = [0]
    print('the minimal jumps needed to jump out of the array is : ' + str(example.minJump(source)) + '\n')
