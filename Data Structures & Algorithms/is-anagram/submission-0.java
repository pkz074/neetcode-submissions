class Solution {
    public boolean isAnagram(String s, String t) {
        // If lengths differ, they can't be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Assuming ASCII character set or just lowercase letters
        // For lowercase letters only, we could use size 26
        int[] charCount = new int[26]; 
        
        // Process both strings in a single pass
        for (int i = 0; i < s.length(); i++) {
            charCount[s.charAt(i) - 'a']++;  // Increment for chars in s
            charCount[t.charAt(i) - 'a']--;  // Decrement for chars in t
        }
        
        // Check if all counts are zero
        for (int count : charCount) {
            if (count != 0) {
                return false;
            }
        }
        
        return true;
    }
}