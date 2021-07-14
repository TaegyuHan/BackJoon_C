# 10845 큐

URL : [https://www.acmicpc.net/problem/10845](https://www.acmicpc.net/problem/10845)

```c
#include <stdio.h>
int QueueArray[10001];

// 문자열 비교 함수
int strcmp(char str1[], const char str2[])
{
    int i;
    for(i=0; str2[i]!=NULL; i++)
    {
        if(str2[i]!=str1[i])
            return 0; // 같지 않으면 0
    }
    return 1; // 같으면 1
}

void push(int Array[], int * head, int * tail, int InputNubmer)
{
    int TempHead = * head;
    int TempTail = * tail;

    // 현재 tail 위치에 숫자 추가
    Array[TempTail] = InputNubmer;

    // 현재 tail 위치 변경
    * tail = TempTail + 1;

    return;
}

void pop(int Array[], int * head, int * tail)
{
    int TempHead = * head;
    int TempTail = * tail;

    if(TempHead == TempTail)
    {
        printf("-1\n");
    }
    else
    {   
        // 현재 head 위치 0으로 변경
        printf("%d\n", Array[TempHead]);
        Array[TempHead] = 0;

        // 현재 head 위치 한칸 앞으로
        * head = TempHead + 1;
    }

    return;
}

void size(int Array[], int * head, int * tail)
{
    int TempHead = * head;
    int TempTail = * tail;

    if((TempHead - TempTail) == 0)
        printf("0\n");
    else if ((TempHead - TempTail) > 0)
        printf("%d\n", (TempHead - TempTail));
    else 
        printf("%d\n", (TempTail - TempHead));

    return;
}

void empty(int Array[], int * head, int * tail)
{
    int TempHead = * head;
    int TempTail = * tail;

    if(TempHead == TempTail)
    {
        printf("1\n");
    }
    else
    {   
        printf("0\n");
    }

    return;
}

void front(int Array[], int * head, int * tail)
{
    int TempHead = * head;
    int TempTail = * tail;
    
    if(TempHead == TempTail)
    {
        printf("-1\n");
    }
    else
    {   
        printf("%d\n", Array[TempHead]);
    }

    return;
}

void back(int Array[], int * head, int * tail)
{
    int TempHead = * head;
    int TempTail = * tail;
    
    if(TempHead == TempTail)
    {
        printf("-1\n");
    }
    else
    {   
        printf("%d\n", Array[TempTail-1]);
    }

    return;
}

int main(void)
{
    int CommandNum; // (1 ≤ CommandNum ≤ 10,000)
    int InputNubmer; // (1 ≤ InputNubmer ≤ 100,000) 
    char InputCommandType[6];
    int head=0, // 배열 처음 부분
        tail=0; // 배열 마지막 부분

    // 커맨드 입력 횟수
    scanf("%d", &CommandNum);

    while(CommandNum--)
    {
        scanf("%s", InputCommandType);

        if(strcmp(InputCommandType, "push"))
        {
            scanf("%d", &InputNubmer);
            push(QueueArray, &head, &tail, InputNubmer);
        }
        else if(strcmp(InputCommandType, "pop"))
        {
            pop(QueueArray, &head, &tail);
        }
        else if(strcmp(InputCommandType, "size"))
        {
            size(QueueArray, &head, &tail);
        }
        else if(strcmp(InputCommandType, "empty"))
        {
            empty(QueueArray, &head, &tail);
        }
        else if(strcmp(InputCommandType, "front"))
        {
            front(QueueArray, &head, &tail);
        }
        else if(strcmp(InputCommandType, "back"))
        {
            back(QueueArray, &head, &tail);
        }

    }

    return 0;
}
```

 숏 코딩

```c
#include <stdio.h>
int main() 
{
	char input[10];
	int que[10001] = { 0 };
	int data=0;
	int st = 0, ed = 0;
	int n;

	scanf("%d", &n);
	

	while (n--)
	{
		scanf("%s", input);

		switch (input[0])
		{
		case 'p':
			if (input[1] == 'u')
			{
				scanf("%d", &data);
				que[st++] = data;
			}
			else if (input[1] == 'o')
			{
				if (st == ed)
					printf("-1\n");
				else
					printf("%d\n", que[ed++]);
			}
			break;
		case 's':
			printf("%d\n", st - ed);
			break;
		case 'e':
			if (st == ed)
				printf("1\n");
			else
				printf("0\n");
			break;
		case 'f':
			if (st == ed)
				printf("-1\n");
			else
				printf("%d\n", que[ed]);

			break;
		case 'b':
			if (st == ed)
				printf("-1\n");
			else
				printf("%d\n", que[st-1]);
			break;
		}
	}
	return 0;
}
```

```c
#include <stdio.h>
int first, rear, arr[10001], i,n,pnum;
char str[13];
int main()
{
	first = 1; rear = 1;
	scanf("%d", &n);
	for (i = 0; i < n; i++)
	{
		scanf("%s", str);
		if (strncmp(str, "pu", 2) == 0)
		{
			scanf("%d", &pnum);
			arr[rear++] = pnum;
		}
		else if (strncmp(str, "po", 2) == 0)
		{
			if (first == rear)
				printf("-1\n");
			else
				printf("%d\n", arr[first++]);
		}
		else if (strncmp(str, "s", 1) == 0)
			printf("%d\n", rear - first);
		else if (strncmp(str, "e", 1) == 0)
		{
			if (rear == first)
				printf("1\n");
			else
				printf("0\n");
		}
		else if (strncmp(str, "f", 1) == 0)
		{
			if (rear == first)
				printf("-1\n");
			else
				printf("%d\n", arr[first]);
		}
		else if (strncmp(str, "b", 1) == 0)
		{
			if (rear == first)
				printf("-1\n");
			else
				printf("%d\n", arr[rear-1]);
		}
	}
	return 0;
}
```