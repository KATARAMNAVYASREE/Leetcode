class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n= len(nums)
        if n == 0:
            return [-1,-1]

        def findelement(val: bool) -> int:
            left,right = 0, n-1
            firsttrueidx = -1
            while left <= right:
                mid = (left+right)//2
                if val:
                    feasible = nums[mid] > target
                else:
                    feasible = nums[mid] >= target
                if feasible:
                    firsttrueidx = mid
                    right= mid-1
                else:
                    left = mid+1
            return firsttrueidx
        firstidx = findelement(False)
        if firstidx == -1 or nums[firstidx] != target:
            return [-1,-1]
        afterlastidx = findelement(True)
        if afterlastidx == -1:
            lastidx = n-1
        else:
            lastidx=afterlastidx-1
        
        return(firstidx , lastidx)



        # def first():
        #     low, high = 0, len(nums) - 1
        #     ans = -1

        #     while low <= high:
        #         mid = (low + high) // 2
        #         if nums[mid] == target:
        #             ans = mid
        #             high = mid - 1      
        #         elif nums[mid] < target:
        #             low = mid + 1
        #         else:
        #             high = mid - 1
        #     return ans

        # def last():
        #     low, high = 0, len(nums) - 1
        #     ans = -1

        #     while low <= high:
        #         mid = (low + high) // 2

        #         if nums[mid] == target:
        #             ans = mid
        #             low = mid + 1       # Search right
        #         elif nums[mid] < target:
        #             low = mid + 1
        #         else:
        #             high = mid - 1

        #     return ans

        # return [first(), last()]