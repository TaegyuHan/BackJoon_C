# 2576 홀수

URL : [https://www.acmicpc.net/problem/2576](https://www.acmicpc.net/problem/2576)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

#define INPUT_NUMBER_COUNT 7

typedef struct number
{
    int n; // (1 <= n <= 100)
} Number;

void inputData(Number * Number)
{
    scanf("%d", &Number->n);
}

int sumOddNumber(Number Number, int sum)
{
    if(Number.n%2!=0)
        sum += Number.n;
    
    return sum;
}

int minOddNumber(Number Number, int min)
{
    if(Number.n%2!=0 && min > Number.n)
        min = Number.n;
    
    return min;
}

int main(void)
{
    int i;
    int sum=0, min=100;
		Number Number;

    for(i=0; i<INPUT_NUMBER_COUNT; i++)
    {
        inputData(&Number);
        sum = sumOddNumber(Number, sum);
        min = minOddNumber(Number, min);
    }

    if(sum==0) 
    {
        printf("-1");
        return 0;
    }

    printf("%d\n", sum);
    printf("%d\n", min);

    return 0;
}
```

 숏 코딩

```c
#include <stdio.h>

int main()
{
	int x, r=0, small=100, T=7;
	
	while(T--)
	{
		scanf("%d", &x);
		
		if(x%2==1) 
		{
			r+=x;
			if(small>x) small=x;
		}
	}
	
	if(small==100) printf("-1");
	
	else printf("%d\n%d", r, small);
	
	return 0;
}
```

```c
#include <stdio.h>
int main(){
	int a,i,count = 0,min = 100;
	
	for(i = 0 ; i < 7; i++){
		scanf("%d", &a);
		if(a % 2 == 1){
			count+= a;
			if(a < min) min = a;
		}	
	}
	if(count == 0)printf("-1");
	else printf("%d\n%d",count, min);
}
```

```c
#include <stdio.h>

int main()
{
	int n,i,min=100,sum=0;
	
	for(i=0;i<7;i++)
	{
		scanf("%d",&n);
		if(n%2)
		{
			sum+=n;
			if(min>n)
				min=n;
		}
	}
	if(sum==0)
		printf("-1\n");
	else
		printf("%d\n%d\n",sum,min);
		
}
```