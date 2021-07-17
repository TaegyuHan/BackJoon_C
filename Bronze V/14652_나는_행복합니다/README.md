# 14652 나는 행복합니다~

URL : [https://www.acmicpc.net/problem/14652](https://www.acmicpc.net/problem/14652)

```c
#include <stdio.h>

int main(void)
{
    int i;
    // (1 <= N, M <= 30,000, 0 <= K <= N*M-1)
    int N,
        M,
        Seat;

    scanf("%d %d %d", &N, &M, &Seat);

    printf("%d %d", Seat/M, Seat%M);

    return 0;
}
```