

"""
As each row has a size of three cells, each row can have 12 combinations of colors (6 for ABC and 6 for ABA).
As for each additional row, there is a limited number of possible combinations.
If the current row is ABC, there are 2 possible ABC and 2 possible ABA combinations.
If the current row is ABA, there are 2 possible ABC and 3 possible ABA combinations.
Thus, for each row take the current ABC and ABA combinations and multiply them with the possible variations.

There is additional request in the problems description. As the number of possibilitys grows fast, they ask to compute the answer with modulo of 10**9 + 7.
Thus, for every calculation, modulo it by the number (10**9 + 7).
"""


class Solution:
    def numOfWays(self, n: int) -> int:
        abc = 6
        aba = 6

        mod = 10 ** 9 + 7

        for i in range(1, n):
            new_abc = (abc * 2 + aba * 2) % mod
            new_aba = (abc * 2 + aba * 3) % mod

            abc = new_abc
            aba = new_aba

        return (abc + aba) % mod


def main():
    s = Solution()

    print(s.numOfWays(5000))


main()

