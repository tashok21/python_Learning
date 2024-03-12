#Length of the last word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       words=s.split()
       print(words)

       if not words:
           return 0
       return len(words[-1])
  
s="     fly me   to   the moon    "
obj=Solution()
func=obj.lengthOfLastWord(s)
print(func)

