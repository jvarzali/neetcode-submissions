class Solution:
    def isValid(self, s: str) -> bool:
        opens = []

        openDict = {
            "{" : "}",
            "[" :"]",
            "(" : ")"
        }    

        for char in s:
            if char in openDict.keys():
                opens.append(char)
            elif not opens:
                return False
            else:
                if char == openDict.get(opens[-1]):
                    opens.pop()
                else:
                    return False
        
        if opens:
            return False
        
        return True

