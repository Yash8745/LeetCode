#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

void reverseArray(vector<int> &arr,int m){
    
    int front=m+1;
    int back=arr.size()-1;
    while(front<=back){
        swap(arr[front],arr[back]);
        front++;
        back--;
    }
    
    



}

int main()
{
    std::vector<int> vec={0,1,2,3,4,5,6,7,8,9};
    int m=5;
    
    reverseArray(vec,m);
    for(auto i: vec){
        cout<<i<<"  ";
    }
    cout<<endl;

    return 0;
}