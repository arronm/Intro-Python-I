"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]
b = [2, 4, 1, 7, 9]

print(b[2:-2])

# Output the second element: 4:
print(a[1])

# Output the second-to-last element: 9
print(a[-2])

# Output the last three elements in the array: [7, 9, 6]
print(a[-3:])

# Output the two middle elements in the array: [1, 7]
# Note: Technically here you would want to get the length of the list, divide, then slice
#   but for simplicities sake, I think the exercise is asking for the following:
print(a[2:-2])

# Better to find mid element(s) of an array
import math
mid = math.floor(len(a) / 2)
if (mid % 2) == 1:
  mid -= 1
print(a[mid:-mid])

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:-1])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[7:12])
