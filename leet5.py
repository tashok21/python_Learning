#To remove the element in-place method

def removeElement(nums,val):
    # newnums=[]
    k=0
    
    for i in range (len(nums)):
        if nums[i]!=val:
            nums[k]=nums[i]
            k+=1
    return k,nums[:k]
    

nums=[3,2,2,3]
val=3
k,new =removeElement(nums, val)
print(f"k={k} newnums {new}")

#Using extra space

def removeElement(nums,val):
    newnums=[]
    
    for i in range (0 , (len(nums)-1)):
        if nums[i]!=val:
            newnums.append(nums[i])
            k=len(newnums)
    return k,newnums
    

nums=[3,2,2,3]
val=3
k,new =removeElement(nums, val)
print(f"k={k} newnums {new}")

