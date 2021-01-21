s = input("Write some sentence: ")

maxspacecount = 0
spaccount = 0
pos = 0

for i, f in enumerate(s):
    if s[i] == " ":
        spaccount += 1
        if maxspacecount < spaccount:
            maxspacecount = spaccount
            pos = i - maxspacecount + 1
    else:
        spaccount = 0

print(f"Max space repeat {maxspacecount} times in {pos} position")
