#include<iostream>

using namespace std;

typedef struct Node
{
	int num;
}node;

int main()
{
	node* node1;
	node1=new node;
	node1->num=1;
	node* node2;
	node2=node1;
	cout<<node1->num<<endl;
	cout<<node2->num<<endl;
	cout<<"-----------"<<endl;
	delete node2;
	cout<<node1->num<<endl;
	cout<<node2->num<<endl;
	cout<<"-----------"<<endl;
	node* node3;
	node3=new node;
	node3->num=2;
	node* node4;
	node4=new node;
	node4=node3;
	cout<<node3->num<<endl;
	cout<<node4->num<<endl;
	cout<<"-----------"<<endl;
	delete node4;
	cout<<node3->num<<endl;
	cout<<node4->num<<endl;
	cout<<"-----------"<<endl;
	return 0;
}
