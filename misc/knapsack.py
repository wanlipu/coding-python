class Solution(object):
    def knapsack(self, values, weights, limit):
        """
        input: string source, string target
        return: int
        """
        # write your solution here
        if len(values) == 0 or len(weights) == 0:
            return 0

        #table = [[0] * len(target)] * len(source) # all rows will change at the same time, bug
        table = []
        for i in range(limit+1):
            table.append([0]*(len(values)+1))


        for max_weights in range(limit+1):
            for i in range(len(values)+1):
                if max_weights == 0:
                    table[max_weights][i] = 0
                else:
                    if i == 0:
                        table[max_weights][i] = 0
                    else:
                        if weights[i-1] > max_weights:
                            table[max_weights][i] = table[max_weights][i-1]
                        else:
                            table[max_weights][i] = max(table[max_weights-weights[i-1]][i-1]+values[i-1], table[max_weights][i-1])
        # print(table)

        return table[limit][len(values)]

if __name__ == "__main__":
    import numpy as np
    example = Solution()

    values = [1, 2, 3, 4, 1, 7, 8, 0]
    weights = [1, 1, 1, 1, 1, 1, 1, 1]
    limit = 20
    print('the largest values: ' + str(example.knapsack(values, weights, limit)) + '\n')


    # some example are from https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html
    values = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
    solution_table = [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
    result = sum(np.array(values) * np.array(solution_table))
    limit = 165
    print('solution is: '+ str(result))
    print('the largest values: ' + str(example.knapsack(values, weights, limit)) + '\n')


