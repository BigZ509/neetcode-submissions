class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmapS = {}
        hashmapT = {}
    


        for value in range(len(s)):
            
            hashmapS[s[value]] = hashmapS.get(s[value], 0) + 1
            hashmapT[t[value]] = hashmapT.get(t[value], 0) + 1


        for keys in hashmapS:
            if hashmapS[keys] != hashmapT.get(keys,0):
                return False

        return True

                
        
   
            
     


