# 10992 별 찍기 -17

URL : [https://www.acmicpc.net/problem/10992](https://www.acmicpc.net/problem/10992)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct star
{
    int number;
} Star;

void inputData(Star * S)
{
    scanf("%d", &S->number);
}

void star(int n)
{
    for(int i=0; i<n; i++)
        printf("*");
}

void space(int n)
{
    for(int i=0; i<n; i++)
        printf(" ");
}

void ShowStar(Star S)
{
    int len = S.number;
    int i, j;
    int spaceNum=S.number-1,
        inSpaceNum=1,
        startNum=1;

    for(i=1; i<len; i++)
    {
        space(spaceNum);
        star(1);
        if(i>1)
        {
            space(inSpaceNum);
            inSpaceNum+=2;
            star(1);
        }
        startNum+=2;
        spaceNum--;
        printf("\n");
    }
    star(startNum);
}

int main(void)
{
    Star S;
    inputData(&S);
    ShowStar(S);

    return 0;
}
```

숏 코딩

```c
int inputNumber(int from, int to);
void print3Line(int n);

int main(void) {
	int n;

	n = inputNumber(1, 100);
	print3Line(n);

	return 0;
}

void print3Line(int n) {
	char start = '*';
	char end   = '*';
	char interval = '*';
	char blank = ' ';
	int  startIndex, endIndex;
	
	int j;
	for(int i = 0; i < n; i++) {
		startIndex = (n - 1) - i;
		endIndex   = (n - 1) + i;
		//printf("startIndex: %d endIndex: %d\n", startIndex, endIndex);
		for(j = 0; j < endIndex + 1; j++) {
			if(j == startIndex) {
				printf("%c", start);
			}else if(j == endIndex) {
				printf("%c", end);
			}else if (i == n - 1) {
				printf("%c", interval);
 			} else {
				printf("%c", blank);	
			}
		}
		printf("\n");

	}	
}

int inputNumber(int from, int to) {
	int n;
	do {
		scanf("%d", &n);
	} while (!(n >= from && n <= to));
	return n;
}
```

```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
	int N = 0;
	fscanf(stdin, "%d", &N);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N + i; j++)
		{
			int padding = abs(N - 1 - i);
			//printf("\ni:%d, j:%d, padding:%d -> ", i, j, padding);

			if (i == (N - 1))
			{
				printf("*");
			}
			else if (j >= padding)
			{
				//printf("%d\n", (j - padding) % 2);
				if (j == padding)
					printf("*");
				else if (j == (N + i - 1))
					printf("*");
				else
					printf(" ");
			}
			else
			{
				printf(" ");
			}
		}
		puts("");
	}

	return 0;
}
```