#include<stdio.h>

#define PI 3.1415926
#define True 1
#define False 0
#define sec_per_year (60*60*24*365)
#define numbers 1,\
				2,\
				3
#define max(x,y) ((x)>(y)?(x):(y))
#define concat(a,b) (a##b)
#define test(a) #a

int main()
{
	int i;
	if(True)
		printf("%lf\n",PI);
	printf("%d\n",sec_per_year);
	int list[]={numbers};
	for(i=0;i<3;i++)
		printf("%d ",list[i]);
	printf("\n");
	printf("%d\n",max(1,2));
	printf("%d\n",concat(12,34));
	char *str=test(abcd);
	printf("%s\n",str);
	return 0;
}
