class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r =0, len(heights)-1
        Marea=0
        while l<r:
            area= min(heights[l], heights[r]) * (r-l)
            Marea= max(Marea,area)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return Marea
        #i honestly struggled the most with understanding how to calculate it but it's not a hard problem. its just a normal sliding window, i had horrible reading comprehension though!! iig