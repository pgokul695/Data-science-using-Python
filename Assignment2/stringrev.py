def rev_num(n):
    return int(str(n)[::-1])

num = int(input("Enter a number to reverse: "))
print("Reversed number:", rev_num(num))
