# 2490 윷놀이

URL : [https://www.acmicpc.net/problem/2490](https://www.acmicpc.net/problem/2490)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct stick
{
    int fourStick[4];
} Stick;

void inputData(Stick * Stick)
{
    int i;
    for(i=0; i<4; i++)
        scanf("%d", &Stick->fourStick[i]);
}

void checkState(Stick Stick)
{
    int i;
    int sum=4;
    for(i=0; i<4; i++)
        sum -= Stick.fourStick[i];

    switch(sum)
    {
        case 0:
            printf("E\n");
            break;
        case 1:
            printf("A\n");
            break;
        case 2:
            printf("B\n");
            break;
        case 3:
            printf("C\n");
            break;
        case 4:
            printf("D\n");
            break;
    }
}

int main(void)
{
    int i;
    Stick Stick;

    for(i=0; i<3; i++)
    {
        inputData(&Stick);
        checkState(Stick);
    }

    return 0;
}
```