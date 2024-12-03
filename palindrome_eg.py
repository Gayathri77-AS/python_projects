def is_palindrome_reversed(string):
    """Method 1: Using string reversal"""
    return string == string[::-1]

def is_palindrome_iterative(string):
    """Method 2: Using two-pointer technique"""
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_recursion(string):
    """Method 3: Using recursion"""
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome_recursion(string[1:-1])

def is_palindrome_stack(string):
    """Method 4: Using a stack"""
    stack = list(string)
    for char in string:
        if char != stack.pop():
            return False
    return True

def is_palindrome_deque(string):
    """Method 5: Using deque"""
    from collections import deque
    d = deque(string)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# Main Function
def best_palindrome_method(string):
    methods = {
        "Reversed String Method": is_palindrome_reversed,
        "Two-pointer Iterative Method": is_palindrome_iterative,
        "Recursion Method": is_palindrome_recursion,
        "Stack Method": is_palindrome_stack,
        "Deque Method": is_palindrome_deque,
    }
    
    # Checking all methods
    for name, method in methods.items():
        result = method(string)
        print(f"{name}: {'Palindrome' if result else 'Not a Palindrome'}")
    
    # Choosing the best method
    # Best method reasoning:
    # - The Two-pointer iterative method is the most optimal because:
    #   - It checks characters one by one from both ends, giving a time complexity of O(n).
    #   - It doesn’t use any extra space like the stack or recursion methods, which have O(n) space complexity.
    #   - It's simple and easy to understand while being very efficient.
    
    return "Two-pointer Iterative Method is the best due to its O(n) time complexity and O(1) space complexity."

# Input
string = input("Enter the string to check: ")

# Output
print(best_palindrome_method(string))
