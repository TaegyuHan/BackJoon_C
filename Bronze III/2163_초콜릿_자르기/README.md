# 2163 초콜릿 자르기

URL : [https://www.acmicpc.net/problem/2163](https://www.acmicpc.net/problem/2163)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct chocolate
{
    int N; // (1≤ N ≤300)
    int M; // (1≤ M ≤300)
} Chocolate;

void inputData(Chocolate * Chocolate)
{
    scanf("%d %d", 
            &Chocolate->N,
            &Chocolate->M );
}

void cutCount(Chocolate Chocolate)
{
    int result = (Chocolate.N)*(Chocolate.M - 1) +
                 (Chocolate.N - 1);

    printf("%d", result); 
}

int main(void)
{
    Chocolate Chocolate;
    inputData(&Chocolate);
    cutCount(Chocolate);

    return 0;
}
```

 숏 코딩

```c
int main(int argc, char *argv[]) {
	int n,m;
	scanf("%d %d",&n,&m);
	printf("%d",n*m-1);
	return 0;
}
```

```c
int main()
{
	int M = 0, N = 0;
	scanf("%d %d", &M, &N);

	if (M == N)
	{
		printf("%d\n", (M - 1)*(M + 1));
	}
	else
	{
		printf("%d\n", (M*N) - 1);
	}
	return 0;
}
```

```c
int main(void)
{
	int N, M;
	int cnt;

	scanf("%d%d", &N, &M);
	if((N-1)+N*(M-1) >= (M-1)+M*(N-1))
		printf("%d\n", (M-1)+M*(N-1));
	else
		printf("%d\n", (N-1)+N*(M-1));

	return 0;
}
```