class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}

        # Count frequencies
        for num in nums:
            elements[num] = elements.get(num, 0) + 1
        
        # Sort by frequency (highest first)
        tuples = sorted(elements.items(), key=lambda x: x[1], reverse=True)

        # Collect top k
        out = []
        for x in range(len(tuples)):
            if len(out) == k:
                return out
            out.append(tuples[x][0])

        return out