class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_arr = [nums[0]]   #assigning the variable with the list with just 1st element on given list as we dont want to add anything on this
        for i in nums[1:]:    # iterating over all the elements in the list or an array
            sum_arr.append(i+sum_arr[-1])  # adding the element on that list equal number of times as its index on the list
        return sum_arr                  # returning final listr