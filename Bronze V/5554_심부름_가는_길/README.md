# 5554 심부름 가는 길

URL : [https://www.acmicpc.net/problem/5554](https://www.acmicpc.net/problem/5554)

```c
#include <stdio.h>

int main(void)
{
    int i;
    int InputSecond;
    int SumSecond=0;

    for(i=0; i<4; i++)
    {
        scanf("%d", &InputSecond);
        SumSecond += InputSecond;
    }

    printf("%d\n", SumSecond/60);
    printf("%d\n", SumSecond%60);

    return 0;
}
```