class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        hashmap = {}

        for index,value in enumerate(nums):
            looking = target - value
            if looking  in hashmap:
                return[hashmap[looking],index]

            hashmap[value] = index