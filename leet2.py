# # #palindrome

def palindrom_Check(arr):
    clean_array=''.join(char.lower() for char in arr if char.isalnum())
    arr_size=len(clean_array)
    start,end =0, arr_size-1
    while start<end:
       if clean_array[start]!=clean_array[end]:
           return False
       start=start+1
       end=end-1
    return True

arr=["687"]
print(palindrom_Check(arr))

# #By reversing the srting
a="madam"
rev_string=a[::-1]
print("The reverser is ",rev_string)
if str(rev_string) == str(a):
    print(rev_string,"it is a palindrome")
else:
    print("Not a palindrome")

#Number 
a=[1,2,3,4]
str=a[::-1]
print(str)

a= "Trisha" 
s=a[::-1] 
print(str(s))