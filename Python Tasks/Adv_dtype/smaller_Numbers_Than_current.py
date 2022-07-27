def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        temp = nums.copy()
        temp.sort()
        for i in nums:
            result.append(temp.index(i))
        return result