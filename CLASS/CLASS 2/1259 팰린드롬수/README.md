# 1259 팰린드롬수

URL : [https://www.acmicpc.net/problem/1259](https://www.acmicpc.net/problem/1259)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>
int i;

int main(void) {

    char intList[100000];
    char check;
    int strNum;

    while(1)
    {
        check=1;
        strNum=0;
        scanf("%s", intList);

        if(intList[0]=='0') break;
        
        for(i=0; intList[i]!=NULL; i++)
        {
            strNum++;
        }

        for(i=0; i<strNum/2; i++)
        {
            if(intList[i]==intList[strNum-i-1])
                continue;
            if(intList[i]!=intList[strNum-i-1])
            {
                check=0;
                break;
            }
        }

        if(check==0) printf("no\n");
        if(check==1) printf("yes\n");

    }

    return 0;
}
```

숏코딩

```c
main(t,n,r){for(;scanf("%d",&n)&&n;){t=n;r=0;while(t){r=r*10+t%10;t/=10;}puts(n-r?"no":"yes");}}
```

```c
#include <stdio.h>

int main(void)
{
	int num = 1, reverse = 0, temp = 0;
	while (num != 0)
	{
		scanf("%d", &num);
		if (num == 0)
			break;
		temp = num;
		while (temp != 0)
		{
			reverse = reverse * 10;
			reverse = reverse + temp % 10;
			temp = temp / 10;
		}
		if (num == reverse)
			printf("yes\n");
		else
			printf("no\n");
		reverse = 0;
	}
	return 0;
}
```

```c
#include <stdio.h>

int array[10000];
int rev(int n);

int main ()
{
	int i,j,ind;
	for (i=0;i+1;i++)
	{
		scanf("%d", &array[i]);
		if (array[i]==0) {
			ind=i;
			break;
		}
	}
	for (j=0;j<ind;j++)
	{
		array[j]==rev(array[j]) ? printf("yes\n") : printf("no\n");
	}
}

int rev(int n)
{
	int result=0;
	while (n)
	{
		result=result*10+n%10;
		n/=10;
	}
	return result;
}
```