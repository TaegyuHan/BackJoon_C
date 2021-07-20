# 2525 오븐 시계

URL : [https://www.acmicpc.net/problem/2525](https://www.acmicpc.net/problem/2525)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

struct Cook
{
    int hour;
    int minute;
};

int main(void)
{

    int tempTime;
    int resultHour,
        resultMinute;
    struct Cook Cook;

    scanf("%d %d", &Cook.hour, &Cook.minute);
    scanf("%d", &tempTime);

    // 분 설정
    resultMinute = (tempTime + Cook.minute)%60;
    resultHour = (Cook.hour + (tempTime + Cook.minute)/60)%24;

    printf("%d %d", resultHour, resultMinute);

	return 0;
}
```