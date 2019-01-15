#include<stdio.h>
#include<string.h>

int main()
{
	char arr1[10];
	char arr2[10];
	strcpy(arr1,"abcdefgh");
	puts(arr1);
	strncpy(arr2,"abcdefgh",4);
	puts(arr2);
	char arr3[10]={'a','b','c','d','\0'};
	strcat(arr3,"efgh");
	puts(arr3);
	printf("%d\n",strcmp("abcd","efgh"));
	printf("%d\n",strcmp("abcd","abcd"));
	printf("%d\n",strcmp("efgh","abcd"));
	printf("--------------\n");
	printf("%ld\n",strlen(arr1));
	return 0;
}
