

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)

        return not stack


if __name__ == '__main__':
    s = Solution()
    print(s.isValid(")"))
