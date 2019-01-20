class Solution(object):
    def stairs(self, n):
        """
        input: int n
        return: int
        """
        # write your solution here
        if n == 1:
            return 1
        if n == 2:
            return 2

        record = [0] * n

        record[0] = 1
        record[1] = 2

        for i in range(2, n):
            record[i] = record[i - 1] + record[i - 2]

        return record[n - 1]


if __name__ == "__main__":

    example = Solution()

    source = 1
    print('the number of ways to climb : ' + str(example.stairs(source)) + '\n')

    source = 2
    print('the number of ways to climb : ' + str(example.stairs(source)) + '\n')

    source = 3
    print('the number of ways to climb : ' + str(example.stairs(source)) + '\n')

    source = 4
    print('the number of ways to climb : ' + str(example.stairs(source)) + '\n')

    source = 30
    print('the number of ways to climb : ' + str(example.stairs(source)) + '\n')