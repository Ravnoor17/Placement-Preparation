//overloading of binary operators + & -
#include<iostream>
using namespace std;
class test
{
	int a,b;
	public: 
	        void getdata(int x,int y)
	        {
	        	a=x;
	        	b=y;
			}
			void display()
			{
				cout<<"a= "<<a<<endl;
				cout<<"b= "<<b<<endl;
			}
			test operator+(test t)
			{
				test T;
				T.a=a+t.a;
			    T.b=b+t.b;
				return T;
			}
			test operator-(test t)
			{
				test T;
		    	T.a=a-t.a;
				T.b=b-t.b;
				return T;
			
			}
};
int main()
{
	test t1,t2,t3,t4;
	t1.getdata(10,20);
	t2.getdata(30,40);
	t3=t1+t2;
//	t3=t1.operator+(t2);
	t4=t1-t2;
//	t4=t1.operator-(t2);
    t3.display();
    t4.display();
	return 0;
}
