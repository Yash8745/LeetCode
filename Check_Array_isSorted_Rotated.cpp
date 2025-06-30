#include <iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

bool isSorted(vector<int> &nums)
{
    for (int i = 0; i < nums.size() - 1; i++)
    {
        if (nums[i] > nums[i + 1])
        {
            return false;
        }
    }
    return true;
}

void reverse(vector<int> &nums, int start, int end)
{
    for (int i = start, j = end; i < j; i++, j--)
    {
        swap(nums[i], nums[j]);
    }
}
void rotate(vector<int> &nums, int k)
{
    reverse(nums, 0, nums.size() - 1 - k % nums.size());
    reverse(nums, nums.size() - k % nums.size(), nums.size() - 1);
    reverse(nums, 0, nums.size() - 1);
}

bool check(vector<int> &nums)
{
    for (int i = 0; i < nums.size(); i++)
    {
        if (isSorted(nums) == true)
        {
            return true;
        }
        rotate(nums, 1);
    }
    return false;
}

int main()
{
    vector<int> nums = {9, 3, -1, 3, 5, 7};
    int k = 2;

    string result = check(nums) ? "iS tRUE" : "FAlse";

    cout << result;

    return 0;
}