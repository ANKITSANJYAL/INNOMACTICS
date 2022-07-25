class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        for i in range(n):
            arr.extend((nums[i],nums[i+n]))   #using the extend function to add an array to the existing array
        return arr
            