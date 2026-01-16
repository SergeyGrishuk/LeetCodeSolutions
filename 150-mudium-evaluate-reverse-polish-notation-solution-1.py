

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.lstrip("-").isnumeric():
                stack.append(int(token))
            else:
                match token:
                    case "+":
                        a = stack.pop()
                        b = stack.pop()

                        stack.append(b + a)
                    case "-":
                        a = stack.pop()
                        b = stack.pop()

                        stack.append(b - a)
                    case "*":
                        a = stack.pop()
                        b = stack.pop()

                        stack.append(b * a)
                    case "/":
                        a = stack.pop()
                        b = stack.pop()

                        stack.append(int(b / a))

        return stack[0]


def main():
    s = Solution()

    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    # print(s.evalRPN(["3", "1", "-"]))


main()
