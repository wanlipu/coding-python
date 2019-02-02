class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1

        length = len(coins)

        if length == 0:
            return -1
        # if length == 1:
        #     if coins[0] == amount:
        #         return 1
        #     else:
        #         return -1

        dp = [[float('inf')] * (length + 1) for _ in range(amount + 1)]

        for j in range(length + 1):
            dp[0][j] = 0

        for value in range(1, amount + 1):
            for j in range(1, length + 1):
                if coins[j-1] <= value:
                    min1 = min(dp[value - coins[j-1]][k] for k in range(j+1))
                    min2 = min(dp[value - coins[j-1]][k] for k in range(j))
                    dp[value][j] = min(min1, min2)+1
                else:
                    dp[value][j] = min(dp[value][k] for k in range(j))

        # print dp
        min_num = min(dp[-1])
        if min_num == float('inf'):
            return -1
        else:
            return min_num

    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1

        length = len(coins)

        if length == 0:
            return -1
        # if length == 1:
        #     if coins[0] == amount:
        #         return 1
        #     else:
        #         return -1

        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for value in range(1, amount + 1):
            for i in range(length):
                if coins[i] <= value and dp[value] > dp[value-coins[i]]+1:
                    dp[value] = dp[value-coins[i]]+1

        # print dp
        min_num = dp[-1]
        if min_num == float('inf'):
            return -1
        else:
            return min_num


if __name__ == "__main__":
    example = Solution()

    coins = [1, 2, 5]
    target = 11
    result = 3
    print('expected num : ' + str(result))
    print('min num to make the change is : ' + str(example.coinChange(coins, target)) + '\n')


    coins = [284, 260, 393, 494]
    target = 7066
    result = 17
    print('expected num : ' + str(result))
    print('min num to make the change is : ' + str(example.coinChange(coins, target)) + '\n')
    print('min num to make the change is : ' + str(example.coinChange2(coins, target)) + '\n')


