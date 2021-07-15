# 1978 소수 찾기

URL : [https://www.acmicpc.net/problem/1978](https://www.acmicpc.net/problem/1978)

```c
#include <stdio.h>

int main() {

    char Number; // 1 <= Number <= 100
    char NumberCheck;
    unsigned short i;
    unsigned short TempNumber, ResultSum=0;

    scanf("%d", &Number);

    while(Number--)
    {
        scanf("%d", &TempNumber);

        if(TempNumber==1) continue;

        NumberCheck = 1;
        for(i=2; i<TempNumber; i++)
        {
            if(TempNumber%i==0)
            {
                NumberCheck = 0;
                break;
            }
        }
        if(NumberCheck==1)
        {
            ResultSum+=1;
        }
    }

    printf("%d", ResultSum);

  return 0;
}
```

숏 코딩

```c
#include <stdio.h>
int main()
{
    int i,j,n,a,A;scanf("%d",&n);getchar();A=n;
    for(i=0;i<n;i++){
        scanf("%d",&a);getchar();
        if(a==1){A--;continue;}
        for(j=2;j*j<=a;j++)if(a%j==0){A--;break;}
    }printf("%d",A);
}
```

```c
#include <stdio.h>
int main(void)
{
	int N, i,j, a,count,prime=0;
	scanf("%d", &N);
	for (i = 0; i < N; i++)
	{
		scanf("%d", &a);
		count = 0;
		for (j = 1; j <= a; j++)
			if (a % j == 0)
				count++;
		if (count == 2)
			prime++;
	}
	printf("%d", prime);
}
```

```c
#include<stdio.h>
int main()
{
	int m,cnt=0,n;
	scanf("%d", &m);
	while (m--)
	{
		int p = 1;
		scanf("%d", &n);
		if (n == 1)p = 0;
		for (int i = 2; i*i <= n; i++)
			if (!(n%i))
			{
				p = 0;
				break;
			}
		if (p)cnt++;
	}
	printf("%d\n", cnt);
	return 0;
}
```