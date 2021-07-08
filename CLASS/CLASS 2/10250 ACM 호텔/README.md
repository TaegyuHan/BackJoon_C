# 10250 ACM 호텔

URL : [https://www.acmicpc.net/problem/10250](https://www.acmicpc.net/problem/10250)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    int cnt;
    char W, H, N;
    scanf("%d", &cnt);

    while(cnt--)
    {
        scanf("%d %d %d", &H, &W, &N);
        if(N%H==0)
            printf("%d\n", ((H*100) + ((N/H))));
        else 
            printf("%d\n", ((N%H*100) + ((N/H)+1)));
    }

    return 0;
}
```

런타임 에러 (DivisionByZero)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    int cnt;
    int W, H, N;
    scanf("%d", &cnt);

    while(cnt--)
    {
        scanf("%d %d %d", &H, &W, &N);
        int floor=1, number=1;
        for(int i=1; i<N; i++)
        {
            if(floor==H)
            {
                floor=1;
                number++;
                continue;
            }
            floor++;
        }
        printf("%d \n", floor*100 + number);
    }
    return 0;
}
```

성공

숏코딩

```c
main(h,n){for(gets(&h);~scanf("%d%*d%d",&h,&n);)printf("%d ",--n%h*100+101+n/h);}
```

```c
int T,H,W,N;
 
int main()
{
    for (scanf("%d",&T);T--;){
        scanf("%d%d%d",&H,&W,&N);
        printf("%d%02d\n",(N-1)%H+1,(N-1)/H+1);
    }
}
```

```c
main(){
    int t,h,w,n;
    scanf("%d",&t);
    while(t--){
        scanf("%d %d %d",&h,&w,&n);
        printf("%d\n",((n%h==0?h:n%h)*100)+((n/h)+(n%h==0?0:1)));
    }
}
```

```c
#include <stdio.h>
int main(){
    int c,h,w,n;
    for(scanf("%d",&c);c>0;c--){
        scanf("%d%d%d",&h,&w,&n);
        printf("%d\n",((n-1)%h)*100+(n-1)/h+101);
    }
}
```

```c
#include<stdio.h>

int main(void) {
	int t,h,w,n;
	int floor;
	int unit;
	
	scanf("%d",&t);
	
	for(;t>0;t--) {
		scanf("%d %d %d",&h,&w,&n);
		printf("%d%02d\n", (n%h == 0) ? h : n%h , (n%h==0) ? n/h : n/h+1 );
	}
}
```