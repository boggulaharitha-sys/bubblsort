def bubbleSort(arr):
    n=len(arr)
    for i in range(n-1,-1,-1):
        
      for j in range(i):
        if arr[j]>arr[i]:
            arr[i],arr[j]=arr[j],arr[i]
      return arr
arr=[3,5,1,8,7,2,100,4,9]
print(bubbleSort(arr))