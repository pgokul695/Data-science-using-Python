#Program to check weather a number is palindrome or not
n= input("Enter a number: ")
if n == n[::-1]:
    print(f"{n} is a Palindrome")
else:
    print(f"{n} is not a Palindrome")
