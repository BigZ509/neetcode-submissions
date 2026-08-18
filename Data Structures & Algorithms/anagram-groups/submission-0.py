class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
     
        hashmap = {}

        for index,word in enumerate(strs):
            
            sortedWord = "".join(sorted(word))

            if sortedWord  not in hashmap:
                hashmap[sortedWord] = [word]
            else:
                hashmap[sortedWord].append(word)

        
        return list(hashmap.values())





         
           

            



