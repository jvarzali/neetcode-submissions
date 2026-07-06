class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        
        for token in tokens:
            if token not in "+-*/":
                nums.append(int(token))
            else:
                n2 = nums.pop()
                n1 = nums.pop()
                if token == "+":
                    nums.append(n1 + n2)
                elif token == "-":
                    nums.append(n1 - n2)
                elif token == "*":
                    nums.append(n1 * n2)
                else:
                    nums.append(int(n1 / n2))

        return nums.pop()