# 9461 판도반 수열

URL : [https://www.acmicpc.net/problem/9461](https://www.acmicpc.net/problem/9461)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N_DATA_LEN 101
#define ONE_END 2
#define TWO_END 4

typedef struct _Data
{
	unsigned long long int array[N_DATA_LEN];
} Data;

void inputIntData(int* num) { scanf("%d", num); return; }

void initArray(Data* D)
{
	int i;

	// 1입력
	for (i = 0; i <=ONE_END; i++)
		D->array[i] = 1;

	// 2입력
	for (i = ONE_END + 1; i <= TWO_END; i++)
		D->array[i] = 2;

	// 나머지 입력
	for (i = TWO_END + 1; i < N_DATA_LEN; i++)
		D->array[i] = D->array[i - 5] + D->array[i - 1];

	return;
}

int main(void)
{
	Data* D = (Data*)malloc(sizeof(Data));
	memset(D, 0, sizeof(Data));

	// 배열 데이터 input
	initArray(D);
	
	// TEST 횟수 데이터 input
	int TEST_CNT;
	inputIntData(&TEST_CNT);
	
	// 결과 출력
	int i;
	int indexTmp;
	for (i = 0; i < TEST_CNT; i++)
	{
		inputIntData(&indexTmp);
		printf("%lld\n", D->array[indexTmp - 1]);
	}

	return 0;
}
```

숏 코딩

```c
#include<stdio.h>
long long dp[100+10];
int T[100+10];

long long f(int x)
{
    if(x==1) return 1;
    if(x==2) return 1;
    if(x==3) return 1;
    if(x==4) return 2;

    if(dp[x]>0)
		{
        return dp[x];
    }

    if(x>4)
		{
        dp[x]= f(x-2)+f(x-3);
        return dp[x];
    }
}

int main()
{
    int n; scanf("%d", &n);
    int i;
    for(i=0; i<n; i++){
    scanf("%d", &T[i]);
    }

    for(i=0; i<n; i++){
    long long ans = f(T[i]);
    printf("%lld\n", ans);
    }

    return 0;
}
```

```c
#include <stdio.h>
#define MAX 110
int T, N;
long long P[MAX];

long long solve(int n) {
	int i;
	if (n <= 3) return 1;
	if (n >= 4 && n <= 5) return 2;
	
	for (i=1; i<4; i++) P[i] = 1;
	for (i=4; i<6; i++) P[i] = 2;
	for (i=6; i<=n; i++) P[i] = P[i-1] + P[i-5];

	return P[n];
}
int main(void) {
	long long ans;
	scanf("%d", &T);
	for (int i=0; i<T; i++) {
		scanf("%d", &N);
		ans = solve(N);
		printf("%ld\n", ans);
	}
	return 0;
}
```