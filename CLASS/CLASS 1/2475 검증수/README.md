# 2475 검증수

URL : [https://www.acmicpc.net/problem/2475](https://www.acmicpc.net/problem/2475)

```c
#include <stdio.h>

int main(void)
{
    char i, len;
    char NumList[9];
    int sum=0;

    len = sizeof(NumList) / sizeof(char);
    scanf("%[^\n]s", NumList);

    for(i=0; i<len; i++)
    {
        if(NumList[i]==' ')
            continue;
        else
        {
            sum += (NumList[i]-48)*(NumList[i]-48);
        }
    }

    printf("%d", sum%10);

    return 0;
}
```

숏코딩

```c
a;main(n){for(;~scanf("%d",&n);)a+=n*n;printf("%d",a%10);}
```

```c
#include <stdio.h>
int main(){
	int a,b,c,d,e;
	scanf("%d %d %d %d %d",&a,&b,&c,&d,&e);
	printf("%d",(a*a+b*b+c*c+d*d+e*e)%10);
}

#include <stdio.h>
int main(){
	int a,b,c,d,e;
	int r;
	scanf("%d%d%d%d%d",&a,&b,&c,&d,&e);
	r=(a*a+b*b+c*c+d*d+e*e)%10;
	printf("%d",r);
}
```

```c
int main(){
    int a[5],i,b=0;
    for(i=0;i<5;i++){
        scanf("%d ",a+i);
        b+= a[i]*a[i];
    }
    printf("%d",b%10);
}

#include<stdio.h>
unsigned int temp, i,s=0;
int main() {
	for (i = 0; i < 5; i++) {
		scanf("%u",&temp);s += temp*temp;
	}printf("%u", s % 10);
}
```

```c
#include <stdio.h>

int main()
{
	int n, sum=0, T=5;
	
	while(T--)
	{
		scanf("%d", &n);
		
		sum += n*n;
	}
	
	printf("%d\n", sum%10);
}
```