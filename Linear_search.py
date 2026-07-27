def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

data = [42, 17, 89, 5, 23, 11, 74]
target_value = 23

result = linear_search(data, target_value)
print("ELement found at index:",result)
