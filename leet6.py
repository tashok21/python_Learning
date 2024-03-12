def stringIndex(strval,val):
   k=len(val)
   for i in range (len(strval)):
        if val!=strval[i:k]:
           return -1
        else:
           return 0
        
  
     

haystack="sadbutsad"
needle="sad"
ran=stringIndex(haystack,needle)
print(ran)
print(f"Explanation: {needle} occurs at index 0 and 6.The first occurrence is at index 0, so we return 0")

#For example 2

def stringIndex(strval,val):
   k=len(val)
   for i in range (len(strval)):
        if val!=strval[i:k]:
           return -1
        else:
           return 0
        
  
     

haystack="sadbutsad"
needle="sad0"
ran=stringIndex(haystack,needle)
print(ran)
print(f"Explanation: {needle}  did not occur in {haystack} so we return -1.")

