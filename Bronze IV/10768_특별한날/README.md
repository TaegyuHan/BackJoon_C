# 10768 특별한날

URL : [https://www.acmicpc.net/problem/10768](https://www.acmicpc.net/problem/10768)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct specialDay
{   
    int month;  // 1 <= month <= 12
    int day;    // 1 <= day <= 31
} SpecialDay;

int main(void)
{
    SpecialDay SD;

    scanf("%d %d", &SD.month, &SD.day);

    if( SD.month==2 && SD.day==18 )
        printf("Special");
    else if( (SD.month<2) ||
             (SD.month==2 && SD.day<18) )
        printf("Before");
    else
        printf("After");

    return 0;
}
```