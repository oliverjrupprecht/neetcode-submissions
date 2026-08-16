class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for n in nums:
            if n in count:
                count[n] += 1 
            else:
                count[n] = 1 
        
        tupled = [(key, value) for key, value in count.items()]
        srt = sorted(tupled, key=lambda i : i[1])

        sived = []
        for i in range(len(srt) -k, len(srt)):
            sived.append(srt[i][0])
        
        return sived
        

