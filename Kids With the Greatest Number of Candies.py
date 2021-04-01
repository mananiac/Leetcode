class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = candies[0]
        arr = candies
        for i in range(len(candies)):
            if candies[i]>=max:
                max=candies[i]
        for i in range(len(candies)):
            if (candies[i] + extraCandies) < max:
                arr[i] = False
            elif (candies[i] + extraCandies) >= max:
                arr[i] = True
        return arr
        
            