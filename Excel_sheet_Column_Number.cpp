// https://leetcode.com/problems/excel-sheet-column-number/
class Solution {
public:
    int titleToNumber(string columnTitle) {
        int ans=0;
        int length=columnTitle.size();
        long long power=1;
        for (int i=length-1;i>=0;i--){
            ans+=(columnTitle[i]-64)*power;
            power=power*26;
        }
        return ans;
    }
};

