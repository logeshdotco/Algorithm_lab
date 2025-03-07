def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
arr=[4,3,2,765,5,89]
insertion_sort(arr)
print(arr)
time=[.26,.36,.39,.45,.49,.52]
plt.plot(my_list,time)
plt.xlabel("list")
plt.ylabel("time")
plt.show()
