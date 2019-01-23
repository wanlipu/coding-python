class Solution(object):
    def merge(self, A, m, B, n):
        """
        input: int[] A, int m, int[] B, int n
        return: int[]
        """
        # write your solution here


        if m == 0:
            return B
        if n == 0:
            return A

        i = 0
        j = 0
        k = 0
        result = [0] * (m + n)

        while i < m and j < n:
            if A[i] <= B[j]:
                result[k] = A[i]
                i += 1
            elif A[i] > B[j]:
                result[k] = B[j]
                j += 1
            k += 1

        if i + j == m + n:
            return result
        elif i < m:
            result[k:] = A[i:m]
        else:
            result[k:] = B[j:n]

        return result

if __name__ == "__main__":

    example = Solution()

    A = [3, 9, 9, 111]
    B = [1, 2, 3, 5, 6, 9, 9]
    print('Merged Array: ' + str(example.merge(A, 2, B,2)) + '\n')