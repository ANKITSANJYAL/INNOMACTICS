class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        return [i+extraCandies >= highest for i in candies] 
        #iterating through all the candies and checking if adding extracandies makes them greater than highest or not and returning respective boolean
    