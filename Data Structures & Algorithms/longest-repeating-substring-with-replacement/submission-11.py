class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mx, chrs, l, r = 0, {}, 0, 0

        while r < len(s):
            chrs[s[r]] = chrs.get(s[r], 0) + 1
               
            while (r - l + 1) - max(chrs.values()) > k:
                chrs[s[l]] = chrs.get(s[l]) - 1

                if chrs[s[l]] <= 0:
                    del chrs[s[l]]

                l += 1
            
            r += 1
            if r - l > mx:
                mx = r - l

        return mx


            