# 20254 Site Score

URL : [https://www.acmicpc.net/problem/20254](https://www.acmicpc.net/problem/20254)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    int A, B, C, D;
    scanf("%d %d %d %d", &A, &B, &C, &D);
    printf("%d", A*56 + B*24 + C*14 + D*6);

    return 0;
}
```