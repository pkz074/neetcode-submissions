
class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Boolean> solut = new HashMap<Integer, Boolean>();
        for(int i = 0; i < nums.length; i++){
            if (solut.containsKey(nums[i])){
                return true;
            }
            solut.put(nums[i], true);
        }
        return false;
     }
}

