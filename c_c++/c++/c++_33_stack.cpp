#include <iostream>
 
using namespace std;

class node 
{
public:
	int data;
	node * next;
 
};
 
class stack
{
private:
	node *head;
	node *curr;
	int length;
 
public:
	stack()
	{
		head = NULL;
		length=0;
	}
 
	void push(int num)
	{
		node* temp;
		temp=new node();
		temp->data=num;
		length++;
		if(head==NULL)
		{
			temp->next=head;
			head=temp;
			curr=temp;
		}
		else
		{
			temp->next=curr;
			curr=temp;
		}
	}
	
	int pop()
	{
		if(isEmpty())
		{
			cout<<"stack is empty"<<endl;
			return -1;
		}
		node* temp=new node();
		temp=curr;
		length--;
		int data=curr->data;
		delete(temp);
		curr=curr->next;
		//cout<<data<<endl;
		return data;
	}
	int len()
	{
		return length;
	}
	bool isEmpty()
	{
		if(length)
			return false;
		return true;
	}
	void clear()
	{
		while(length)
			pop();
	}
};

int main()
{
	int i;
	stack stack1;
	cout<<stack1.isEmpty()<<endl;
	cout<<"-----------"<<endl;
	stack1.push(1);
	stack1.push(2);
	stack1.push(3);
	stack1.push(4);
	stack1.push(5);
	stack1.push(6);
	for(i=0;i<4;i++)
		cout<<stack1.pop()<<endl;
	cout<<"-----------"<<endl;
	stack1.clear();
	cout<<stack1.isEmpty()<<endl;
	return 0;
}
