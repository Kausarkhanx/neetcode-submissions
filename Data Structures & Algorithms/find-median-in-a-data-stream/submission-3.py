class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        n = len(self.nums)

        if n % 2 == 1:
            return self.nums[n // 2]

        else:
            left_middle = self.nums[n // 2 - 1]
            right_middle = self.nums[n // 2]

            return (left_middle + right_middle) / 2