class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}

        for index,num in enumerate(nums):
            difference = target - num
            if difference in hashMap:
               return[hashMap[difference],index]
            hashMap[num] = index
            
            
        

        

                
            

            