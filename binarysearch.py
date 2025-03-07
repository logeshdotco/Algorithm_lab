import matplotlib.pyplot as plt
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
my_list = [1,15,22,88,100,123]
target = 100
index = binary_search(my_list, target)

if index != -1:
    print(f"The number",target," is found at index",index)
else:
    print(f"The number",target," is not found in the list")
time=[.49,.52,.96,.99,.98,.96]
plt.plot(my_list,time)
plt.xlabel("my_list")
plt.ylabel("time")  
