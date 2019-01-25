import math

class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        num_of_repeats = int(math.ceil(float(len(B)) / len(A)))

        A_new = A * num_of_repeats

        if B in A_new:
            return num_of_repeats
        elif B in A_new + A:
            return num_of_repeats + 1
        else:
            return -1

if __name__ == "__main__":

    example = Solution()

    array = 'aaaaaaaaaaaaaaaaaaaaaaab'
    target = 'aba'
    print('num of repeats: ' + str(example.repeatedStringMatch(array, target)) + '\n')
