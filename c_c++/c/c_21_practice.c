#include<stdio.h>

int main()
{
	int n;
	scanf("%d",&n);
	getchar();
	char a,b,c,s;
	while(n--)
	{
		scanf("%c%c%c",&a,&b,&c);
		getchar();
		if(a>b)
        {
            s=a;
            a=b;
            b=s;
        }
        if(a>c)
        {
            s=a;
            a=c;
            c=s;
        }
        if(b>c)
        {
            s=b;
            b=c;
            c=s;
        }
		printf("%c %c %c\n",a,b,c);
	}
	return 0;
}
