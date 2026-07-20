class Solution:
    def minWindow(self, s: str, t: str) -> str:
        r, mn, chars = 0, "", {}

        for char in t:
            chars[char] = chars.get(char, 0) + 1

        valid = len(chars.keys())

        print(chars)

        for l in range(len(s)):
            while r < len(s) and valid != 0:
                if s[r] in chars.keys():
                    chars[s[r]] = chars[s[r]] - 1
                    if chars[s[r]] == 0:
                        valid -= 1
                r += 1
            
            print(chars)
            print(valid)
            
            if valid == 0 and (r - l < len(mn) or len(mn) == 0):
                mn = s[l:r]
            
            if s[l] in chars.keys():
                chars[s[l]] = chars[s[l]] + 1
                if chars[s[l]] == 1:
                    valid += 1

            print(chars)
            print(valid)

            if valid == 0 and (r - l < len(mn) or len(mn) == 0):
                mn = s[l:r]

            print()

        return mn
        
