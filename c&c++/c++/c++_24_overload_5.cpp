#include<iostream>
#define SIZE 10

using namespace std;


class array
{
	public:
		array()
		{
			int i;
			for(i=0;i<SIZE;i++)
				list[i]=i+1;
		}
		int& operator[](int i)
		{
			if(i>SIZE)
			{
				cout<<"worng"<<endl;
				return list[SIZE-1];
			}
			return list[i];
		}
	private:
		int list[SIZE];
};

int main()
{
	array arr;
	cout<<arr[0]<<endl;
	cout<<arr[2]<<endl;
	cout<<arr[20]<<endl;
	return 0;
}
