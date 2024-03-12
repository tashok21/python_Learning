#Merge two sorted lists

def mergesort(list1,list2):
    merge=[]
    i=j=0
    while i<len(list1)and j<len(list2):
        if list1[i]<list2[j]:
            merge.append(list1[i])
            i+=1
        else:
            merge.append(list2[j])
            j+=1
    while i<len(list1):
        merge.append(list1[i])
        i+=1
    while j<len(list2):
        merge.append(list2[j])
        j+=1

    return merge



list1=[1,2,4]
list2=[1,3,4]
merged_list=mergesort(list1,list2)
print("The sorted array in ascending order",merged_list)



