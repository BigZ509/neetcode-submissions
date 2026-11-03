class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mySet = {}

        for index, num  in  enumerate(nums):

            need =  target - num

            if need in mySet:
                return [mySet[need],index]

            mySet[num] = index




        