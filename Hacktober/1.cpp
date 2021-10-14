#include<iostream>
#include<vector>
#include<iterator>
#include<map>
using namespace std;


int main(){

    int length;
    cout<<"Enter length of the array"<<endl;
    cin>>length;

    int arr[length];
    map<int, int> myMap;
    map<int, int>::iterator itr;
    
    for(int i=0;i<length;i++){
        cin>>arr[i];
    }

    for(int i=0;i<length;i++){
        itr = myMap.find(arr[i]);

        if(itr == myMap.end()){
            myMap.insert({arr[i], 1});
        }
        else{
            itr->second += 1;
        }
    }

    vector<int> repeatingElements;

    for(itr = myMap.begin();itr != myMap.end();itr++){

        cout<<itr->first<<" "<<itr->second<<endl;

        if(itr->second > 1){
            repeatingElements.push_back(itr->first);
        }
    }

    cout<<"All repeating elements are : "<<endl;

    for(int i=0;i<repeatingElements.size();i++){
        cout<<repeatingElements.at(i)<<" ";
    }







    return 0;
}