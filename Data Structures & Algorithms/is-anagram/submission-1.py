class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hashMap = {}

        for item in range(len(s)):
            hashMap[s[item]] = hashMap.setdefault(s[item], 0) + 1
            hashMap[t[item]] = hashMap.setdefault(t[item],0) - 1

        for letter in hashMap:
            if hashMap[letter] != 0:
                return False

        
        return True

