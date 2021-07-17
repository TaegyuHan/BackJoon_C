# 3003 킹, 퀸, 룩, 비숍, 나이트, 폰

URL : [https://www.acmicpc.net/problem/3003](https://www.acmicpc.net/problem/3003)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    char King, Queen, Look, Bishop, Knight, Pawn;

    scanf("%d %d %d %d %d %d", &King, &Queen, &Look, &Bishop, &Knight, &Pawn);
    printf("%d %d %d %d %d %d",
            1 - King,
            1 - Queen,
            2 - Look,
            2 - Bishop,
            2 - Knight,
            8 - Pawn);

    return 0;
}
```