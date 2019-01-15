#include<stdio.h>
#include<stdlib.h>
#include<memory.h>

char str[8];

long func(int n)
{
	int i;
	long ans=1;
	for(i=1;i<n;i++)
		ans*=10;
	return ans;
}

void transfer(int num)
{
	memset(str,0,sizeof(str));
	int i=0,j=0;
	int temp=num>=0?num:-num;
	if(num<0)
	{
		str[0]='-';
		num=-num;
		i++;
	}
	while(temp)
	{
		temp/=10;
		j++;
	}
	while(j)
		str[i++]=(num/func(j--)%10)+'0';
	str[i]='\0';
}

typedef struct student
{
	int id;
	int score;
	struct student *next;
}stu;

stu* init()
{
	stu *p;
	p=(stu*)malloc(sizeof(stu));
	if(p==NULL)
	{
		printf("error\n");
		exit(1);
	}
	return p;
}

stu* build(stu* head)
{
	stu *p;
	p=(stu*)malloc(sizeof(stu));
	if(p==NULL)
	{
		printf("error\n");
		exit(1);
	}
	head->next=p;
	scanf("%d%d",&p->id,&p->score);
	p->next=NULL;
	return p;
	
}

void print_all(stu* head)
{
	printf("--------------\n");
	while(head->next!=NULL)
	{
		head=head->next;
		printf("student id:%d\nstudent score:%d\n",head->id,head->score);
		printf("--------------\n");
	}
}

void insert(stu* head,int n)
{
	int i;
	for(i=0;i<n;i++)
		if(head!=NULL)
			head=head->next;
		else
			{
				printf("wrong\n");
				exit(1);
			}
	stu *temp;
	temp=head->next;
	stu *p;
	p=(stu*)malloc(sizeof(stu));
	if(p==NULL)
	{
		printf("error\n");
		exit(1);
	}
	head->next=p;
	scanf("%d%d",&p->id,&p->score);
	head->next=p;
	p->next=temp;
}

void delete(stu* head,int n)
{
	int i;
	for(i=1;i<n;i++)
		if(head!=NULL)
			head=head->next;
		else
			{
				printf("wrong\n");
				exit(1);
			}
	stu* temp=head->next;
	head->next=head->next->next;
	free(temp);
}

void write(stu* head)
{
	FILE* fp;
	if((fp=fopen("./student.txt","w"))==NULL)
	{
		printf("wrong\n");
		exit(1);
	}
	fputs("students information\n**************\n",fp);
	while(head->next!=NULL)
	{
		head=head->next;
		fputs("student id:",fp);
		transfer(head->id);
		fputs(str,fp);
		fputs("\n",fp);
		fputs("student score:",fp);
		transfer(head->score);
		fputs(str,fp);
		fputs("\n",fp);
		fputs("-----------\n",fp);
	}
	fclose(fp);
	printf("done\n-------------\n");
}

int main()
{
	int n,i;
	printf("input the numer of students\n");
	scanf("%d",&n);
	stu *head=init();
	stu *temp=head;
	printf("build the list\n");
	for(i=0;i<n;i++)
	{
		temp=build(temp);
	}
	print_all(head);
	printf("done\n------------\n");
	int op;
	printf("input what to do\n");
	printf("1:print list\n2:insert node\n3:delete node\n4:write to file\n");
	while(scanf("%d",&op)!=EOF)
	{
		switch(op)
		{
			case 1:
				print_all(head);
				break;
			case 2:
				printf("input the place to insert\n");
				scanf("%d",&n);
				insert(head,n);
				break;
			case 3:
				printf("input the place to delete\n");
				scanf("%d",&n);
				delete(head,n);
				break;
			case 4:
				printf("writing to file...\n");
				write(head);
				break;
			default:
				printf("wrong input\n");
				break;
		}
	}
	return 0;
}
