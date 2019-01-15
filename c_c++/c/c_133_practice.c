#include<stdio.h>
#include<string.h>

int main()
{
	char a[]="abcd";
	char b[]="abcd\0";
	char c[]="ab\0cd";
	char d[10]="abcd";
	char e[]="123\045";
	char *f="123\045";
	printf("%ld %ld\n",strlen(a),sizeof(a));
	printf("%ld %ld\n",strlen(b),sizeof(b));
	printf("%ld %ld\n",strlen(c),sizeof(c));
	printf("%ld %ld\n",strlen(d),sizeof(d));
	printf("%ld %ld\n",strlen(e),sizeof(e));
	printf("%ld %ld\n",strlen(f),sizeof(f));
	return 0;
}
