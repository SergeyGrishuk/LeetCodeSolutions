

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_length = 0

        for i in range(len(s)):
            if s[-(i + 1)] != " ":
                last_word_length += 1
            elif last_word_length > 0:
                    break

        return last_word_length

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("a"))