class Solution(object):
    def longest(self, array):
        """
        input: int[] array
        return: int
        """
        # write your solution here
        if len(array) == 1:
            return 1
        if len(array) == 0:
            return 0

        record = [1] * len(array)

        j = 0
        i = 1
        while i < len(array):
            while j < i:
                if array[j] < array[i]:
                    if record[i] < record[j] + 1:
                        record[i] = record[j] + 1
                j += 1
            j = 0
            i += 1
        return max(record)

if __name__ == "__main__":
    example = Solution()
    test = [1, 2, 3, 4, -1, 7, 8, 0]
    print(example.longest(test))