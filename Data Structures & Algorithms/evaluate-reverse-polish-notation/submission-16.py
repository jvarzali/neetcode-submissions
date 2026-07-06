class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        
        for token in tokens:
            if token == "+":
                nums.append(nums.pop() + nums.pop())
            elif token == "-":
                n2, n1 = nums.pop(), nums.pop()
                nums.append(n1 - n2)
            elif token == "*":
                nums.append(nums.pop() * nums.pop())
            elif token == "/":
                n2, n1 = nums.pop(), nums.pop()
                nums.append(int(n1 / n2))
            else:
                nums.append(int(token))
        
        return nums.pop()