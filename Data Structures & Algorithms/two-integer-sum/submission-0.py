class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = False
        arr = [0, 0]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    arr[0] = i
                    arr[1] = j
                    return arr
        