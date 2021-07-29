# 10870 피보나치 수 5

URL : [https://www.acmicpc.net/problem/10870](https://www.acmicpc.net/problem/10870)

```c
#include <stdio.h>

typedef struct _number
{
	int N; // 1 <= N <= 20
} Number;

void InputData(Number* N)
{
	scanf("%d", &N->N);
}

int Fibo(int n)
{
    if (n == 1)
        return 0;
    else if (n == 2)
        return 1;
    else
        return Fibo(n - 1) + Fibo(n - 2);
}

int main(void)
{
	Number N;
    InputData(&N);
    printf("%d", Fibo(N.N+1));

	return 0;
}
```