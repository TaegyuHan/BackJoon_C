# 1929 소수 구하기

URL : [https://www.acmicpc.net/problem/1929](https://www.acmicpc.net/problem/1929)

```c
#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0

typedef struct _Number
{   //  (1 ≤ M ≤ N ≤ 1,000,000)
    int M;
    int N;
} Number;

void InputIntData(int* num)
{
    scanf("%d", num);
}

void CheckPrimeNumber(Number Number)
{
    int i, j;
    int* Array = (int*)malloc(sizeof(int) * (Number.N + 1));

    // 전부 소수 인정 데이터 입력
    for (i = 0; i <= Number.N; i++)
    {
        Array[i] = TRUE;
    }

    // 0과 1 소수 아님
    Array[0] = Array[1] = FALSE;
    for (i = 2; i * i <= Number.N; i++)
    {
        // 소수 아니면 PASS
        if (!Array[i]) continue;

        int mult = 2;
        for (j = i * mult; j <= Number.N; j = i * ++mult)
        {   // 소수 판별
            Array[j] = FALSE;
        }
            
    }

    // 출력
    for (i = Number.M; i <= Number.N; i++)
    {
        if (Array[i] != FALSE) printf("%d\n", i);
    }
}

int main()
{
    int count = 0;
    Number Number;

    InputIntData(&Number.M);
    InputIntData(&Number.N);

    CheckPrimeNumber(Number);

    return 0;
}
```

 

숏 코딩

```c
#include<stdio.h>
//1929번 소수구하기
//에라토스테네스의 체방식으로 구하기.

//힙 - 동적으로 할당받는 변수가 올라감
//스택 - 지역변수가 올라감
//데이터 - 전역변수가 올라감
int number = 1000000;
int a[1000001];//지역변수로 선언시,100(1MB)만이 넘으면 오버플로우 발생한다.
int main()
{
	int M, N;//1 ≤ M ≤ N ≤ 1,000,000
	scanf("%d %d", &M, &N);
	for (int i = 2; i <= number; i++)
	{
		a[i] = i;
	}
	for (int i = 2; i <= number; i++)
	{
		if (a[i] == 0)
			continue;
		for (int j = 2; j * i <= number; j++)
		{
			if (i * j <= number)
				a[i * j] = 0;
			else
				break;
		}
	}
	for (int i = M; i <= N; i++)
	{
		if(a[i]!=0)
			printf("%d\n", a[i]);
	}
	return 0;
}
```

```c
#include <stdio.h>

int ft_sqrt(int nb)
{
  int root = 100;
  while (1)
  {
    if (root * root <= nb && (root + 1) * (root + 1) > nb)
      break ;
    else
      root = (nb / root + root) / 2;
  }
  return (root);
}

void is_prime(int nb)
{
  int sqrt_nb;
  int i;

  if (nb < 2)
    return ;
  else if (nb == 2)
    printf("2\n");
  else
  {
    i = 2;
    sqrt_nb = ft_sqrt(nb);
    while (i <= sqrt_nb)
    {
      if (nb % i == 0)
        return ;
      i++;
    }
    printf("%d\n", nb);
  }
  return ;
}

int main(void)
{
  int start, end;
  int i;

  scanf("%d %d", &start, &end);
  i = start - 1;
  while (++i <= end)
    is_prime(i);
  return (0);
}
```

```c
#include <stdio.h>
#include <math.h>

#define MAX 1000000

int main(void)
{
    int prime[MAX], found=1, i, j, tmp = 0, m, n;
    
    prime[0] = 2;
    
    for(i=3; i<MAX; i++)
    {
        for(j=0; j<found; j++)
        {
            if(prime[j] > sqrt(i)) break;
            if(i % prime[j] == 0)
            {
                tmp = 1;
                break;
            }
        }
            
        if(!tmp) prime[found++] = i;
        tmp = 0;
    }
    
    scanf("%d %d", &m, &n);
    
    for(i=0; i<found; i++)
    {
        if(prime[i] > n) break;
        else if(prime[i] >= m) printf("%d\n", prime[i]);
    }
    
    return 0;
}
```