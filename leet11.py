import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=re.sub('[^A-Za-z0-9]','', s)
        result=res.lower()
        print(result)
        palin=result[::-1]
        if str(palin)==result:
            return True
        else:
            return False


s="A man, a plan, a canal: Panama"
obj=Solution()
ret=obj.isPalindrome(s)
print(ret)

