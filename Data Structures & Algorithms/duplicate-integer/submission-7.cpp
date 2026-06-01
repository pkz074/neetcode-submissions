#include <unordered_set>
class Solution {
public:
    unordered_set<int> check;
    bool hasDuplicate(vector<int>& nums) {
        for (int num : nums) {
            if(!check.insert(num).second){
                return true;
            }
        }



      return false; 
    }
};