class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        myList =[1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            #mmultiply then add to right
            myList[i] = prefix
            prefix *= nums[i]

        postfix= 1
        for i in range(len(nums)-1, -1, -1):

            myList[i] *= postfix
            postfix *= nums[i]

        return myList




        