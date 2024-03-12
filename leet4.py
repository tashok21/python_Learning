#Removing the duplicates
def removeDuplicates(nums):
    dupli=[]
    for i in range (0,(len(nums)-1)):
         if nums[i]!=nums[i-1]:
              dupli.append(nums[i])
    dupli.append(nums[-1])          
    return dupli

nums=[1,1,2,3,4,4,4,5,7,8,8]
dup=removeDuplicates(nums)
print("The new list", dup)

# #"""
# 1. List is sorted
# 2. List is an int
# 3. any other types should return error\
# #
# """
# output = [1,2,3,4,5,6,7]

def remove_duplicates(input: list):
  #output = []
  j = 0
  n=len(input)-1
  for i in range (0, n):
    if input[i] != input[i-1]:
      input[j] = input[i]
      j += 1
      if input[:-1] != input[:-2]:
          input[:j]=input[:-1]
  return input[:j]

input = [1,1,2,3,3,4,4,4,5,7,7]
ret = remove_duplicates(input)
print("The list after removing the duplicates", ret)
