# Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Example 1:
#
# Input: strs = ["act","pots","tops","cat","stop","hat"]
#
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:
#
# Input: strs = ["x"]
#
# Output: [["x"]]
# Example 3:
#
# Input: strs = [""]
#
# Output: [[""]]
# Constraints:
#
# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

def anagram_list(words_list:list[str]) -> list[list[str]]:
    anagram_list_map = {}

    for word in words_list:
        sorted_word = "".join(sorted(word))

        if sorted_word in anagram_list_map:
            anagram_list_map[sorted_word].append(word)
        else:
            anagram_list_map[sorted_word] = [word]

    return list(anagram_list_map.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(anagram_list(strs))


