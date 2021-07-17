# 18301 Rats

URL : [https://www.acmicpc.net/problem/18301](https://www.acmicpc.net/problem/18301)

```c
#include <stdio.h>

int main(void)
{
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);
    printf("%d", (A+1)*(B+1)/(C+1)-1);
    
    return 0;
}
```