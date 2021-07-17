# 17256 달달함이 넘쳐흘러

URL : [https://www.acmicpc.net/problem/17256](https://www.acmicpc.net/problem/17256)

```c
#include <stdio.h>

int main(void)
{
    int Ax, Ay, Az;
    int Cx, Cy, Cz;
    
    scanf("%d %d %d", &Ax, &Ay, &Az);
    scanf("%d %d %d", &Cx, &Cy, &Cz);
    printf("%d %d %d", Cx-Az, Cy/Ay, Cz-Ax);

    return 0;
}
```