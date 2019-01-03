#include<stdio.h>
int arr[10]={0};
void sort(int len)
{
	int i,j;
	int index,temp;
	for(i=0;i<len;i++)
	{
		index=i;
		for(j=i+1;j<len;j++)
		{
			if(arr[j]<arr[index])
				index=j;
		}
		temp=arr[i];
		arr[i]=arr[index];
		arr[index]=temp;
	}
}
int main()
{
	int i;
	for(i=0;i<10;i++)
		scanf("%d",&arr[i]);
	sort(10);
	for(i=0;i<10;i++)
		printf("%d ",arr[i]);
	return 0;
}
