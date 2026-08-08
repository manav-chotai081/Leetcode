class Solution {
public:
    int scoreOfString(string s) {
        int ans = 0;
        int temp = 0;
        for(int i = 0; i < s.length()-1; i++){
            temp = int(s[i]) - int(s[i+1]);
            if(temp < 0){
                temp *= -1;
                ans+=temp;
            }else{
                ans += temp;
            }
        }
        return ans;
    }
};