class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""

        for i in s:
            if i.isalnum():
                x += i.lower()

        return x[::-1] == x