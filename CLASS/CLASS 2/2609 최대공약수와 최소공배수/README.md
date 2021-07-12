# 2609 최대공약수와 최소공배수

URL : [https://www.acmicpc.net/problem/2609](https://www.acmicpc.net/problem/2609)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int i;

int main(void) {

    int num1, num2;
    int sml, big;
    int result;

    scanf("%d %d", &num1, &num2);

    sml = (num1 < num2) ? num1 : num2;
    big = (num1 > num2) ? num1 : num2;

    // 최대 공약수
    for(i=1; i<=sml; i++)
    {
        if(num1%i==0 && num2%i==0)
            result=i;
    }
    printf("%d\n", result);

    // 최소 공배수
    for(i=1; ; i++)
    {
        if((sml*i)%big == 0)
        {   
            result=sml*i;
            break;
        }
    }
    printf("%d\n", result);

    return 0;
}
```

숏 코딩

```c
i=1e5;main(n,m){for(scanf("%d%d",&n,&m);n%--i|m%i;);printf("%d %d",i,n*m/i);}
```

```c
int main()
{
	int a,b,i,max=1;
	scanf("%d %d",&a,&b);
	for(i=1;i<=a;i++)
	{
		if(a%i==0 && b%i==0)
			if(max<i)
				max=i;
	}

	printf("%d %d",max,a*b/max);
}
```

```c
#include <stdio.h>
int a, b, mod, p, q;
int main(void) {
	scanf("%d%d",&a,&b);
	mod = a%b; p=a; q=b;
	while(mod>0)
	{
		a=b;
		b=mod;
		mod=a%b;
	}
	printf("%d\n%d",b,p*q/b);
	return 0;
}
```

```c
#include <stdio.h>

int main()
{
	int A, B, a, b;
	scanf("%d %d", &A, &B);
	a = A, b = B;
	int mod = a % b;
	while (mod > 0) {
		a = b;
		b = mod;
		mod = a % b;
	}
	printf("%d\n%d", b, (A*B / b));
}
```