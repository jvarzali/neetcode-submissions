class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) < 2):
            return len(s)


        charSet = set(s[0])
        l, r, m = 0, 1, 1

        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                r += 1
                if r - l > m:
                    m = r - l
            else:
                charSet.remove(s[l])
                l += 1       

        return m