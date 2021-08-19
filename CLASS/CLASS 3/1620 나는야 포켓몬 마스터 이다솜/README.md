# 1620 나는야 포켓몬 마스터 이다솜

URL : [https://www.acmicpc.net/problem/1620](https://www.acmicpc.net/problem/1620)

시간초과 수정 필요

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define POKEMON_NAME_LEN 21

typedef struct _Data
{
	int index;
	char name[POKEMON_NAME_LEN];
} Data;

void InputIntData(int* num){ scanf("%d", num); }
void InputStrData(char* str){ scanf("%s", str); }

int IntNumberCheck(char* str)
{
	if (str[0] >= '0' && str[0] <= '9')
		return 1;
	else
		return 0;
}

int main(void)
{
	int i, j;
	int BOOK_LEN, TEST_LEN;
	char tmpStr[POKEMON_NAME_LEN];

	InputIntData(&BOOK_LEN); InputIntData(&TEST_LEN);

	// 사전 저장 리스트 생성
	Data* data = (Data*)malloc(sizeof(Data) * (BOOK_LEN + 2));

	for (i = 1; i <= BOOK_LEN; i++)
	{
		InputStrData(data[i].name);
		data[i].index = i;
	}

	for (i = 0; i < TEST_LEN; i++)
	{
		InputStrData(tmpStr);

		if (IntNumberCheck(tmpStr))
		{
			printf("%s\n", data[atoi(tmpStr)].name);
		}
		else
		{
			for (j = 1; j <= BOOK_LEN; j++)
			{
				if (!strcmp(tmpStr, data[j].name))
				{
					printf("%d\n", j);
				}
			}
		}
	}

	return 0;
}
```