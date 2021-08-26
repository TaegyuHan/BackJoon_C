# 2579 계단 오르기

URL : [https://www.acmicpc.net/problem/2579](https://www.acmicpc.net/problem/2579)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX(A,B) (A)>(B)?(A):(B)
#define ARY_LEN 301

typedef struct _Data
{
	char backOneStep;
	int len;
	unsigned short ary[ARY_LEN];
	int maxSum[ARY_LEN];
} Data;

void inputIntData(int* num) { scanf("%d", num); return; }
void inputUnShortData(unsigned short* num) { scanf("%d", num); return; }

int stairsMax(Data* D)
{
	//초기값 지정해주기
	D->maxSum[0] = 0;
	D->maxSum[1] = D->ary[1];
	D->maxSum[2] = D->ary[1] + D->ary[2];

	//최대 값 구하기
	for (int i = 3; i <= D->len; i++) {
		D->maxSum[i] = D->ary[i] + (MAX(D->maxSum[i - 2], D->ary[i - 1] + D->maxSum[i - 3]));
	}

	return D->maxSum[D->len];
}

int main(void)
{
	// 변수 생성
	Data* D = (Data*)malloc(sizeof(Data));
	memset(D, 0, sizeof(Data));

	// 입력
	inputIntData(&(D->len));

	// 데이터 입력
	int i;
	for (i = 1; i <= D->len; i++)
		inputUnShortData(&(D->ary[i]));

	printf("%d", stairsMax(D));

	return 0;
}
```

숏 코딩

```c
#include <stdio.h>
#define MAX(a,b) a>b?a:b

int dp[301];
int stair[301];

int main() {
    int N;
    scanf("%d", &N);

    for (int i = 1; i <= N; i++) {
        scanf("%d", &stair[i]);
    }

    //초기값 지정해주기
    dp[0] = 0;
    dp[1] = stair[1];
    dp[2] = stair[1] + stair[2];

    //최대 값 구하기
    for (int i = 3; i <= N; i++) {

        printf("MAX ( %d, %d )\n", dp[i - 2], stair[i - 1] + dp[i - 3]);

        dp[i] = stair[i] + (MAX(dp[i - 2], stair[i - 1] + dp[i - 3]));
        printf("dp[%d] : %d\n", i, dp[i]);
    }

    //결과 출력
    printf("%d\n", dp[N]);
    return 0;
}
```