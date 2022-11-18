lst=[-10, -5, 10, 23, 45, 56, 78, 89 ,1]
target = 89

# def findTarget(lst, target):
#   for i in range(0,len(lst)):
#     if lst[i]==target:
#       return i
#   return -1

# find = findTarget(lst,target)
# print(find) #O(n)

# def findTarget2(lst, target):
#   for i in range(0,len(lst)/2):
#     if lst[i]==target:
#       return i
#     if lst[len(lst)-i-1] ==target:
#       return len(lst)-i-1
    
#   return -1

def findTarget3(lst,target):
  
  mid = lst[int(len(lst)//2)]
  mid_index = int(len(lst)//2)
  for i in range(0,mid_index):
    if target<mid:
      mid = lst[mid_index -1]
      mid_index = mid_index-1
    if target>mid:
      mid = lst[mid_index +1]
      mid_index = mid_index+1
    if target==mid:
      return mid_index
  return -1

find = findTarget3(lst,target)
print(find) 
