//https://leetcode.com/problems/length-of-last-word/
//c++ code solution

class Solution {
public:
    int lengthOfLastWord(string s) {
        int count = 0;
        int n = s.size();
        int i = 0;
        while(i<n){
            if(s[i]!=' '){
                count++;
                i++;
            }else{
                /// current char is a space
                while(i<n && s[i]==' ')i++;
                
                if(i==n){   /// end of string
                    return count;
                }else{
                    count = 0;
                }
                
            }
        }
        
        return count;
        
    }
};



//python code solution

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reverse_Str=s[::-1]
        reverse_Str=reverse_Str.strip()
        last_word=""
        for i in range(len(reverse_Str)):
            if reverse_Str[i]==" ":
                return len(last_word)
            else:
                last_word+=reverse_Str[i]
        return len(last_word)
                
                
             
