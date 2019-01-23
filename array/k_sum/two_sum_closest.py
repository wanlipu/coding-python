class Solution(object):
    def closest(self, array, target):
        """
        input: int[] array, int target
        return: Integer[]
        """
        # write your solution here

        array_sorted = sorted(array)

        i = 0
        j = len(array) - 1

        diff = float('Inf')
        while i < j:
            current = array_sorted[i] + array_sorted[j]
            if abs(current - target) < diff:
                diff = abs(current - target)
                result = [array_sorted[i], array_sorted[j]]
            if array_sorted[i] + array_sorted[j] < target:
                i += 1
            elif array_sorted[i] + array_sorted[j] > target:
                j -= 1
            else:
                return result

        return result

if __name__ == "__main__":

    example = Solution()

    array = [3, 4, 1, -1, 2, 0, 5]
    target = 0
    print('closest pair: ' + str(example.closest(array, target)) + '\n')
    # print('exist or not: ' + str(example.allPairs(array, target)) + '\n')