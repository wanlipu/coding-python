class Solution(object):
    def quickSort(self, array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here
        if not array:
            return array
        if len(array) == 0:
            return array

        self.partition(array, 0, len(array) - 1)
        return array

    def partition(self, array, low, high):
        if low < high:
            pivot = array[low]
            i = low + 1
            j = high
            while i <= j:
                if array[i] < pivot:
                    i += 1
                elif array[j] >= pivot:  # have to have equal
                    j -= 1
                else:
                    array[i], array[j] = array[j], array[i]
            array[j], array[low] = array[low], array[j]
            self.partition(array, low, j - 1)
            self.partition(array, j + 1, high)
        else:
            return

if __name__ == "__main__":
    solution = Solution()

    test_array = [1, 2, 3, 4, 9, 5, 6, 7, 0]
    print('array is: ' + str(test_array))
    print('sorted array: ' + str(solution.quickSort(test_array)) + '\n')

    test_array = []
    print('array is: ' + str(test_array))
    print('sorted array: ' + str(solution.quickSort(test_array)) + '\n')

    test_array = None
    print('array is: ' + str(test_array))
    print('sorted array: ' + str(solution.quickSort(test_array)) + '\n')