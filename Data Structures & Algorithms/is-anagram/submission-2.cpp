#include <unordered_map>
class Solution {
public:
    bool isAnagram(string s, string t) {
            unordered_map<char,int> map1;
            unordered_map<char,int> map2;

        if (s.size() != t.size()){
            return false;
        }
        for (char s1 : s){
            map1[s1]++;
        }
        for (char s2 : t){
            map2[s2]++;
        }

        if (map1 == map2){
            return true;
        } else {
            return false;
        }
    return false;
    }
};
