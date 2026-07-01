class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        base = 0
        for base in range(0, len(nums)-2):
            if nums[base] > 0:
                break
            if base > 0 and nums[base] == nums[base - 1]:
                continue

            target = -nums[base]
            left, right = base + 1, len(nums) - 1

            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    result.append([nums[base], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:    # 跳過重複 left
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # 跳過重複 right
                        right -= 1
                    left += 1
                    right -= 1
                elif s > target:
                    right -= 1
                else:
                    left += 1
        return result