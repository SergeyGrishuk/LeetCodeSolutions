

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)

        for i in range(len(haystack) - needle_len + 1):
            if needle == haystack[i: i + needle_len]:
                return i

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("sadbutsad", "ad"))
