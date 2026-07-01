class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        base = 0
        for base in range(0, len(nums)-2):
            target = -nums[base]
            left = base+1
            right = len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    result.add((nums[base], nums[left] ,nums[right]))
                    right -= 1
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    left += 1
        return [list(r) for r in result]