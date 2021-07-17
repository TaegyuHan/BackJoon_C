# 15727 조별과제를 하려는데 조장이 사라졌다

URL : [https://www.acmicpc.net/problem/15727](https://www.acmicpc.net/problem/15727)

```c
#include <stdio.h>

int main(void)
{
    int i;
    int Distance;
    int Answer=0;

    scanf("%d", &Distance);

    for(i=0; i<Distance; i+=5)
    {
        Answer++;
    }

    printf("%d", Answer);

    return 0;
}
```