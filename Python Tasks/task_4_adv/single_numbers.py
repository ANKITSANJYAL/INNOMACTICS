class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ll=[]
        f=0
        l=len(nums)-1
        while f<l:
            if nums.count(nums[f])==1:
                ll.append(nums[f])
                
            if nums.count(nums[l])==1:
                ll.append(nums[l])
				
            if len(ll)==2:
                return ll
            f=f+1
            l=l-1
        return ll
        