#include<iostream>
using namespace std;
int main()
{
	int n,size,k=0;
	cout<<"Enter order of the matrix : ";
	cin>>n;
	size= (n*(n+1)/2);
	int *A=new int [size];
	for(int i=0;i<size;i++)
	{
		cout<<"enter element "<<i+1<<" of the matrix (row-major) : ";
		cin>>A[i];
	}
	cout<<"Upper triangular matrix is :\n";
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(i<=j)
			{
				cout<<A[k]<<"\t";
				k++;
			}
			else
			cout<<"0\t";
		}
		cout<<endl;
	}
	cout<<"Lower triangular matrix is :\n";
	k=0;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(i>=j)
			{
				cout<<A[k]<<"\t";
				k++;
			}
			else
			cout<<"0\t";
		}
		cout<<endl;
	}
	return 0;
}
