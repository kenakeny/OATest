class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r= 1, max(piles)
        result=r
        while l<=r:
            k=( l + r ) //2
            totalT=0
            for p in piles:
                totalT+=math.ceil(float(p)/k) # K is the devouring rate rate we tryn test!!
            if totalT<=h:
                result=k
                r=k-1
            else:
                l=k+1
        return result
#interesting problem ngl i got confused cuz im grinding late at night