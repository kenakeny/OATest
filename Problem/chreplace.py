class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts={}
        res=0 #max length found
        l=0
        maxFR=0 ## Most frequent character count
        for r in range(len(s)):
            counts[s[r]]= 1+counts.get(s[r],0)
            maxFR=max(maxFR,counts[s[r]])
            while (r-l+1) -maxFR>k:
                counts[s[l]]-=1
                l+=1
            res=max(res, r- l +1)
        return res