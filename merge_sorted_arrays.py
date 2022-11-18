arr1 = [0,2,10]
arr2 = [1,3,5,8,19]

def mergeSortedArrays(arr1,arr2):
  arr3 = arr1+arr2
  arr3.sort()
  return arr3

arr = mergeSortedArrays(arr1,arr2)
print(arr)