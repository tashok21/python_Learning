# def arr_sum(num, target):
#     hash_map={}
#     print("Hash map",hash_map)
#     for i,num in enumerate(num):
#         print("Printing i",i,"num",num)
#         complement=target-num
#         print("complement",complement,target,num)
#         if complement in hash_map:
#             a=[hash_map[complement],i]
#             return a
#         hash_map[num]=i
#         print("final",i, num,)

# num=[2,7,11,15,6]
# target=17
# print(arr_sum(num,target))

class Solution:
    def twoSum(self,num,target):
        hashmap={}

        for i,val in enumerate(num):
            diff=target-val
            if diff in hashmap:
                return[hashmap[diff],i]
            hashmap[val]=i
            

num=[2,7,11,15,6]
target=17
obj=Solution()
ret=obj.twoSum
print(ret(num,target))