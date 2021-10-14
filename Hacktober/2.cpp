#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
    
    int num;
    cout<<"Enter length of array."<<endl;
    cin>>num;
    cout<<"Enter num"<<endl;
    int sum;
    cin>>sum;

    int arr[num];

    for(int i=0;i<num;i++){
        cin>>arr[i];
    }

    sort(arr, arr+num);

    int start = 0;
    int end = num-1;

    int count=0;
    vector<int> found;
    while(start<end){
        if(arr[start] + arr[end] ==  sum){
            found.push_back(arr[start]);
            found.push_back(arr[end]);
            count++;
            break;
        }
        else if(arr[start] + arr[end] > sum){
            end--;
        }
        else if(arr[start] + arr[end] < sum){
            start++;
        }
    }

    if(count==1){
        cout<<"Found"<<endl;
        for(int i=0;i<found.size();i++){
            cout<<found.at(i)<<end;
        }
    }
    else{
        cout<<"Not Found"<<endl;
    }






    return 0;
}
