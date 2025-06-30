#include <iostream>
#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>
using namespace std;

void reverse(vector<int> &nums,int start,int end)
{
    for (int i = start,j=end ; i < j; i++,j--){
        swap(nums[i],nums[j]);
    }
}
void rotate(vector<int> &nums, int k)
{
    reverse(nums,0,nums.size()-1-k%nums.size());  
    reverse(nums,nums.size()-k%nums.size(),nums.size()-1);  
    reverse(nums,0,nums.size()-1);  

}

int main()
{
    vector<int> nums = {-1};
    int k = 2;
    // reverse(nums,0,nums.size()-1);
    rotate(nums, k);
    
    for (auto i : nums)
    {
        cout << i << " ";
    }
    return 0;
}