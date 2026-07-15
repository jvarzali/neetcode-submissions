class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charCount, zeros, l, r = {}, 0, 0, 0
        
        for char in s1:
            charCount[char] = charCount.get(char, 0) + 1

        while r < len(s2):
            if r - l < len(s1):
                if s2[r] in charCount.keys():
                    count = charCount.get(s2[r])
                    charCount[s2[r]] = count - 1
                    if count == 0:
                        zeros -= 1
                    elif count == 1:
                        zeros += 1
                r += 1
            else:
                if s2[l] in charCount.keys():
                    count = charCount.get(s2[l])
                    charCount[s2[l]] = count + 1
                    if count == 0:
                        zeros -= 1
                    elif count == -1:
                        zeros += 1
                l += 1
            if zeros == len(charCount):
                return True
        
        return False
            

