class Solution(object):
    def smallerPairs(self, array, target):
        """
        input: int[] array, int target
        return: int
        """
        # write your solution here

        count = 0
        records = []

        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] + array[j] < target:
                    count += 1
                    records.append([array[i], array[j]])

        return count, records

if __name__ == "__main__":

    example = Solution()

    A = [3, 9, 9, 111]
    Target = 15
    print('number of pairs: ' + str(example.smallerPairs(A, Target)[0]))
    print('and they are: ' + str(example.smallerPairs(A, Target)[1]) + '\n')