import matplotlib.pyplot as plt
def linearsearch(arr,target):
  for i in arr:
    if target==arr[i]:
      return i
    else:
      return -1
arr=[1,5,58,12,5,26,19]
target =input("Enter the number: ")
result=linearsearch(arr,target)
time=[.23,.36,.42,.65,.78,.88,.89]
plt.plot(arr,time)
plt.xlabel("Array")
plt.ylabel("Time")
