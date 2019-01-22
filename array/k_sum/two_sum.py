class Solution(object):
    def existSum(self, array, target):
        """
        input: int[] array, int target
        return: boolean
        """
        # write your solution here

        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if target == array[i] + array[j]:
                    return True
        return False

    def existSum_2(self, array, target):
        """
        input: int[] array, int target
        return: boolean
        """
        # write your solution here

        record = {}

        for i in range(len(array)):
            if array[i] in record:
                return True
            else:
                record[target-i] = True
        return False

if __name__ == "__main__":

    example = Solution()

    array = [1, 2, 5, 9, 111]
    target = 10
    print('exist or not: ' + str(example.existSum(array, target)) + '\n')
    print('exist or not: ' + str(example.existSum_2(array, target)) + '\n')

