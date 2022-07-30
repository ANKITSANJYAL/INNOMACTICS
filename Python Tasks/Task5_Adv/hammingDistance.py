class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x and y:
            if (x%2==0 and y%2==1) or (x%2==1 and y%2==0):
                ans +=1
            x = x//2
            y = y//2
        while x:
            if x%2==1:
                ans+=1
            x = x//2
        while y:
            if y%2==1:
                ans+=1
            y = y//2
        return ans