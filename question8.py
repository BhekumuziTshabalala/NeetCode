# Longest Consecutive Sequence
# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
#
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
#
# You must write an algorithm that runs in O(n) time.
#
# Example 1:
#
# Input: nums = [2,20,4,10,3,4,5]
#
# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].
#
# Example 2:
#
# Input: nums = [0,3,2,5,4,6,1,1]
#
# Output: 7
# Constraints:
#
# 0 <= nums.length <= 1000
# -10^9 <= nums[i] <= 10^9


def consecutive_sequence(nums: list) -> int:
    sequence_length: list[int] = []

    sorted_nums = sorted(nums)

    sequence = 1

    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] - sorted_nums[i-1] == 1 :
            sequence += 1
        elif sorted_nums[i] - sorted_nums[i-1] == 0:
            continue
        else:
            sequence_length.append(sequence)
            sequence = 1

    sequence_length.append(sequence)
    return max(sequence_length)


def longestConsecutiveChatGPT(nums: list[int]) -> int:
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # Only start if it's the beginning of a sequence
            current = num
            count = 1

            while current + 1 in num_set:
                current += 1
                count += 1

            longest = max(longest, count)

    return longest


if __name__ == '__main__':
    nums = [2,20,4,10,3,4,5]
    print(consecutive_sequence(nums))
    print(longestConsecutiveChatGPT(nums))
