import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums

        # turn nums into a min heap
        heapq.heapify(self.heap)

        # keep only the k biggest numbers
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:

        # add the new number
        heapq.heappush(self.heap, val)

        # if there are more than k numbers,
        # remove the smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # smallest of the k biggest = kth largest
        return self.heap[0]