class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mx, chrs, l, r , maxf = 0, {}, 0, 0, 0

        for r in range(len(s)):
            chrs[s[r]] = chrs.get(s[r], 0) + 1
            maxf = max(maxf, chrs[s[r]])
               
            while (r - l + 1) - maxf > k:
                chrs[s[l]] = chrs.get(s[l]) - 1
                l += 1

            mx = max(r - l + 1, mx)

        return mx


            