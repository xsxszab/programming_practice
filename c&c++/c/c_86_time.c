#include<stdio.h>
#include<time.h>

int main()
{
	time_t t;
	struct tm *p;
	time(&t);
	p=gmtime(&t);
	printf("%d\n",p->tm_sec);
    printf("%d\n",p->tm_min);
    printf("%d\n",8+p->tm_hour);
    printf("%d\n",p->tm_mday);
    printf("%d\n",1+p->tm_mon);
    printf("%d\n",1900+p->tm_year);
    printf("%d\n",p->tm_yday);
	return 0;
}
