class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        if len(nums) == 0:
            return 1
        if len(nums) == 1:
            return nums[0]

        nums = [1] + nums + [1]

        record = [[0] * len(nums) for i in range(len(nums))]


        # for i in range(len(nums)):
        #     record[i][i]=nums[i]

        for j in range(2, len(nums)):
            for i in range(len(nums) - j):
                max_value = 0
                for k in range(1, j):
                    temp = record[i][i+k]+ nums[i]*nums[i+k]*nums[j+i]+record[i+k][j+i]
                    if temp > max_value:
                        max_value = temp

                record[i][i + j] = max_value

        return record[0][len(nums) - 1]

if __name__ == "__main__":
    import numpy as np
    example = Solution()

    values = [3, 1, 5, 8]
    result = 167
    print('the largest values: ' + str(example.maxCoins(values)) + '\n')

    values = [3, 3]
    result = 3
    print('the largest values: ' + str(example.maxCoins(values)) + '\n')