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

시간초과

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define POKEMON_NAME_LEN 21
#define ALPHABET_COUNT 26
#define ALPHABET_TO_INDEX(X) ((X) - (65))

typedef struct _Data
{
	char name[POKEMON_NAME_LEN];
} Data;

typedef struct _Table
{
	struct _Table* nextNode;
	int index;
	char name[POKEMON_NAME_LEN];
} Table;

void InputIntData(int* num){ scanf("%d", num); }
void InputStrData(char* str){ scanf("%s", str); }

int IntNumberCheck(char* str)
{
	if (str[0] >= '0' && str[0] <= '9')
		return 1;
	else
		return 0;
}

void InsertDataToTable(Table* table, int i, int index, char str[])
{
	Table* tmp;
	if (table[index].nextNode == NULL)
	{
		strcpy(table[index].name, str);
		table[index].index = i;
		table[index].nextNode = (Table*)malloc(sizeof(Table));
		table[index].nextNode->nextNode = NULL;
		return;
	}
	else
	{
		tmp = table[index].nextNode;
		while (1)
		{
			if (tmp->nextNode == NULL)
			{
				strcpy(tmp->name, str);
				tmp->index = i;
				tmp->nextNode = (Table*)malloc(sizeof(Table));
				tmp->nextNode->nextNode = NULL;
				return;
			}
			tmp = tmp->nextNode;
		}
	}
	return;
}

void checkStrTable(Table* table, char str[])
{
	int index = ALPHABET_TO_INDEX(str[0]);
	Table* tmp = table[index].nextNode;

	if (!strcmp(str, table[index].name))
	{
		printf("%d\n", table[index].index);
		return;
	}
	
	while (tmp != NULL)
	{
		if (tmp->nextNode == NULL)
			break;

		if (!strcmp(str, tmp->name))
		{
			printf("%d\n", tmp->index);
			return;
		}
		tmp = tmp->nextNode;
	}

	return;
}

int main(void)
{
	int i, j;
	int BOOK_LEN, TEST_LEN;
	int tmpIndex;
	char tmpStr[POKEMON_NAME_LEN];

	InputIntData(&BOOK_LEN); InputIntData(&TEST_LEN);

	// 사전 저장 리스트 생성
	Data* data = (Data*)malloc(sizeof(Data) * (BOOK_LEN + 2));
	Table* table = (Table*)malloc(sizeof(Table) * (ALPHABET_COUNT + 1));

	for (i = 0; i < ALPHABET_COUNT; i++)
		table[i].nextNode = NULL;

	for (i = 1; i <= BOOK_LEN; i++)
	{
		InputStrData(data[i].name);
		tmpIndex = ALPHABET_TO_INDEX(data[i].name[0]);

		InsertDataToTable(table, i, tmpIndex, data[i].name);
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
			checkStrTable(table, tmpStr);
		}
	}

	return 0;
}
```