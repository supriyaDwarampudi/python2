def is_palindrome(s):
    return s==s[::-1]
s='MOM'
a=is_palindrome(s)
if a:
    print(' String is Palindrome ')
else:
    print("String is not a palindrome")

    # output:
    # String is Palindrome 