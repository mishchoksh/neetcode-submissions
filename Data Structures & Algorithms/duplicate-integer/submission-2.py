class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = {};
        for val in nums:
            if val in found:
                return True;
            else:
                found[val] = 1;
        return False

        
        