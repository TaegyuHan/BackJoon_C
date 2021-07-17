# 1550 16진수

URL : [https://www.acmicpc.net/problem/1550](https://www.acmicpc.net/problem/1550)

```c
#include <stdio.h>

int hex(char hexNumber)
{
    int result;

    if(hexNumber >= 65 && hexNumber <= 70)
        result = hexNumber-55;
    else if(hexNumber >= 48 && hexNumber <= 57)
        result = hexNumber-48;

    return result;
}

int main(void)
{

    char i;
    int NumberSquares=1;
    int ArrayLength=0;
    int result=0;
    char HexList[20];
    scanf("%s", HexList);

    for(i=0; HexList[i]!='\0'; i++)
    {
        ArrayLength++;
    }

    for(i=(ArrayLength-1); i>=0; i--)
    {
        result += hex(HexList[i])*NumberSquares;
        NumberSquares *= 16;
    }

    printf("%d", result);

    return 0;
}
```