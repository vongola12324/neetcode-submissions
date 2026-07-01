class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        s = numbers[left] + numbers[right]
        while s != target and left < right:
            if s > target:
                right -= 1
            else:
                left += 1
            s = numbers[left] + numbers[right]
            
        return [left+1, right+1]