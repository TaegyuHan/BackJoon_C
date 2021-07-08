# 4153 직각삼각형

URL : [https://www.acmicpc.net/problem/4153](https://www.acmicpc.net/problem/4153)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

void ShowResult(int a, int b, int c)
{
    if( a*a == (b*b) + (c*c))
        printf("right\n");
    else
        printf("wrong\n");
}

int main(void)
{
    int a, b, c;

    do
    {
        scanf("%d %d %d", &a, &b, &c);

        if(a>b && a>c)
            ShowResult(a, b, c);
        else if(b>a && b>c)
            ShowResult(b, a, c);
        else if(c>a && c>b)
            ShowResult(c, b, a);
    }
    while(a!=0 && b!=0 && c!=0);

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>

int main(void) {
	int x, y, z;

	while(scanf("%d %d %d", &x, &y, &z), x)
	{
		if(x > z) {int t = x; x = z; z = t;}
		if(y > z) {int t = y; y = z; z = t;}
		printf(z*z == x*x + y*y ? "right\n" : "wrong\n");
	}

	return 0;
}
```

```c
#include <stdio.h>

int main(void)
{
	int a,b,c;
	
	for(;;)
	{
		scanf("%d %d %d",&a,&b,&c);
		if(a==0&&b==0&&c==0)
		{
			break;
		}
		else if (a*a==b*b+c*c||b*b==a*a+c*c||c*c==a*a+b*b)
		{
			printf("right\n");
		}
		else
		{
			printf("wrong\n");
		}
	}
	
	return 0;
}
```

```c
int main()
{
    int a, b, c;
    
    while(1)
    {
        scanf("%d%d%d", &a, &b, &c);
        
        if(a==0) break;
        if(a*a+b*b==c*c || a*a==b*b+c*c || b*b==a*a+c*c)
            puts("right");
        else
            puts("wrong");
    }
}
```