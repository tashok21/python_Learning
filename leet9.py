#Add binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=int(a,2)
        y=int(b,2)
        sumbin= x+y
        #String rep of binary number
        c=bin(sumbin)
        #Onky the binary number
        d=bin(sumbin)[2:]
        return c,d


a="1010"
b="1011"
obj=Solution()
ret1,ret=obj.addBinary(a,b)
print(ret1,ret)