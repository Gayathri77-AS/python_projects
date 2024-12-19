#Count of occurence of each characters in sequence
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

#------------------------------------------------------------------------------------------------------------------------
#Swap string without 3rd variable

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
#------------------------------------------------------------------------------------------------------------------------
# Removing space from the string

s = "Try programiz.pro"
result = ""

for i in range(len(s)):
    if s[i] != ' ':
        result += s[i]

print(result)

#Output : Tryprogramizpro

#------------------------------------------------------------------------------------------------------------------------

#Printing charcters in even index

s = "Try programiz.pro"
result = ""

for i in range(len(s)):
    if i%2 == 0:
        result += s[i]

print(result)

#Output:Typormzpo

#------------------------------------------------------------------------------------------------------------------------

#Print each letter twice from the string

s = "Try programiz.pro"
result = ""

for i in range(len(s)):
    result += s[i] + s[i]

print(result)

#Output: TTrryy  pprrooggrraammiizz..pprroo

#------------------------------------------------------------------------------------------------------------------------

#Leap Year Check without Using Modulus Operator

def is_leap_year(year):
    if year // 4 * 4 == year and (year // 100 * 100 != year or year // 400 * 400 == year):
        return True
    else:
        return False

year = 2000
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
#Output: 2000 is a leap year.
    
#Leap Year Check Using Modulus Operator

def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

year = 2010
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
#Output: 2000 is not a leap year.

'''
Hint : (year divisible by 4 AND (year not divisible by 100 or year divisible by 400))
'''   
#------------------------------------------------------------------------------------------------------------------------

#Base Raised to Exponent without Using Built-in Power Function

def power(base, exponent):
    result = 1
    if exponent == 0:
        return 1
    else:
        for i in range(1, exponent + 1):
            result *= base
    return result

base = 2
exponent = 3
print(power(base, exponent))

#Output: 8


#Base Raised to Exponent Using Built-in Power Function

base = 2
exponent = 3
result = pow(base, exponent)
print(result)

#Output: 8

#------------------------------------------------------------------------------------------------------------------------

#Reverse a String without Using Built-in String Reversal Functions

def reverse_string(s):
    char_array = list(s)
    left = 0
    right = len(char_array) - 1
    while left < right:
        char_array[left], char_array[right] = char_array[right], char_array[left]
        left += 1
        right -= 1
    return ''.join(char_array)

s = "Try programiz.pro"
print(reverse_string(s))

#Output: orp.zimargorp yrT

#Reverse a String Using Built-in String Reversal Functions

original = "Try programiz.pro"
reversed_string = original[::-1]
print("Original:", original)
print("Reversed:", reversed_string)

#Output: orp.zimargorp yrT

#------------------------------------------------------------------------------------------------------------------------
#Count Spaces in a String

s = "Hello, World! How are you today?"
count = sum(1 for char in s if char == ' ')
print(count)

#Output: 5

#------------------------------------------------------------------------------------------------------------------------
#Common elements between two arrays

def find_common_elements(arr1, arr2): 
    s1 = set(arr1) 
    common_set = set() 
    for i in arr2: 
        if i in s1: 
            common_set.add(i) 
    return common_set 
arr1 = [1, 2, 3, 4, 5] 
arr2 = [4, 5, 6, 7, 8] 
common_elements = find_common_elements(arr1, arr2) 
print(common_elements)

#Output: [4,5]

#------------------------------------------------------------------------------------------------------------------------
#Finding 1st and last elements in an arraylist

def find_first_and_last(elements):
    if elements:
        first_element = elements[0]
        last_element = elements[-1]
        print(first_element)
        print(last_element)
    else:
        print("Empty List")

arrlist = ["banana", "apple", "cherry", "berry"]
find_first_and_last(arrlist)

'''
Output:banana
berry
'''
#------------------------------------------------------------------------------------------------------------------------




