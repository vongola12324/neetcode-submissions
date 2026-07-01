class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total *= num
        if zero_count > 1:
            total = 0            
        
        if zero_count == len(nums):
            return [0] * zero_count
        else:
            l = []
            for num in nums:
                if zero_count > 0:
                    if num != 0:
                        l.append(0)
                    else:
                        l.append(total)
                else:
                    l.append(int(total/num))
            return l