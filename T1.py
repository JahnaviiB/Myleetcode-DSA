def ispalindrome(s):
    if(s==s[::-1]):
        return "Palindrome"
    else:
        return "Noo"

s = input("Enter the string")
print(ispalindrome(s))

