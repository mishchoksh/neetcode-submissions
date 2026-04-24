class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = set();
        for val in nums:
            if val in found:
                return True;
            else:
                found.add(val);
        return False

        
        