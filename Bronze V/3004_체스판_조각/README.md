# 3004 체스판 조각

URL : [https://www.acmicpc.net/problem/3004](https://www.acmicpc.net/problem/3004)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct sangGeun
{
    int cutCount;
} SangGeun;

void inputData(SangGeun * SG)
{
    scanf("%d", &SG->cutCount);
}

int solve(SangGeun * SG)
{
    int pice;
    int width;
    int height;

    // 짝수 줄
    if(SG->cutCount%2==0)
    {   
        width = SG->cutCount/2;
        height = SG->cutCount/2;
        pice = (width + 1) * (height + 1);
    }
    else // 홀수 줄
    {
        width = (SG->cutCount/2)+1;
        height = SG->cutCount/2;
        pice = (width + 1) * (height + 1);
    }

    return pice;
}

int main(void)
{
    int result;
    SangGeun SG;

    inputData(&SG);
    result = solve(&SG);
    printf("%d", result);

    return 0;
}
```

숏코딩

```c
#include <stdio.h>

int main()
{
    int n, max = 1, temp, i;
    
    scanf("%d", &n);
    
	for(i=1;i<n;i++)
    {
    	temp = (i + 1) * (n - i + 1);
    	if(max < temp)
    	{
    		max = temp;
		}
	}
	
	printf("%d\n", max);
    
    return 0;
}
```

```c
#include <stdio.h>

int f(int count)
{
	int i = count / 2 + 1;

	if (count == 0) return 1;
	if (count == 1) return 1;

	return f(count - 1) + i;
}

int main(void)
{
	int count;

	scanf("%d", &count);
	
	printf("%d", f(count) + 1);
	
	return 0;
}
```

```c
#include <stdio.h>

int main()
{
	int N;
	scanf("%d", &N);
	if (N % 2 == 0)
	{
		printf("%d", ((N / 2) + 1) *((N/2)+1));
	}
	else
	{
		printf("%d", ((N / 2) + 1) * ((N / 2) + 2));
	}
}
```