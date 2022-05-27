//Write a function that reverses a string. The input string is given as an array of characters s.
//You must do this by modifying the input array in-place with O(1) extra memory.

//python code
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.''
        """
        start = 0
        end = len(s)-1
        while start <= end :
            tmp = s[start]
            s[start] = s[end]
            s[end]= tmp
            start+=1
            end-=1

//cpp code

class Solution {
public:
    void reverseString(vector<char>& s) {
//         method -1

        stack<char> st;
        for(int i=0;i<s.size();i++){
            //pushing ele in stack
            st.push(s[i]);
        }
        //pop every char
        for(int i=0;i<s.size();i++){
            s[i]=st.top();
            st.pop();
        }
    
// method -2

    int st=0;
    int e=s.size()-1;
        
        while(st<=e){
            swap(s[st],s[e]);
            st++;
            e--;
        }
        
    }
};
