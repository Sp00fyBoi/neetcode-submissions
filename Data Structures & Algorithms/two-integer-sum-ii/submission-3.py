class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum_v = numbers[left] + numbers[right]
            if sum_v == target:
                return [left + 1 , right + 1]
            if sum_v < target:
                left += 1
                continue
            if sum_v > target:
                right -= 1
                continue 
        return [left , right]