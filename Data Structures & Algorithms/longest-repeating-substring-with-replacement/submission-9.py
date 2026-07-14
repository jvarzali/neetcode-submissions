class Solution:
    def isValid(self, chrs: dict, k: int) -> bool:
        if len(chrs) <= 1:
            return True
        
        count = -max(chrs.values())

        for value in chrs.values():
            count += value
        
        if count > k:
            return False
        return True

    def characterReplacement(self, s: str, k: int) -> int:
        mx, chrs, l, r = 0, {}, 0, 0

        while r < len(s):
            chrs[s[r]] = chrs.get(s[r], 0) + 1
               
            while not self.isValid(chrs, k):
                chrs[s[l]] = chrs.get(s[l]) - 1

                if chrs[s[l]] <= 0:
                    del chrs[s[l]]

                l += 1
            
            r += 1
            if r - l > mx:
                mx = r - l
            print(s[l:r])
            print(mx)
            print(chrs)

        return mx


            