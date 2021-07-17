# 5522 카드게임

URL : [https://www.acmicpc.net/problem/5522](https://www.acmicpc.net/problem/5522)

```c
#include <stdio.h>

int main(void)
{
    char i;
    int InputNumber, sum=0;

    for(i=0; i<5; i++)
    {
        scanf("%d", &InputNumber);
        sum += InputNumber;
    }
    
    printf("%d", sum);

    return 0;
}
```