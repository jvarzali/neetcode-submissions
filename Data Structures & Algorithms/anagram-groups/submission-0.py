class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = [[strs[0]]]

        for word in strs[1:]:
            wordAppended = False
            for wordList in anagrams:
                if self.isAnagram(word, wordList[0]):
                    wordList.append(word)
                    wordAppended = True
                    break

            if not wordAppended:
                anagrams.append([word])                

        return anagrams

    def isAnagram(self, str1: str, str2: str) -> bool:
        for char in str1:
            index = str2.find(char)
            if index == -1:
                return False
            str2 = str2[:index] + str2[index+1:]
        
        if len(str2) > 0:
            return False
        
        return True
