def binarySearch(arr, x):
    count = 0
    for element in arr:
        if element == x:
            return count
    count += 1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, x)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")