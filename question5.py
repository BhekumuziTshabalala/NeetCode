# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
#
# Please implement encode and decode
#
# Example 1:
#
# Input: ["neet","code","love","you"]
#
# Output:["neet","code","love","you"]
# Example 2:
#
# Input: ["we","say",":","yes"]
#
# Output: ["we","say",":","yes"]
# Constraints:
#
# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.
from operator import indexOf


def encode(strings : list) -> str:
    result = ""
    for i in strings:
        result +=   str(len(i)) + "#" + i
    return result




def decode(code : str) -> list:
    words = []
    code_ = code

    while True:
        i = None
        try:
            i = code_.index("#")
        except ValueError:
            return words

        if code_[:i].isdigit():
            start = i + 1
            end = start +  int(code[:i])
            words.append(code_[start:end])
            code_ = code_[end:]


code_v =  encode(["VeryLongStringWithoutAnySpacesOrSpecialCharactersRepeatedManyTimesVeryLongStringWithoutAnySpacesOrSpecialCharactersRepeatedManyTimes"])
print(code_v)
print(decode(code_v))