

"""
This solution uses Manacher's algorithm which has a runtime complexity of O(N).

Technically, because we add the character (`#`) to the string, the complexity is O(2N), but constants are omitted.

4 Cases: # This is just a reminder for myself

1. The letter's mirror palindrome exists entirely within the larger palindrome
but NOT up to the border.
    -> Copy mirror length
2. The letter's mirror palindrome exists entirely within the larger palindrome
up to the border.
    -> Explore beyond mirror length
3. The letter's mirror palindrome extends beyond the current palindrome.
    -> Explore beyond current palindrome
4. The current letter is not contained within a larger palindrome.
    -> Explore from scratch
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_mod = "#" + "#".join(s) + "#" # Add `#` character to make the length of the string odd
        p = [0 for _ in range(len(s_mod))] # Used to store the palindrome length for each character of `s`
        center = 0 # Represents the center of the current palindrome
        right = 0  # Represents the right index of the current palindrome

        max_radius = 0
        largest_palindrome_center = 0

        for i in range(len(s_mod)):
            mirror = center - (i - center) # The the mirror letter

            # Check if the current letter exists within a larger palindrome.
            if i < right:
                # Check if the mirror palindrome does not extent beyond the border of the
                # current palindrome centered at `center`
                if p[mirror] < right - i:
                    p[i] = p[mirror]
                
                # Check if the mirror palindrome extends beyond or up to the border of the palindrome centered at `center`
                # -> then we know that the radius of the palindrome centered at `s_mod[i]` is >= `right - i`
                else:
                    p[i] = right - i

            #
            # if `s_mod[i]` is NOT within a larger palindrome, then `p[i]` would be 0 and we'd be exploring from scratch
            while i - 1 - p[i] >= 0 \
                and i + 1 + p[i] < len(s_mod) \
                and s_mod[i - 1 - p[i]] == s_mod[i + 1 + p[i]]:

                p[i] += 1

            # if the palindrome centered at `i` extends beyond the palindrome centered at `center`
            if i + p[i] > right:

                # reset center and `right` to `i` and `i + p[i]` because the current palindrome is the
                # palindrome that reaches the furthest to the right
                center = i
                right = i + p[i]

            if p[i] > max_radius:
                max_radius = p[i]
                largest_palindrome_center = i

        # max_radius is a "radius" in s_mod but the full length of the palindrome in `s`
        start_index = (largest_palindrome_center - max_radius) // 2
        return s[start_index : start_index + max_radius]


def main():
    s = Solution()

    print(s.longestPalindrome("asa"))


main()

