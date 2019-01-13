class Solution(object):
    def sortSpecial(self, A1, A2):
        """
        input: int[] A1, int[] A2
        return: int[]
        """
        # write your solution here
        counts = {}
        for item in A2:
            counts[item] = 0
        counts['others'] = []
        for item in A1:
            if item in counts:
                counts[item] += 1
            else:
                counts['others'].append(item)

        results = []
        for item in A2:
            results += [item] * counts[item]
        results += sorted(counts['others'])

        return results

if __name__ == "__main__":
    solution = Solution()

    test_array = [1, 2, 3, 4, 9, 5, 6, 7, 0]
    print('array is: ' + str(test_array))
    print('sorted array: ' + str(solution.sortSpecial(test_array, [])) + '\n')

    test_array = [1, 2, 3, 4, 9, 5, 6, 7, 0]
    print('array is: ' + str(test_array))
    print('sorted array: ' + str(solution.sortSpecial(test_array, [4, 5, 6])) + '\n')

    test_array = []
    print('array is: ' + str(test_array))
    print('sorted array: ' + str(solution.sortSpecial(test_array, [])) + '\n')

    # test_array = None
    # print('array is: ' + str(test_array))
    # print('sorted array: ' + str(solution.sortSpecial(test_array, [])) + '\n')