class Solution:
    
    def search(self, nums: list, target: int) -> int:
        
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1

        return -1       