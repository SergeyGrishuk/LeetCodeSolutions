

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        first_word = strs[0]
        last_word = strs[-1]

        if first_word:
            for i in range(len(first_word)):
                if first_word[i] != last_word[i]:
                    return first_word[:i]

        return first_word

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["a"]))