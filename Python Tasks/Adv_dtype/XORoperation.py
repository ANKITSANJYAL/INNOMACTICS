class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        final = fornow = start
        for i in range(1, n):
            fornow += 2  
            final = final ^ fornow
        return final