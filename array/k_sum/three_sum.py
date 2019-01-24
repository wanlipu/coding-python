class Solution(object):
    def allTriples(self, array, target):
        """
        input: int[] array, int target
        return: int[][]
        """
        # write your solution here

        results = []
        results_set = set()
        for i in range(len(array)):
            record = set()
            cur_target = target - array[i]
            for j in range(i + 1, len(array)):
                if array[j] in record:
                    temp_array = sorted([array[i], cur_target - array[j], array[j]])
                    temp_str = str(temp_array[0]) + ':' + str(temp_array[1]) + ':' + str(temp_array[2])
                    if temp_str not in results_set:
                        results.append(temp_array)
                        results_set.add(temp_str)
                    record.add(cur_target - array[j])
                else:
                    record.add(cur_target - array[j])

        return results

if __name__ == "__main__":

    example = Solution()

    array = [1, 1, 1, 1, 1, 1, 2, 2, 2, 0]
    target = 3
    print('all triples: ' + str(example.allTriples(array, target)) + '\n')
