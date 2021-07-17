# 6749 Next in line

URL : [https://www.acmicpc.net/problem/6749](https://www.acmicpc.net/problem/6749)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    int YoungestChildren,
        MiddleChildren;

    scanf("%d %d", &YoungestChildren, &MiddleChildren);
    printf("%d", MiddleChildren + (MiddleChildren-YoungestChildren));

    return 0;
}
```