class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sol = 0
        for _ in nums:
            sol ^= _
        return sol
        