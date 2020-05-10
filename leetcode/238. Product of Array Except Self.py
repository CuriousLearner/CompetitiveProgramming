# https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        left_val = 1
        right_val = 1

        left_index = 0
        right_index = len(nums) - 1

        for i in range(len(nums)):
            result[left_index] *= left_val
            result[right_index] *= right_val

            left_val *= nums[left_index]
            right_val *= nums[right_index]

            left_index += 1
            right_index -= 1

        return result
