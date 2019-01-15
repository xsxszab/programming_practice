#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct student
{
	//int id;
	//char name[20];
	//int gender;
	int score;
	struct student *next;
} stu;

stu* init()
{
	stu *p;
	p=(stu*)malloc(sizeof(stu));
	memset(p,0,sizeof(stu));
	return p;
}

stu* build(stu* head)
{
	stu* node;
	node=(stu*)malloc(sizeof(stu));
	head->next=node;
	scanf("%d",&node->score);
	node->next=NULL;
	return node;
}

void print(stu* head,int n)
{
	int i;
	stu* temp=head->next;
	for(i=0;i<n;i++)
	{
		printf("%d\n",temp->score);
		temp=temp->next;
	}
}

void insertSort(stu* node)
{
    if(node->next==NULL)
    {
		printf("the list is empty\n"); 
        return;
    }
	if(node->next->next==NULL)
	{
		printf("no need to sort\n");
		return;
	}
    stu *head,*p1,*pre1,*p2,*pre2,*temp;
    head=node;
    pre1=head->next;
    p1=pre1->next;
    int flag;

    while(p1!=NULL)
    {
        flag=1;
        temp=p1;
        for(pre2=head,p2=pre2->next;p2!=p1;pre2=pre2->next,p2=p2->next)
        {
            if(p2->score>p1->score) 
            {
                p1=p1->next;
                pre1->next=p1;
                pre2->next=temp;
                temp->next=p2;
                flag=0;
                break;
            }
        }
        if(flag)
        {
            pre1=pre1->next;
            p1=p1->next;
        }
    }
}

int main()
{
	int n;
	printf("input the number of students\n");
	scanf("%d",&n);
	int i;
	stu *p=init();
	stu *temp=p;
	for(i=0;i<n;i++)
		temp=build(temp);
	printf("before:\n");
	print(p,n);
	insertSort(p);
	printf("after:\n");
	print(p,n);
	return 0;
}
