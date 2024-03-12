def inSort(nums,val):
    left,right=0, len(nums)-1
    while left<=right:
        mid=left+(right - left)//2
        if nums[mid]==val:
            return mid
        elif nums[mid]<val:
            left=mid+1
        else:
            right=mid-1
    return left


nums=[1,3,5,6]
target=2
func=inSort(nums,target)
print(func)
