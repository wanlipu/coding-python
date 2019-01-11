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

        i = 0

        for i in range(len(array) - 1):
            current_min = array[i]
            idx = i
            for j in range(i + 1, len(array)):
                if array[j] < current_min:
                    idx = j
                    current_min = array[j]
            if idx > i:
                array[i], array[idx] = array[idx], array[i]
        return array

if __name__ == "__main__":
    solution = Solution()
    test_array = [1, 2, 3, 4, 9, 5, 6, 7, 0]
    print(solution.sort(test_array))

    test_array = []
    print(solution.sort(test_array))

    test_array = None
    print(solution.sort(test_array))