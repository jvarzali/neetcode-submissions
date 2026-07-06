class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) < 2):
            return len(s)

        l, r, m = 0, 1, 1

        while r < len(s):
            print(s[l:r] + " " + str(l) + " " + str(r) + " " + str(m))
            if s[r] not in s[l:r]:
                r += 1
                if r - l > m:
                    m = r - l
            else:
                l += 1       
            print(s[l:r] + " " + str(l) + " " + str(r) + " " + str(m))
            print()

        return m