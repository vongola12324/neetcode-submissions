class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        while True:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif right - left <= 1:
                break
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        return -1
# 0, 2, 5 => mid_n = 2, < t
# 2, 3, 5 => mid_n = 4, > t
# 2, x, 3