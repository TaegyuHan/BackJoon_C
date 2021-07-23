# 2444 별 찍기 - 7

URL : [https://www.acmicpc.net/problem/2444](https://www.acmicpc.net/problem/2444)

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
    int len = S.number*2;
    int i;
    int starNum = 1,
        spaceNum = S.number-1;

    for(i=1; i<len; i++)
    {
        space(spaceNum);
        star(starNum);
        if(i>=S.number)
        {
            starNum-=2;
            spaceNum++;
        }
        else 
        {
            starNum+=2;
            spaceNum--;
        }

        if(i!=len-1) printf("\n");
    }
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
#include <stdio.h>

int main()
{
	int nInput = 0;

	scanf("%d", &nInput);

	// 입력받은 줄까지 삼각형 출력
	for (int nLine=0; nLine<nInput; nLine++)
	{
		int nSpaceCount = nInput - nLine - 1;
		for (int nSpaceLine=0; nSpaceLine<nSpaceCount; nSpaceLine++)
		{
			printf(" ");
		}

		// 1 3 5 7 9
		int nStarCount = 2 * nLine + 1;
		for (int nStarLine=0; nStarLine<nStarCount; nStarLine++)
		{
			printf("*");
		}
		printf("\n");
	}

	// 입력받은 줄 이후 삼각형 출력
	for (int nLine=0; nLine<nInput-1; nLine++)
	{
		int nSpaceCount = nLine + 1;
		for (int nSpaceLine=0; nSpaceLine<nSpaceCount; nSpaceLine++)
		{
			printf(" ");
		}

		// 4 line
		// 7(0) 5(1) 3(2) 1(3)
		// 1 3 5 7
		int nStarCount = 2 * (nInput - 1) - (2 * nLine + 1);
		for (int nStarLine=0; nStarLine<nStarCount; nStarLine++)
		{
			printf("*");
		}
		printf("\n");
	}

	return 0;
}
```