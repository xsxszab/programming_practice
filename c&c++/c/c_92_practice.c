#include<stdio.h>

int main()
{
	int list[10]={0};
	int *p=list;
	printf("%d\n%d\n%d\n",list,&list,*list);
	printf("-------------\n");
	printf("%d\n%d\n",list,p);
	printf("-------------\n");
	printf("%d\n%d\n",p+1,&list[1]);
	printf("-------------\n");
	return 0;
}
