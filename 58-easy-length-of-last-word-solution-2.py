

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_length = 0

        # Turns out hat in Python the reversed() function returns one element at a time.
        # Unlike s[::-1] which creates a copy in the memory.
        # This eliminates the need to implement custom logic such as s[-(i+1)].
        for character in reversed(s):
            if character != " ":
                last_word_length += 1
            elif last_word_length > 0:
                    break

        return last_word_length

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("a"))