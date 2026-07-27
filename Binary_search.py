def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
data = [12, 23, 34, 45, 56, 67, 78, 89, 90]

target_value = 45

result = binary_search(data, target_value)
print("Element found at index:",result)
