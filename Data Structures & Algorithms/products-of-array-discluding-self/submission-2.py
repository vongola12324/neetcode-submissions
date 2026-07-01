class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        length = len(nums)
        left_product = [1]*len(nums)
        right_product = [1]*len(nums)
        for index in range(length):
            if index > 0:
                # Left
                left_product[index] = left_product[index-1] * nums[index-1]
                # Right
                right_product[len(nums) - 1 - index] = right_product[len(nums) - index] * nums[len(nums) - index]
        
        return [left_product[index]*right_product[index] for index in range(length)]