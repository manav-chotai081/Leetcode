class Solution {
public:
    int reverseDegree(string s) {
        int ans = 0;
        int temp = 0;
        for(int i = 1; i <= s.length(); i++){
            temp = 123-s[i-1];
            ans += temp*i;
            
        }
        return ans;
        
    }
};