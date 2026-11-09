class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            our_target = target - num
            if our_target in seen:
                return [seen[our_target], i]
            seen[num] = i
        return []