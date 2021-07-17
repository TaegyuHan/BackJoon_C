# 20492 세금

URL : [https://www.acmicpc.net/problem/20492](https://www.acmicpc.net/problem/20492)

```c
#include <stdio.h>

int main(void)
{
    int PrizeMoney;
    scanf("%d", &PrizeMoney);

    printf("%d %d",
            PrizeMoney-(PrizeMoney/100*22),
            PrizeMoney-((PrizeMoney/100*20)/100*22));

    return 0;
}
```