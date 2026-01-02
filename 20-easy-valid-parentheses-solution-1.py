

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in "([{":
                stack.append(i)

                continue

            if len(stack) == 0 or stack.pop() != pairs[i]:
                return False

        return True if len(stack) == 0 else False


if __name__ == '__main__':
    s = Solution()
    print(s.isValid(")"))
