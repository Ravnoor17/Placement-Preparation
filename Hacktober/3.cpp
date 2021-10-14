#include<bits/stdc++.h>
using namespace std;


int main(){
    cout<<"Enter length of array"<<endl;
    int len;
    cin>>len;
    cout<<"Enter length of second array"<<endl;
    int len1;
    cin>>len1;

    int arr[len];
    int arr1[len1];
    cout<<"Enter first array"<<endl;
    for(int i=0;i<len;i++){
        cin>>arr[i];
    }
    cout<<"Enter second array"<<endl;
    for(int i=0;i<len1;i++){
        cin>>arr1[i];
    }

    unordered_set<int> set;
    unordered_set<int>::iterator itr;

    for(int i=0;i<len1;i++){

        set.insert(arr1[i]);
        
    }   

    vector<int> notPresent;

    for(int i=0;i<len;i++){
        itr = set.find(arr[i]);

        if(itr == set.end()){
            notPresent.push_back(arr[i]);
        }
    }


    for(int i=0;i<notPresent.size();i++){
        cout<<notPresent.at(i)<<" ";
    }

    return 0;   
}