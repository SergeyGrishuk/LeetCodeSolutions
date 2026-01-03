

"""
This solution uses a sliding window with "teleporation".
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = {}

        left = 0
        right = 0

        max_size = 0

        while right < len(s):
            if s[right] in unique_chars and unique_chars[s[right]] >= left:
                left = unique_chars[s[right]] + 1

            unique_chars[s[right]] = right

            if right - left + 1 > max_size:
                max_size = right - left + 1

            right += 1

        return max_size


def main():
    s = Solution()

    print(s.lengthOfLongestSubstring("dvdf"))


main()

