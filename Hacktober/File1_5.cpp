#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
int main()
{
	fstream ob;
	string str;
	string c;
	ob.open("File1.txt",ios::app);
	cout<<"Enter text to add in file"<<endl;
	getline(cin,str);
	ob<<endl<<str;
	ob.close();
	ob.open("File1.txt",ios::in);
	while(!ob.eof())
	{
		getline(ob,c);
		cout<<c;
	}
	ob.close();
	return 0;
	
	
}
