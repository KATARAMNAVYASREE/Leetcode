class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        temp=[]
        def backtrack():
            if len(temp)==len(nums):
                result.append(temp[:])
                return
            for num in nums:
                if num in temp:
                    continue
                temp.append(num)
                backtrack()
                temp.pop()

        backtrack()
        return result