class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        strS = {}
        strT = {}

        if len(s) != len(t):
            return False

        
        for letter in s:
            strS[letter] = strS.get(letter, 0) + 1
        for letter in t:
            strT[letter] = strT.get(letter, 0) + 1

        if strS == strT:
            
            return True

        return False

        


        
       


