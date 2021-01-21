import sys

s = input("Write some sentence: ")
n1 = int(input("Write delete start index: "))
n2 = int(input("Write delete end index: "))

if n1 > n2:
    print("Fist index more than second", file=sys.stderr)
    exit(1)

if n2 > len(s)-1 or n1 > len(s)-1:
    print("Index(es) are greater than string length", file=sys.stderr)
    exit(1)

print(s[0:n1]+s[n2:len(s)-1])
