class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #wow thats new for me
        for s in strs:
            count= [0] * 26 #where we have at most 26 characters
            for ch in s:
                count[ord(ch)-ord('a')]+=1 #
            res[tuple(count)].append(s) #apparently lists cant be keys but tuples can be, smth about immutables and stuff
        return list(res.values())