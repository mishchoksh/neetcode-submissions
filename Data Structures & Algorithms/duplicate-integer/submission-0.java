class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> dict = new HashMap<>();
        for (int val : nums) {
            if (dict.containsKey(val)) {
                return true;
            } else {
                dict.put(val, 1);
            }
        }
        return false;
    }
}