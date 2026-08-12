class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        maxHeap = []

        for num, freq in count.items():
            heapq.heappush(maxHeap, (-freq, num))

        res = []

        for _ in range(k):
            freq, num = heapq.heappop(maxHeap)
            res.append(num)

        return res
        