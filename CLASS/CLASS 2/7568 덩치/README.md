# 7568 덩치

URL : [https://www.acmicpc.net/problem/7568](https://www.acmicpc.net/problem/7568)

```c
#include <stdio.h>

int main(void) 
{
    int i, j;
    int N;
    int cnt;
    int size[201][2];
    
    //2 ≤ N ≤ 50
    scanf("%d", &N);

    // 배열 받기
    for(i=0; i<N; i++) // 10 ≤ x, y ≤ 200
        scanf("%d %d", &size[i][0], &size[i][1]);

    for(i=0; i<N; i++)
    {
        cnt=1;
        for(j=0; j<N; j++)
        {
            if(size[j][0]>size[i][0] && size[j][1]>size[i][1])
                cnt++;
        }
        if(i==N)
        {
            printf("%d", cnt);
            break;
        }
        printf("%d ", cnt);
    }

    return 0;
}
```

숏 코딩

```c
j;i;a[52];b[52];main(n){for(gets(&n);~scanf("%d%d",i+a,++i+b););for(;a[++j];printf("%d ",n))for(n=i=1;a[i];i++)a[i]>a[j]&&b[i]>b[j]&&n++;}
```

```c
#include <stdio.h>
int x[205],y[205],c[205];
int main() {
	int n,i,j;
	scanf("%d", &n);
	for (i = 1; i <= n; i++)
		scanf("%d %d", &x[i], &y[i]);
	for (i = 1; i <= n; i++) {
		c[i]++;
		for (j = 1; j <= n; j++)
			if (x[i] < x[j] && y[i] < y[j] && j != i)
				c[i]++;
	}
	for (i = 1; i <= n;)
		printf("%d ", c[i++]);
}
```

```c
#include <stdio.h>

int main() {
	int N, k=0;

	int x[50] = { 0, };
	int y[50] = { 0, };

	scanf("%d", &N);

	for (int i = 0; i < N; i++)
		scanf("%d %d", &x[i], &y[i]);

	for (int i = 0; i < N; i++) {
		k = 0;
		for (int j = 0; j < N; j++) {
			if (x[i] < x[j] && y[i] < y[j])
				k++;
		}
		printf("%d ", k + 1);
	}
	return 0;
}
```

```c
#include <stdio.h>
int main() {
	int N,i,k; 
	int x[51] = {0, }, y[51] = {0, };
	int rank = 0;
	scanf("%d", &N);
	for (i = 0; i < N; i++)
		scanf("%d %d", &x[i], &y[i]);
	for (i = 0; x[i] != 0; i++) {
		rank = 0;
		k = 0;
		while (1) {
			if (x[k] > x[i] && y[k] > y[i])
				rank++;
			if (k==N) {
				printf("%d ", rank+1);
				break;
			}
			k++;
		}
	}
	return 0;
}
```

```c
#include <stdio.h>

struct Build {
	int h;
	int w;
};

int main() {
	int n;
	struct Build build[50];
	
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d %d", &build[i].h, &build[i].w);
	
	for (int i = 0; i < n; i++) {// me
		int myRank = 1;
		for (int j = 0; j < n; j++) { // target
			if (build[i].h < build[j].h && build[i].w < build[j].w)
				myRank++;
		}
		printf("%d ", myRank);
	}
	
}
```