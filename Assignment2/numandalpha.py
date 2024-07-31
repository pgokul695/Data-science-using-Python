s = "abc123"

alpha = 0
num = 0

for c in s:
    if c.isalpha():
        alpha += 1
    elif c.isdigit():
        num += 1

print("Total number of alphabets:", alpha)
print("Total number of digits:", num)
