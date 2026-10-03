from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product_of_whole_list = prod(nums)

        products = []
        for i in range(len(nums)):
            if nums[i]==0:
                # need to remove 0 from list but first create a copy
                copied_list = nums.copy()
                copied_list.remove(0)
                products.append(prod(copied_list))
            else:
                products.append(product_of_whole_list // nums[i])
        return products
        