# 11050 이항 계수 1

URL : [https://www.acmicpc.net/problem/11050](https://www.acmicpc.net/problem/11050)

```c
#include <stdio.h>

int main() {

    char N, K, temp;
    int result=1;
    scanf("%d %d", &N, &K);
    
    temp = N;
    
    for(;N>(temp-K);N--)
        result *= N;

    for(;K>0;K--)
        result /= K;

    printf("%d", result);

    return 0;
}
```

숏코딩

```c
#include<stdio.h>
int main(){
	int N, K,n;
	int ans=1;
	scanf("%d", &N);
	scanf("%d", &K);
	for(n=N-K+1;n<=N;n++){
		ans*=n;
	}
	for(n=1;n<=K;n++){
		ans/=n;
	}
	printf("%d", ans);
}
```

```c
#include <stdio.h>

int N, K;
int output = 1;

int main(void)
{
	int i;
	scanf("%d %d", &N, &K);
	for (i = N; i > (N-K); i--) output *= i;
	for (i = 1; i <= K; i++) output /= i;
	printf("%d\n", output);
}
```

```c
#include<stdio.h>

int fac(int n){
	int i;
	int ret=1;
	for(i=1; i<=n; i++){
		ret*=i;
	}
	return ret;
}

int main(){
	int n,k,result;
	scanf("%d %d", &n, &k);
	result=fac(n)/(fac(k)*fac(n-k));
	printf("%d", result);
}
```