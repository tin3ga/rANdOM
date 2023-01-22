ascii_values = [int(num) for num in input("enter ascii space separated values: ").split()]
words = ""
for value in ascii_values:
    words += chr(value)
print(words)
