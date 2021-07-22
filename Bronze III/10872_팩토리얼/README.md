# 10872 팩토리얼

URL : [https://www.acmicpc.net/problem/10872](https://www.acmicpc.net/problem/10872)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct factorial
{
    int number;
} Factorial;

void inputData(Factorial * F)
{   
    scanf("%d", &F->number);
    return;
}

int factorial(Factorial F)
{
    int i;
    int result = 1;
    for(i=1; i<=F.number; i++)
    {
        result *= i;
    }
    return result;
}

int main(void)
{
    Factorial F;
    inputData(&F);
    printf("%d", factorial(F));

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>
int main(void)
{
    int n;
    scanf("%d",&n);
    switch(n){
        case 0 : printf("1\n"); break;
        case 1 : printf("1\n"); break;
        case 2 : printf("2\n"); break;
        case 3 : printf("6\n"); break;
        case 4 : printf("24\n"); break;
        case 5 : printf("120\n"); break;
        case 6 : printf("720\n"); break;
        case 7 : printf("5040\n"); break;
        case 8 : printf("40320\n"); break;
        case 9 : printf("362880\n"); break;
        case 10 : printf("3628800\n"); break;
        case 11 : printf("39916800\n"); break;
        case 12 : printf("479001600\n"); break;
    }
    return 0;
}
```

```c
#include <stdio.h>

int factorial(int n){
    //초항 a_0  = 1
    if(n == 0) return 1;
    //점화식 a(n) = n * a(n-1)
    else return n * factorial(n - 1);
}

int main(void){
    //첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다
    int N;
    scanf("%d", &N);
    
    //첫째 줄에 N!을 출력한다
    printf("%d\n", factorial(N));
    
    return 0;
}
```

```c
#include <stdio.h>
int fact2(int n);
int main() {
	int N;
	int i;
	int total=1;
	while (1) {
		scanf("%d", &N);
		if (N >= 0 && N <= 12)break;
	}
	printf("%d",total = fact2(N));

	return 0;
}
int fact2(int n) {
	int res, i;

	if (n == 1 || n == 0)
		return 1;
	else {
		res = n;
		for (i = n - 1; i > 0; i--)
			res *= i;
		return res;
	}
}
```