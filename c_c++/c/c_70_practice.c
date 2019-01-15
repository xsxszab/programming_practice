#include<stdio.h>

typedef struct student
{
	int id;
	char name[20];
	struct information
	{
		int grade;
		int class;
	}status;
}stu;

int main()
{
	stu a;
	scanf("%d%s%d%d",&a.id,a.name,&a.status.class,&a.status.grade);
	printf("%d\n%s\n%d\n%d\n",a.id,a.name,a.status.class,a.status.grade);
	return 0;
}
