class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            location = t.find(i)
            if location == -1:
                return False
            t = t[:location] + t[location+1:]

        if len(t) > 0:
            return False
        
        return True