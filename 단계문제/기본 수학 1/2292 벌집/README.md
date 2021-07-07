# 2292 벌집

URL : [https://www.acmicpc.net/problem/2292](https://www.acmicpc.net/problem/2292)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    unsigned int i=0;
    unsigned int CheckNum, sum=1;
    scanf("%d", &CheckNum);

    do
    {   // 6개씩 벌집이 늘어남
        sum += 6*i;
        i++;
    }
    while(sum < CheckNum);

    printf("%d", i);

    return 0;
}
```

<br>

숏 코딩

```c
#include<stdio.h>
int main()
{
	int a, i;
	scanf("%d", &a);
	for(i=0; a>(3*i*i+3*i+1);i++);
	printf("%d", i+1);
}
```

```c
#include <stdio.h>
int main(void) {
  int x, i=0, c =0;
  scanf("%d", &x);
  while(x>c*6+1){i++;c+=i;}
  printf("%d", i+1);
  return 0;
}
```