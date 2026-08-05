class Solution:
    def groupAnagrams(self, strs):
        arr = []
        for s in strs:
            key = sorted(s)
            arr.append([key,s])
        arr.sort()
        res = []
        i = 0
        n = len(arr)
        while i < n:
            group = [arr[i][1]]
            j = i + 1
            while j < n and arr[i][0] == arr[j][0]:
                group.append(arr[j][1])
                j += 1
            res.append(group)
            i = j
        return res