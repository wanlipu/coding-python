class Solution(object):
    def canMerge(self, a, b, c):
        """
        input: string a, string b, string c
        return: boolean
        """
        # write your solution here

        if len(a) + len(b) != len(c):
          return False

        if len(a) == 0:
            if b == c:
                return True
            else:
                return False
        if len(b) == 0:
            if a == c:
                return True
            else:
                return False
        if len(a) == len(b) == len(c) == 0:
          return True

        record = [[0] * (len(b) + 1) for i in range(len(a) + 1)]

        record[0][0] = 1

        for i in range(1, len(a) + 1):
            if c[i - 1] == a[i - 1] and record[i-1][0] == 1:
                record[i][0] = 1

        for j in range(1, len(b) + 1):
            if c[j - 1] == b[j - 1] and record[0][j-1] == 1:
                record[0][j] = 1

        for i in range(1, len(a) + 1):
            for j in range(1, len(b) + 1):
                if c[i + j - 1] == a[i - 1] and record[i - 1][j] == 1:
                    record[i][j] = 1
                if c[i + j - 1] == b[j - 1] and record[i][j - 1] == 1:
                    record[i][j] = 1

        print(record)
        if record[len(a)][len(b)] == 1:
            return True
        else:
            return False


if __name__ == "__main__":

    example = Solution()

    A = 'abc'
    B = 'fgh'
    C = 'abcdfg'
    print('can merge?: ' + str(example.canMerge(A, B, C)) + '\n')