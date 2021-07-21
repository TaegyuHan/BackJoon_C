# 5596 시험점수

URL : [https://www.acmicpc.net/problem/5596](https://www.acmicpc.net/problem/5596)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct test
{   
    int information;
    int math;
    int science;
    int english;
    int pointSum;
} Test;

int main(void)
{
    int i;
    int resultPoint;
    Test Test[2];

    // 점수 받기
    for (i=0; i<2; i++)
    {
        scanf("%d %d %d %d",
            &Test[i].information,
            &Test[i].math,
            &Test[i].science,
            &Test[i].english );

        // 점수 총합
        Test[i].pointSum = Test[i].information + 
                           Test[i].math + 
                           Test[i].science + 
                           Test[i].english;
    }
    
    // 큰수 구하기
    resultPoint = (Test[0].pointSum > Test[1].pointSum) ?
                        Test[0].pointSum : Test[1].pointSum;

    printf("%d", resultPoint);

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>

int main(){
int a,b,c,d;
int z,x,v,n;
int S, T;
scanf("%d %d %d %d",&a,&b,&c,&d);
scanf("%d %d %d %d",&z,&x,&v,&n);
S = a + b + c + d;
T = z+x+v+n;
if(S >= T){
  printf("%d", S);}
  else if(S < T){
    printf("%d", T);
  }
}
```

```c
#include <stdio.h>

int main()
{
	int n[8], sum[2] = { 0 };
	int i;

	for (i = 0; i < 4; i++) {
		scanf(" %d", &n[i]);
		sum[0] += n[i];
	}

	for (i = 4; i < 8; i++) {
		scanf(" %d", &n[i]);
		sum[1] += n[i];
	}

	if (sum[0] >= sum[1])
		printf("%d\n", sum[0]);
	else
		printf("%d\n", sum[1]);

	return 0;
}
```

```c
int main()                            //메인지정
{
	int a, b, c, d;
	int s1, s2;

	scanf("%d %d %d %d", &a, &b, &c, &d);
	s1 = a + b + c + d;
	scanf("%d %d %d %d", &a, &b, &c, &d);
	s2 = a + b + c + d;

	if (s1 == s2) {
		printf("%d", s1);
	}
	else if (s1 < s2) {
		
		printf("%d", s2);
	}
	else {
		printf("%d", s1);
	}
}
```

```c
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
    int s = 0;
    int t = 0;
    int item;
    for (int i = 0 ; i < 4; i ++) {
        scanf("%d", &item);
        s += item;
    }
    
    for (int i = 0 ; i < 4; i ++) {
        scanf("%d", &item);
        t += item;
    }
    s > t? printf("%d", s) : printf("%d", t);
}
```

```c
#include <stdio.h>

int score1[5];
int score2[5];

int main()
{
	int i;
	for(i=0;i<4;i++)
	{
		scanf(" %d", &score1[i]);
	}
	for(i=0;i<4;i++)
	{
		scanf(" %d", &score2[i]);
	}
	
	int sum1=0, sum2=0;
	for(i=0;i<4;i++)
	{
		sum1 = sum1 + score1[i];
		sum2 = sum2 + score2[i];	
	}
	
	if(sum1>sum2)
	{
		printf("%d", sum1);
	}
	else if(sum1==sum2)
	{
		printf("%d", sum1);
	}
	else
	{
		printf("%d", sum2);
	}
	
	return 0;
}
```