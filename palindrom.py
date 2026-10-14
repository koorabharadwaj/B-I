

def palindrome(num):
    original = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    if original == rev:
        print("Palindrome")
    else:
        print("Not a palindrome")
n = int(input("Enter a number: 121"))
palindrome(n)
