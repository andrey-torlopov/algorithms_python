class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in d:
                d[num] = i
            else:
                return [d[n], i]
        return []

# [2,7,11,15], target = 9
# Output: [0,1]


s = Solution()
print(s.twoSum(nums=[2, 7, 11, 15], target=9))
