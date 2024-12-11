s = "Try programizzzzzzz.pro"
result = []
count = 1

for i in range(len(s)):
    if i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
    else:
        result.append(s[i] + str(count))
        count = 1

print("".join(result))


# Output : T1r1y1 1p1r1o1g1r1a1m1i1z6.1p1r1o1

------------------------------------------------------------

# Swap string without 3rd variable

s = "Try Programiz Pro "
t = "Hope For Best"

# Concatenate s and t
s = s + t

# Extract original value of s
t = s[:len(s) - len(t)]

# Extract original value of t
s = s[len(t):]

# Print the results
print(s)
print(t)

'''
 Output : Hope For Best 
          Try Programiz Pro
'''
------------------------------------------------------------

# Removing space from the string
s = "Try programiz.pro"
result = ""

for i in range(len(s)):
    if s[i] != ' ':
        result += s[i]

print(result)
------------------------------------------------------------

