class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mySet = {}

        for word in strs: # loop through words
            newWord = sorted(word, reverse = False) #sort each letter

            newWord = "".join(newWord) #join them into a word 

            if newWord in mySet: #see if sorted word is in hashMap
                mySet[newWord].append(word) #adds new word with the word as the index
            else:
                mySet[newWord] = [word] # creates a new instance of the word assign it a list

        return list(mySet.values()) #retrun the valued as a list


            



        
            





        

            
        