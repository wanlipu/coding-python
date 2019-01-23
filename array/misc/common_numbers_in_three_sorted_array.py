class Solution(object):
    def common(self, a, b, c):
        """
        input: int[] a, int[] b, int[] c
        return: Integer[]
        """
        # write your solution here

        i = 0
        j = 0
        k = 0
        result = []

        while i < len(a) and j < len(b) and k < len(c):
            if a[i] == b[j] == c[k]:
                result.append(a[i])
                i += 1
                j += 1
                k += 1
            elif a[i] < c[k] and b[j] < c[k]:
                i += 1
                j += 1
            elif a[i] < b[j] and c[k] < b[j]:
                i += 1
                k += 1
            elif b[j] < a[i] and c[k] < a[i]:
                j += 1
                k += 1
            elif a[i] == c[k] and b[j] < c[k]:
                j += 1
            elif b[j] == c[k] and a[i] < c[k]:
                i += 1
            elif a[i] == b[j] and c[k] < a[i]:
                k += 1

        return result

if __name__ == "__main__":

    example = Solution()

    A = [3, 9, 9, 111]
    B = [1, 2, 3, 5, 6, 9, 9]
    C = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 1000]
    print('Common numbers: ' + str(example.common(A, B, C)) + '\n')