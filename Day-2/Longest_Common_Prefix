// https://leetcode.com/problems/longest-common-prefix/

//cpp solution

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
//         string ans="";
//         string s=*min_element(strs.begin(),strs.end());//min element
        
//         for(int i=0;i<s.size();i++){
//             for(int j=0;j<strs.size();j++){
//                 if(s[i]!=strs[j][i]){
//                     return ans;
//                 }
                    
                
//             }
//             ans.push_back(s[i]);
//         }
//         return ans;
        
        //this time we will consider the first element as the min element and start comparing the char.
        
        string ans="";
        string s=strs[0];
        
        for(int i=0;i<s.size();i++){
            for(int j=1;j<strs.size();j++){
                if(i>=strs[j].size() ||s[i]!=strs[j][i]){
                    return ans;
                }
            }
            ans.push_back(s[i]);
        
        }
        
        return ans;
        
        
    }
};
