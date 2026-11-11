import heapq

class MedianFinder:

    def __init__(self):

        # smaller half of numbers
        # we use negatives to make this act like a max heap
        self.small = []

        # bigger half of numbers
        # normal min heap
        self.large = []

    def addNum(self, num: int) -> None:

        # STEP 1:
        # put the new number into small
        heapq.heappush(self.small, -num)

        # STEP 2:
        # move the biggest number from small
        # into large
        biggest_small = -heapq.heappop(self.small)
        heapq.heappush(self.large, biggest_small)

        # STEP 3:
        # if large has more numbers than small,
        # move one back to small
        if len(self.large) > len(self.small):

            smallest_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -smallest_large)

    def findMedian(self) -> float:

        # if small has one extra number,
        # its biggest number is the median
        if len(self.small) > len(self.large):
            return -self.small[0]

        # otherwise both sides are same size,
        # so average the two middle numbers
        left_middle = -self.small[0]
        right_middle = self.large[0]

        return (left_middle + right_middle) / 2