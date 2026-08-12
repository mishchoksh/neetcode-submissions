class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputArr = []
        zeroCount = 0
        totalProduct = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                totalProduct *= nums[i]
            else:
                zeroCount += 1
        
        for i in range(len(nums)):
            if nums[i] == 0 and zeroCount == 1:
                outputArr.append(int(totalProduct))
            elif zeroCount == 1:
                outputArr.append(0)
            elif zeroCount > 1:
                outputArr.append(0)
            else:
                outputArr.append(int(totalProduct/nums[i]))
        
        return outputArr
        