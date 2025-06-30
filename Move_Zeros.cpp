#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void moveZeroes(vector<int> &nums)
{
    int i=0;
    for(int nonZero=0;nonZero<nums.size();nonZero++){
        if(nums[nonZero]!=0){
            swap(nums[i],nums[nonZero]);
            i++;
        }
    }
}

int main()
{
    vector<int> nums = {0, 1, 0, 3, 12};
    moveZeroes(nums);
    for (auto i : nums)
    {
        cout << i << " ";
    }
    return 0;
}