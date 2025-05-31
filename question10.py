# Two Integer Sum II
# Given an array of integers numbers that is sorted in non-decreasing order.
#
# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
#
# There will always be exactly one valid solution.
#
# Your solution must use
# O(1)
# O(1) additional space.
#
# Example 1:
#
# Input: numbers = [1,2,3,4], target = 3
#
# Output: [1,2]
# Explanation:
# The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].
#
# Constraints:
#
# 2 <= numbers.length <= 1000
# -1000 <= numbers[i] <= 1000
# -1000 <= target <= 1000
from operator import index


def two_sum(nums: list[int], target: int) -> list[int]:
    left =  nums[0]
    right = nums[-1]

    while left < right:
        if left + right == target:
            return [nums.index(left), nums.index(right)]

        if right >= target:
            right = nums[nums.index(right) - 1]
        else:
            left = nums[nums.index(left) + 1]

if __name__ == '__main__':
    numbers = [-5, -3, 0, 2, 4, 6, 8]
    target = 5
    print(two_sum(numbers, target))

