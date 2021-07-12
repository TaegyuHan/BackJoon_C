# 11866 요세푸스 문제 0

URL : [https://www.acmicpc.net/problem/11866](https://www.acmicpc.net/problem/11866)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void) 
{
    int i;
    int cnt=0,
        gap=0;
    int N, K; // 1 ≤ K ≤ N ≤ 1,000
    int arr[1001];

    scanf("%d %d", &N, &K);
    
    for(i=0; i<N; i++)
        arr[i] = i+1;

    printf("<");
    i=0;
    while(1)
    {
        if(i==N) i=0; // 배열 처음으로 이동
        if(arr[i]==0) // 이미 삭제한 배열 넘기기
        {
            i++;
            continue;
        }

        gap++; // K번째 찾기
        if(gap>=K)
        {
            cnt++;
            if(cnt==N)
            {   // 마지막 번째
                printf("%d", arr[i]);
                arr[i] = 0;
                break;
            }
            else
            {   // 처음 ~ 중간 출력
                printf("%d, ", arr[i]);
                arr[i] = 0;
            }
            gap=0; // 출력하면 초기화
        }
        i++;
    }
    printf(">");

    return 0;
}
```

숏 코딩

```c
a[1001];i,j,t;
main(N,M)
{
	for(scanf("%d%d",&N,&M),putchar(60);i++<N;)
	{
		 for(j=0;j++<M;)
				t=++t>N?:t,a[t]&&j--;a[t]=1;
			printf("%d%s",t,i<N?", ":">");
	}
}
```

```c
#include <stdio.h>
//10845

static int q[1001] = {0, };

int main(void) {
    int n, m, N, i, count, top = 0;

	scanf("%d %d", &n, &m);
	for(i = 0; i < n; i++)
		q[i] = i + 1;
	
	printf("<");
	N = n;
	while(n > 0){
		count = m;
		while(count != 0){
			if(q[top%N] == 0)
				top++;
			else{
				count--;
				if(count == 0){
					printf("%d", q[top%N]);
						q[top%N]=0;
				}
				top++;
			}
		}
		if(n > 1)
			printf(", ");
		n--;
	}
	printf(">\n");

    return 0;    
}
```

```c
#include <stdio.h>

int queue[1000001];
int start = 0, end = 0;

void enque(int n);
int deque();

int main()
{
    int N, K;

    scanf("%d %d", &N, &K);

    for (int i = 1; i <= N; i++)
        enque(i);
   
    printf("<");
    while (start != end) {
        for (int i = 0; i < K - 1; i++)
            enque(deque());
        if (end - start == 1)
            printf("%d>", deque());
        else
            printf("%d, ", deque());
    }
    return 0;
}

void enque(int n)
{
    queue[end] = n;
    end++;
}

int deque()
{
    return queue[start++];
}
```