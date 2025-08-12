#reversre a string without using slicing
def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

# Test
print(reverse_string("Selenium"))  # muineleS
