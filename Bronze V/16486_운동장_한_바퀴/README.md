# 16486 운동장 한 바퀴

URL : [https://www.acmicpc.net/problem/16486](https://www.acmicpc.net/problem/16486)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct ground
{
    int width;
    int radius;
} Ground;

void inputData(Ground * G)
{
    scanf("%d %d", 
            &G->width,
            &G->radius );
    return;
}

double OneLap(Ground * G)
{
    double pie = 3.141592;
    return (double)(G->width*2) + (G->radius*2*pie) ;
}

int main(void)
{
    Ground G;

    inputData(&G);
    printf("%.6lf", OneLap(&G));

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>
int main() {
	float d1;
	float d2;
	scanf("%f %f", &d1, &d2);
	float sum = (d1 * 2) + (d2 * 2 * 3.141592);
	printf("%f", sum);

	return 0;
}
```