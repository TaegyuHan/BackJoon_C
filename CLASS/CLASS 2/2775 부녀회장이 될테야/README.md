# 2775 부녀회장이 될테야

URL : [https://www.acmicpc.net/problem/2775](https://www.acmicpc.net/problem/2775)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void) 
{

    int n, i, j, k;
    int cnt, sum;
    int K, N; // 1 ≤ k, n ≤ 14
    int apartment[15][15];

    scanf("%d", &cnt);

    for(n=0; n<cnt; n++)
    {
        scanf("%d", &K); // 층
        scanf("%d", &N); // 호

        for(i=0; i<=K; i++)
        {
            // 첫번째 층
            if(i==0)
            {
                for(j=0; j<N; j++)
                    apartment[i][j] = j+1;
            }
            else // 다른 층
            {
                for(j=0; j<N; j++)
                {
                    sum = 0;
                    for(k=0; k<=j; k++)
                        sum += apartment[i-1][k];
                    apartment[i][j] = sum;
                }   
            }
        }

        printf("%d\n", apartment[K][N-1]);

    }

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>

int f(int k, int n)
{
	int x,i;
	if (k == 0)
		return n;
	else
	{
		x = 0;
		for (i = 0; i <= n; i++)
			x += f(k - 1, i);
		return x;
	}
}

int main()
{
	int a,n,k;
	scanf("%d", &a);
	while (a--)
	{
		scanf("%d %d", &k, &n);
		printf("%d\n", f(k, n));
	}

	return 0;
}
```

```c
#include <stdio.h>

int t, n, k, d[15][15];

int main() {
	for (int i = 1; i < 15; i++) d[0][i] = i;
	for (int i = 1; i < 15; i++) for (int j = 1; j < 15; j++)
		d[i][j] = d[i-1][j] + d[i][j-1];

	scanf("%d", &t);
	while (t--) {
		scanf("%d %d", &k, &n);
		printf("%d\n", d[k][n]);
	}

	return 0;
}
```

```c
#include <stdio.h>

int main()
{
	int i,j,k,t,n,T;
	int a[14];
	scanf("%d", &T);
	for (i = 0; i < T; i++) {
		scanf("%d %d", &k, &n);
		for (j = 0; j < n; j++) {
			a[j] = j + 1;
		}
		for (j = 1; j <= k; j++) {
			for (t = 1; t <= n; t++) {
					a[t] +=  a[t - 1];
			}
		}
		printf("%d\n", a[n-1]);
	}
}
```

```c
#include <stdio.h>

int many (int k, int n);

int main () {
	int k, n, t, i;
	scanf("%d", &t);
	for (i=0;i<t;i++) {
		scanf("%d\n%d", &k, &n);
		printf("%d\n", many(k,n));
	}
	return 0;
}

int many (int k, int n) {
	if (n ==1 ) {
		return 1;
	} else if (k==0) {
		return n;
	} else {
		return (many(k-1,n) + many(k,n-1));
	}
}
```