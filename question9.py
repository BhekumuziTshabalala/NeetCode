import string
from string import punctuation


def isPalindrome(s: str) -> bool:

    working_string = ''
    lower_s = s.lower()

    for char in lower_s:
        if char in string.ascii_lowercase:
            working_string += char
    return "".join(working_string[::-1]).lower() == working_string.lower()


if __name__ == '__main__':
    print(isPalindrome("Was it a car or a cat I saw?"))
