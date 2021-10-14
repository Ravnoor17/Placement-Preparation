//overloading of unary operator !
#include<iostream>
using namespace std;
class test
{
	int a,b,c;
	public: void getdata(int x,int y,int z)
	        {
	        	a=x;
	        	b=y;
	        	c=z;
			}
			void display()
			{
				cout<<a<<endl;
				cout<<b<<endl;
				cout<<c<<endl;
			}
			void operator !()
			{
				a=!a;
				b=!b;
				c=!c;
			}
};


int main()
{
	test t;
	t.getdata(2,0,12);//anything except 0 is equivalent to 1
	t.operator !();
   // !t;   /*both are correct way to call overloaded operator*/
	t.display();
}
