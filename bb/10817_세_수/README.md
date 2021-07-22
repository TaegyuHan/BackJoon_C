# 10817 세 수

URL : [https://www.acmicpc.net/problem/10817](https://www.acmicpc.net/problem/10817)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct intLIst
{
    int number[3];
} IntLIst;

void inputData(IntLIst * IL)
{
    int i;
    for(i=0; i<3; i++)
        scanf("%d", &IL->number[i]);

    return;
}

void bubbleSort(int list[], int len)
{
    int i, j;
    int temp;
    for(i=0; i<len; i++)
    {
        for(j=0; j<len; j++)
        {
            if(list[i] >= list[j])
            {
                temp = list[i];
                list[i] = list[j];
                list[j] = temp;
            }
        }
    }
}

int main(void)
{
    IntLIst IL;

    inputData(&IL);
    bubbleSort(IL.number, 3);
    printf("%d", IL.number[1]);
    return 0;
}
```

숏코딩

```c
#include <stdio.h>
int main(void)
{
	int a,b,c,d;
	scanf("%d %d %d",&a,&b,&c);
	if(a>b)
	{
		if(b>c)
			d=b;
		else if(c>a)
			d=a;
		else
			d=c;
	}
	else
	{
		if(c>b)
			d=b;
		else if(a>c)
			d=a;
		else
			d=c;
	}
	printf("%d",d);
}
```

```c
main(a,b,c){
    scanf("%d %d %d",&a,&b,&c);
    if((a>=b&&c>=a)||(a>=c&&b>=a)){
        printf("%d\n",a);
    }
    else if((b>=a&&c>=b)||(b>=c&&a>=b)){
        printf("%d\n",b);
    }
    else{
        printf("%d\n",c);
    }
}
```

```c
#include<stdio.h>

int main(void)
{
	int a,b,c,num;
	scanf("%d %d %d",&a,&b,&c);
	if(a<b)
	{
		num=a;
		a=b;
		b=num;
	}
	if(a<c)
	{
		num=a;
		a=c;
		c=num;
	}
	if(b<c)
	{
		num=b; 
		b=c;
		c=num;
	}
	printf("%d\n",b);
}
```