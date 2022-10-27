class Solution {
public:
    static bool cmp(int a, int b){
        return a > b;
    }
    vector<vector<int>>ans; map<vector<int>,int>m;
    void func(int i,vector<int>a,int sum,vector<int>v,int t){
    
        if(sum == t){
            if(m[v] == 0){
            ans.push_back(v);
            m[v]++;
            }
            return;
        }
        if(i == a.size()){
            return;
        }
        if(sum > t){return;}
        
        v.push_back(a[i]);
        
        func(i,a,sum + a[i],v,t);
       
         
        v.pop_back();
        func(i + 1,a,sum,v,t);
  
    
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int>v;
        sort(v.begin(),v.end(),cmp);
        func(0,candidates,0,v,target);
        return ans;
    
    }
};