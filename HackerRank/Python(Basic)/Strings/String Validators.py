if __name__ == '__main__':
    s = input()

    isAlphaNumeric = False
    isAlpha = False
    isDigit = False
    isLower = False
    isUpper = False

    for i in range(len(s)):
        if s[i].isalnum():
           isAlphaNumeric = True

        if s[i].isalpha():
            isAlpha = True

        if s[i].isdigit():
            isDigit = True

        if s[i].islower():
            isLower = True

        if s[i].isupper():
            isUpper = True

    print(isAlphaNumeric)
    print(isAlpha)
    print(isDigit)
    print(isLower)
    print(isUpper)