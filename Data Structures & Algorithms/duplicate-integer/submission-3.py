class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in range(len(nums)):

            if nums[num] not in seen:
                seen.add(nums[num])
            
            elif nums[num] in seen:
                    return True

        return False
