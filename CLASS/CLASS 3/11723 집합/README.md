# 11723 집합

URL : [https://www.acmicpc.net/problem/11723](https://www.acmicpc.net/problem/11723)

```c
#include <stdio.h>
#include <string.h>

#define DATA_LEN 21
#define CMD_STRING_LEN 7

typedef struct _Set
{
	char set[DATA_LEN];
	int DataSize;
} Set;

void InputIntData(int* num) { scanf("%d", num); }
void InputStrData(char* str) { scanf("%s", str); }

void add(Set* S, int index) { S->set[index] = 1; return; }
void remove2(Set* S, int index) { S->set[index] = 0; return; }
void check(Set* S, int index) { printf("%d\n", S->set[index]); return; }

void toggle(Set* S, int index) 
{ 
	if (S->set[index])
		S->set[index] = 0;
	else
		S->set[index] = 1;

	return; 
}

void all(Set* S) 
{
	int i;
	for (i = 0; i < DATA_LEN; i++)
		S->set[i] = 1;

	return;
}

void empty(Set* S)
{
	int i;
	for (i = 0; i < DATA_LEN; i++)
		S->set[i] = 0;

	return;
}

void ExecuteCommand(Set* S, char* tmpCMD, int tmpNumber)
{

	if (strcmp(tmpCMD, "add") == 0)
	{
		add(S, tmpNumber);
	}
	else if (strcmp(tmpCMD, "remove") == 0)
	{
		remove2(S, tmpNumber);
	}
	else if (strcmp(tmpCMD, "check") == 0)
	{
		check(S, tmpNumber);
	}
	else if (strcmp(tmpCMD, "toggle") == 0)
	{
		toggle(S, tmpNumber);
	}
	else if (strcmp(tmpCMD, "all") == 0)
	{
		all(S);
	}
	else if (strcmp(tmpCMD, "empty") == 0)
	{
		empty(S);
	}

	return;
}

int main(void)
{
	Set Set = {0,};
	int i;
	int INPUT_CMD_COUNT;
	char tmpCMD[CMD_STRING_LEN];
	int tmpNumber;

	InputIntData(&INPUT_CMD_COUNT);

	for (i=0; i < INPUT_CMD_COUNT; i++)
	{
		InputStrData(tmpCMD); InputIntData(&tmpNumber);
		ExecuteCommand(&Set, tmpCMD, tmpNumber);
	}
	return 0;
}
```

숏 코딩

```c
#include <stdio.h>
#include <string.h>

int main()
{
	int cmd, M, S=0;	
	char str[7]={0};
	int num=0;

	scanf("%d", &M);

	for(cmd=0; cmd<M; cmd++)
	{		
		scanf("%s %d", str, &num);
		if(!strcmp(str,"add"))
			S = S|(1<<num);	
		else if(!strcmp(str,"remove"))
			S = S & ~(1<<num);
		else if(!strcmp(str,"check"))
			printf("%d\n", (S&(1<<num))?1:0);
		else if(!strcmp(str,"toggle"))
			S = S^(1<<num);
		else if(!strcmp(str,"all"))
			S = 2147483647;
		else if(!strcmp(str,"empty"))
			S = 0;
	}

	return 0;
}
```