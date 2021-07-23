# 2747 피보나치 수

URL : [https://www.acmicpc.net/problem/2747](https://www.acmicpc.net/problem/2747)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct fibonacci
{
    int number; // 1 <= number <= 45
} Fibonacci;

void inputData(Fibonacci * F)
{
    scanf("%d", &F->number);
}

void showNumber(Fibonacci F)
{
    int len = F.number;
    int i;
    int result, temp;
    int num1=0, num2=1;

    if(len==0) { printf("0"); return; }
    else if(len==1) { printf("1"); return; }
    else if(len==2) { printf("1"); return; }

    for(i=0; i<len; i++)
    {
        result = num1 + num2;
        temp = num1;
        num1 = result;
        num2 = temp;
    }

    printf("%d", result);

    return;
}

int main(void)
{
    Fibonacci F;
    inputData(&F);
    showNumber(F);

    return 0;
}
```

숏 코딩

```c
// ConsoleApplication1.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//
#include "stdio.h"

// 1. 피보나치 수열
int fibonacci_TopDown(int n);
int fibonacci_BottomUp(int n);

int main() {
	int n = 0;
	int result = 0;

	scanf("%d", &n);

	result = fibonacci_TopDown(n);
	//result = fibonacci_BottomUp(n);

	printf("%d\n", result);

	return 0;
}

// Top-down
int memo[100] = { 0 };
int fibonacci_TopDown(int n) {
	// fibonacci(0) = 0, fibonacci(1) = 1
	if (n <= 1) {
		return n;
	}
	else {
		if (memo[n] > 0) {
			// 메모가 있으면 리턴
			return memo[n];
		}
		memo[n] = fibonacci_TopDown(n - 1) + fibonacci_TopDown(n - 2);
		return memo[n];
	}
}

// Bottom-up
int d[100];
int fibonacci_BottomUp(int n) {
	d[0] = 0;
	d[1] = 1;
	for (int i = 2; i <= n; i++) {
		d[i] = d[i - 1] + d[i - 2];
	}
	return d[n];
}
```

```c
#include<stdio.h>
#include<stdlib.h>

#define MAX_NUM  90

int main(void)
{
	int* arr;
	int a0, a1, a2;
	int i;
	int n;

	scanf("%d", &n);

	if (n<1 || n>MAX_NUM)
	{
		printf("유효하지 않은 항을 입력하셨습니다. 프로그램은 강제종료됩니다.");
			return -1;
	}

	arr = (int*)calloc(n+1, sizeof(int));

	for (i = 0; i <= n; i++)
	{
		if (i == 0)
		{
			a0 = i;
			arr[i] = a0;
		}

		else if (i == 1)
		{
			a1 = i;
			arr[i] = a1;
		}

		else
		{
			a2 = a0 + a1;
			a0 = a1;//피보나치수열의 핵심은, 처음0번째항 1번째항은 값이 0,1로 각각 정해져있고, 그 이후부터는
			a1 = a2;//바로 이전항값과 그이전이전항값을 더함으로써 그 다음항이 구해진다는 점이다. -> 즉 앞으로의 그 다음항을 계속 구하기 위해선,
			        // "그 이전항과 , 그 이전이전항 값의 정보를 계속 업데이트해줘야 한다!!"
			arr[i] = a2;
		}
	}

	printf("%d\n", arr[n]);

	return 0;

}
```