class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_count = 0
    
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j]==nums[i] and i<j:
                    good_count+=1

        return good_count
        