

"""
This solution has O(N**2) runtime complexity and O(1) space complexity.
For each of the characters in string `s` you iterate twice more to check if it is a center of a plindrome.
You iterate twice because a palindrom can be either even or odd.

The complexity is O(N**2) because we iterate over all the characters in the for loop O(N) and for each character we iterate again, this in the worst case results in N/2.
We have two inner loops, each of which has a runtime of N/2, thus N/2 + N/2 is N.
Thus the final tuntime is O(N**2). 
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_n = 0
        p_left = 0
        p_right = 0

        for i in range(len(s)):
            # First check for odd palindromes
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                lenght = right - left + 1

                if lenght > longest_n:
                    longest_n = lenght
                    p_left = left
                    p_right = right

                left -= 1
                right += 1

            # Check again for even palindromes
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                lenght = right - left + 1

                if lenght > longest_n:
                    longest_n = lenght
                    p_left = left
                    p_right = right

                left -= 1
                right += 1

        return s[p_left:p_right + 1]


def main():
    s = Solution()

    print(s.longestPalindrome("cbbd"))


main()

