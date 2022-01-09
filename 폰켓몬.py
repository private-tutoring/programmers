def solution(nums):
   a = len(nums)//2
   nums = set(nums)
   if len(nums) >= a:
       return a
   else: return len(nums)



print(solution([3,3,3,2,2,4]))