#include<iostream>

using namespace std;

typedef struct Node
{
	int data;
	Node *left;
	Node *right;
}node;

node* create()
{
	node* head;
	int temp;
	cin>>temp;
	if(temp==0)
		head=NULL;
	else
	{
		head=new node;
		head->data=temp;
		head->left=create();
		head->right=create();
	}
	return head;
}

void print(node* head)
{
	if(head==NULL)
		return;
	cout<<head->data<<endl;
	print(head->left);
	print(head->right);
}

int main()
{
	node* head=create();
	print(head);
	return 0;
}
