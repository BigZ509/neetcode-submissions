class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mySet = {}
       

        for num in nums: #loop through
            if num in mySet: #increment the number count if its in
                mySet[num] += 1 #increment it by 1
            else:
                mySet[num] = 1 #store it with count 1

        
        sortedNum = sorted(mySet, key = mySet.get, reverse = True) #reverses my keys array

        
        return sortedNum[:k] #slice form beginning up to k








        