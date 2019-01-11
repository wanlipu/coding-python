class Solution(object):
    def sort(self, array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here
        if not array:
            return array
        if len(array) == 0:
            return array

        i = 1
        while i < len(array):
            j = i
            while j > 0 and array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                j -= 1
            i += 1
        return array

if __name__ == "__main__":
    solution = Solution()
    test_array = [1, 2, 3, 4, 9, 5, 6, 7, 0]
    print(solution.sort(test_array))

    test_array = []
    print(solution.sort(test_array))

    test_array = None
    print(solution.sort(test_array))