class Solution(object):
    def mergeSort(self, array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here
        if not array:
            return array
        if len(array) == 0:
            return array
        if len(array) == 1:
            return array

        left_half = self.mergeSort(array[:len(array) / 2])
        right_half = self.mergeSort(array[len(array) / 2:])

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                k += 1
                i += 1
            else:
                array[k] = right_half[j]
                k += 1
                j += 1
        while i < len(left_half):
            array[k] = left_half[i]
            k += 1
            i += 1
        while j < len(right_half):
            array[k] = right_half[j]
            k += 1
            j += 1
        return array


if __name__ == "__main__":
    solution = Solution()

    test_array = [1, 2, 3, 4, 9, 5, 6, 7, 0]
    print('array is: ' + str(test_array))
    print('sorted array: ' + str(solution.mergeSort(test_array)) + '\n')

    test_array = []
    print('array is: ' + str(test_array))
    print('sorted array: ' + str(solution.mergeSort(test_array)) + '\n')

    test_array = None
    print('array is: ' + str(test_array))
    print('sorted array: ' + str(solution.mergeSort(test_array)) + '\n')


