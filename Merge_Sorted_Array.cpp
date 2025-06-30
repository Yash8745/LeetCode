#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void merge(vector<int> &vec1,int left,int mid,int right){
    int n1=mid-left+1;
    int n2=right-mid;

    std::vector<int> L(n1);
    std::vector<int> R(n2);

    for (int i = 0; i < n1; i++) {
        L[i] = vec1[left + i];
    }
    for (int j = 0; j < n2; j++) {
        R[j] = vec1[mid + 1 + j];
    }
    int i = 0, j = 0, k = left;

    // Merge the temporary array back in to vector[left...right]
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            vec1[k] = L[i];
            i++;
        } else {
            vec1[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of L[], if any
    while (i < n1) {
        vec1[k] = L[i];
        i++;
        k++;
    }

    // Copy the remaining elements of R[], if any
    while (j < n2) {
        vec1[k] = R[j];
        j++;
        k++;
    }
}



void merge_sort(vector<int> &nums1,int left,int right){
    if(left<right){
        int mid=left+(right-left)/2;
        merge_sort(nums1,left,mid);
        merge_sort(nums1,mid+1,right);

        merge(nums1,left,mid,right);
    }
}



void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
{
    int counter = n-1;
    int nums1_size=nums1.size();
    

    for(int i=nums1_size-1; nums1[i]==0;i--){
        nums1[i]=nums2[counter];
            counter--;  
    }
    

    
    for (auto i : nums1)
    {
        cout << i << " ";
    }
    merge_sort(nums1,0,nums1_size-1);
    cout<<endl;
    for (auto i : nums1)
    {
        cout << i << " ";
    }
}

int main()
{
    vector<int> nums1 ={0};
    vector<int> nums2 = {1};

    int m = 0;
    int n = 1;
    merge(nums1,m,nums2,n);
    cout<<endl<<"This is the final returning value of num1"<<endl;
    for (auto i : nums1)
    {
        cout << i << " ";
    }

    return 0;
}