class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        for word in strs:
            sortedWords = "".join(sorted(word))
            if sortedWords not in hashmap:
                hashmap[sortedWords] = [word]
            else:
                hashmap[sortedWords].append(word)

        return list(hashmap.values())


