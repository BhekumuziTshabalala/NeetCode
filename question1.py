# Given integer array , return true if any value appears atleast twice in the array, and return false if every element is distinct
# Time Complexity O(n)
def is_duplicates(nums : list ) -> bool:
    return len(set(nums)) != len(nums)
