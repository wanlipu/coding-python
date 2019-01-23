class Solution(object):
    def common(self, A, B):
        """
        input: Integer[] A, Integer[] B
        return: Integer[]
        """
        # write your solution here


        result = []

        i = 0
        j = 0

        while i < len(A) and j < len(B):
            if A[i] == B[j]:
                result.append(A[i])
                i += 1
                j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1

        return result


if __name__ == "__main__":

    example = Solution()

    A = [3, 9, 9, 111]
    B = [1, 2, 3, 5, 6, 9, 9]
    print('Common numbers: ' + str(example.common(A, B)) + '\n')
