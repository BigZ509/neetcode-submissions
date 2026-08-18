class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        hashmap = {}

        for key,value in enumerate(nums):
            targetLookup = target - value


            if targetLookup in hashmap:
                return [hashmap[targetLookup],key]

            hashmap[value] = key
              

             
        