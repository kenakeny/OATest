class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we hash all of these first
        counters ={}
        for n in nums:
            counters[n] = 1+ counters.get(n,0) # if key doesnt exist return zero, else add +1

        heap=[]
        # we use min heap
        for num in counters:
            heapq.heappush(heap,(counters[num],num)) #tuple pushing (freq, num)
            if len(heap) >k: 
                heapq.heappop(heap) #remove less frequent element
        res=[]
        for i in range (k):
            res.append(heapq.heappop(heap)[1]) #we're getting the number, 0 is the frequency :3
        return res[::-1]
        #nlogk i think along with o N