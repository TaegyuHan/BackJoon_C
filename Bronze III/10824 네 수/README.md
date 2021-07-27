# 10824 네 수

URL : [https://www.acmicpc.net/problem/10824](https://www.acmicpc.net/problem/10824)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>
#include <string.h>

#define CHAR_TO_NUMBER(X) ((X)-(48))
#define NUMBER_TO_CHAR(X) ((X)+(48))

typedef struct number
{   // (1 ≤ A, B, C, D ≤ 1,000,000)
    char AB[20];
    char B[8];
    char CD[20];
    char D[8];
} Number;

void strAdd(char str1[], char str2[])
{
    int i;
    char result[17];
    int str1Len = strlen(str1)-1;
    int str2Len = strlen(str2)-1;
    int loop = (str1Len >= str2Len) ? str1Len : str2Len;

    int nextTemp = 0,
        addTemp = 0,
        currTemp = 0;

    // printf("str1 : %s\n", str1);
    // printf("str1Len : %d\n", str1Len);

    // printf("str2 : %s\n", str2);
    // printf("str2Len : %d\n", str2Len);

    for(i=loop+1; i>=0; i--)
    {
        // printf("str1Len : %d ", str1Len); printf("str1[str1Len] : %c ", str1[str1Len]);
        // printf("str2Len : %d ", str2Len); printf("str2[str2Len] : %c ", str2[str2Len]);

        addTemp = nextTemp + 
                  CHAR_TO_NUMBER(str1[str1Len]) +
                  CHAR_TO_NUMBER(str2[str2Len]);
        nextTemp = addTemp/10;
        currTemp = addTemp%10;
        // printf("addTemp : %d ", addTemp);
        // printf("nextTemp : %d ", nextTemp);
        // printf("currTemp : %d ", currTemp);
        result[i] = NUMBER_TO_CHAR(currTemp);
        
        if(str1Len > 0)
            str1Len--;
        else
        {
            str1Len = 0;
            str1[str1Len] = '0';
        }
        
        if(str2Len > 0)
            str2Len--;
        else
        {
            str2Len = 0;
            str2[str2Len] = '0';
        }
        // printf("\n");
    }

    for(i=0; i<=loop+1; i++)
    {
        if(i==0 && result[i]=='0')
            continue;
        else
            printf("%c", result[i]);
    }

    return;
}

void Calculation(Number Number)
{
    // 두 문자열 합치기
    strcat(Number.AB, Number.B);
    strcat(Number.CD, Number.D);

    strAdd(Number.AB, Number.CD);

    return;
}

void InputData(Number * Number)
{
    scanf("%s %s %s %s",
            Number->AB,
            Number->B,
            Number->CD,
            Number->D );
}

int main(void)
{
    Number Number;

    InputData(&Number);
    Calculation(Number);

    return 0;
}
```

숏코딩

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
#include <stdlib.h>
char A[20];
char B[20];
char C[20];
char D[20];
char plus[30];

int main()
{
	scanf(" %s %s %s %s", A, B, C, D);
	int lenA = strlen(A);
	int lenB = strlen(B);
	int lenC = strlen(C);
	int lenD = strlen(D);
	int j = 0;
	for (int i = lenA; i < lenA + lenB; i++)
	{
		A[i] = B[j];
		j++;
	}
	j = 0;
	for (int i = lenC; i < lenC + lenD; i++)
	{
		C[i] = D[j];
		j++;
	}
	long long int result1 = atoll(A);
	long long int result2 = atoll(C);
	printf("%ld", result1 + result2);
}
```

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
	unsigned long long int ia[4];
	int count[2] = {0, 0};
	int buf[2];
	int i = 0;
	scanf("%lld %lld %lld %lld", &ia[0], &ia[1], &ia[2], &ia[3]);

	buf[0] = ia[1];
	while (buf[0] != 0)
	{
		buf[0] = buf[0] / 10;
		++count[0];
	}
	for (i = 0; i < count[0]; i++)
	{
		ia[0] *=  10;
	}

	buf[1] = ia[3];
	while (buf[1] != 0)
	{
		buf[1] = buf[1] / 10;
		++count[1];
	}
	for (i = 0; i < count[1]; i++)
	{
		ia[2] *= 10;
	}

	printf("%lld", ia[0] + ia[1] + ia[2] + ia[3]);
}
```