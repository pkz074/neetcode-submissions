
class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Create a HashMap to store numbers we've seen
        HashMap<Integer, Boolean> seen = new HashMap<Integer, Boolean>();
        
        // Loop through each number in the array
        for (int i = 0; i < nums.length; i++) {
            // Check if we've seen this number before
            if (seen.containsKey(nums[i])) {
                // We found a duplicate
                return true;
            }
            
            // Add this number to our HashMap
            seen.put(nums[i], true);
        }
        
        // If we get here, no duplicates were found
        return false;
    }
}