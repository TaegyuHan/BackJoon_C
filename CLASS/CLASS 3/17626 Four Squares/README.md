# 17626 Four Squares

URL : [https://www.acmicpc.net/problem/17626](https://www.acmicpc.net/problem/17626)

```c
#include <stdio.h>

void InputIntData(int* num) { scanf("%d", num); }

int HighestSquares(int NUM)
{
	int i = 1;
	while (i * i <= NUM)
		i++;

	return --i;
}

int main(void)
{	
	int i = 0, j = 0, k = 0;
	int NUM;
	int result=4;

	InputIntData(&NUM);

	for (i = HighestSquares(NUM); i > 0; i--)
	{
		j = 0, k = 0;
		if (NUM == (i * i) + (j * j) + (k * k) || result == 1)
		{
			result = 1;
			break;
		}

		for (j = HighestSquares(NUM - (i * i)); j > 0; j--)
		{
			k = 0;
			if (NUM == (i * i) + (j * j) + (k * k) || result == 2)
			{
				result = 2;
				break;
			};

			for (k = HighestSquares(NUM - (i * i) - (j * j)); k > 0; k--)
			{
				if (NUM == (i * i) + (j * j) + (k * k) || result == 3)
				{
					result = 3;
					break;
				};
			}
		}
	}

	printf("%d", result);

	return 0;
}
```

숏 코딩

```c
#include <stdio.h>
 
int main(void)
{
    
    int N;
    int Dp[100001] = {};
    scanf("%d", &N);
    
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j*j <= i; j++){
            if (Dp[i] > Dp[i - j*j] + 1 || Dp[i] == 0)
                Dp[i] = Dp[i - j*j] + 1;
        }
    }
    
    printf("%d\n", Dp[N]);
 
    return 0;
}
```

```c
#include <stdio.h>
#define N 50005

int n, dt[N];

int min(int a, int b){
	return (a<b) ? a : b;
}

int main()
{
	
	int i;
	scanf("%d", &n);
	
	dt[1]=1;
	for(i=2; i<=n; i++){
		dt[i]=9999999;
		for(int j=1; ; j++){
			if(j*j>i) break;
			dt[i]=min(dt[i], dt[i-(j*j)]+1);
		}
	}
	printf("%d", dt[n]);
	
	return 0;
}
```

```c
#include<stdio.h>
#include<math.h>
int N, a[50001];
void check(int n) {
	int sq = (int)sqrt((double)n);
	int tmp;
	for (int i = 1; i <= sq; i++) {
		tmp = 1 + a[n - i * i];
		if (!a[n]) a[n] = tmp;
		else a[n] = tmp < a[n] ? tmp : a[n];
	}
}
int main() {
	scanf("%d", &N);
	a[1] = 1;
	for (int i = 2; i <= N; i++) {
		check(i);
	}

	printf("%d", a[N]);
	return 0;
}
```