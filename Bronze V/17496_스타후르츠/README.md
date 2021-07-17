# 17496 스타후르츠

URL : [https://www.acmicpc.net/problem/17496](https://www.acmicpc.net/problem/17496)

```c
#include <stdio.h>

int main(void)
{
    int i;
    int N, //  (2 ≤ N ≤ 90)
        T, //  (1 ≤ T ≤ N-1)
        C, //  (1 ≤ C ≤ 300)
        P; //  (1 ≤ P ≤ 1,000)

    int EarnedMoney=0;

    scanf("%d %d %d %d", &N, &T, &C, &P);

    for(i=1; i*T<N; i++)
    {
        EarnedMoney += C*P;
    }

    printf("%d", EarnedMoney);

    return 0;
}
```