class Solution(object):
    def numWays(self, n, k):
        """
        input: int n, int k
        return: int
        """
        # write your solution here

        if n == 0 or k == 0:
            return 0

        if n > 2 and k == 1:
            return 0

        if n == 1:
            return k

        record = [0] * n

        record[0] = k
        record[1] = k + k * (k - 1)
        for i in range(2, n):
            record[i] = record[i - 1] * (k - 1) + record[i - 2] * (k - 1)

        return record[n - 1]


if __name__ == "__main__":

    example = Solution()

    num_of_color = 1
    num_of_post = 10
    print('the number of ways to paint the fence : ' + str(example.numWays(num_of_color, num_of_post)) + '\n')

    num_of_color = 2
    num_of_post = 1
    print('the number of ways to paint the fence : ' + str(example.numWays(num_of_color, num_of_post)) + '\n')

    num_of_color = 10
    num_of_post = 2
    print('the number of ways to paint the fence : ' + str(example.numWays(num_of_color, num_of_post)) + '\n')

    num_of_color = 1
    num_of_post = 10
    print('the number of ways to paint the fence : ' + str(example.numWays(num_of_color, num_of_post)) + '\n')

    num_of_color = 1
    num_of_post = 10
    print('the number of ways to paint the fence : ' + str(example.numWays(num_of_color, num_of_post)) + '\n')
