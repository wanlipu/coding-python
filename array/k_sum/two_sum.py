import time

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
                record[target-array[i]] = True
        return False

    def existSum_3(self, array, target):
        """
        input: int[] array, int target
        return: boolean
        """
        # write your solution here

        record = set()

        for i in range(len(array)):
            if array[i] in record:
                return True
            else:
                record.add(target-array[i])
        return False

if __name__ == "__main__":

    example = Solution()

    array = list(range(10000))
    target = 19999


    start = time.time()
    print('exist or not: ' + str(example.existSum(array, target)))
    end = time.time()
    print('time used: ' + str(end - start) + '\n')

    start = time.time()
    print('exist or not: ' + str(example.existSum_2(array, target)))
    end = time.time()
    print('time used: ' + str(end - start) + '\n')

    start = time.time()
    print('exist or not: ' + str(example.existSum_3(array, target)))
    end = time.time()
    print('time used: ' + str(end - start) + '\n')


