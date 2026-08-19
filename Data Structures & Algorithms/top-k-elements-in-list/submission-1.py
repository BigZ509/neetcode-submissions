class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}

        for num in nums:
            if num not in seen:
                seen[num] = 1

            else:
                seen[num] += 1

        maxItem = sorted(seen.items(), key = lambda pair: pair[1], reverse = True)
        
        values = []

        for item in maxItem[:k]:
            values.append(item[0])

        return values




            
        