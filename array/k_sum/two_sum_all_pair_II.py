class Solution(object):
    def allPairs(self, array, target):
        """
        input: int[] array, int target
        return: int[][]
        """
        # write your solution here


        record = {}

        results = []
        for i in range(len(array)):
            num = array[i]
            if num in record:
                if record[num]:
                    if num < target - num:
                        results.append([num, target - num])
                    else:
                        results.append([target - num, num])
                    record[target - num] = False
                    record[num] = False
            else:
                record[target - num] = True

        return results

if __name__ == "__main__":

    example = Solution()

    array = [1, 2, 5, 9, 111, 5]
    target = 10
    print('all pairs: ' + str(example.allPairs(array, target)) + '\n')
    # print('exist or not: ' + str(example.allPairs(array, target)) + '\n')