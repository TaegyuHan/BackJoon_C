# 2164 카드2

URL : [https://www.acmicpc.net/problem/2164](https://www.acmicpc.net/problem/2164)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>
int CardArray[500001]={0,};

void InputToArray(int CardArray[], int CardNumber)
{   
    // 배열에 숫자 넣는 함수
    int i;
    for(i=0; i<CardNumber; i++)
    {
        CardArray[i] = i+1;
    }
}

void ShowArray(int CardArray[], int CardNumber)
{
    // 배열의 내용 보여주는 함수
    int i;
    for(i=0; i<CardNumber; i++)
    {
        printf("%d ", CardArray[i]);
    }
    printf("\n");
}

void DropCard(int CardArray[], int * CardNumber)
{
    int i;
    int TempCardNumber = *CardNumber;

    for(i=0; i<=TempCardNumber; i++)
    {
        CardArray[i] = CardArray[i+1];
    }
    *CardNumber = --TempCardNumber;
}

void BackCard(int CardArray[], int CardNumber)
{
    int i;
    CardArray[CardNumber] = CardArray[0];
    for(i=0; i<CardNumber; i++)
    {
        CardArray[i] = CardArray[i+1];
    }
}

int main(void)
{
    int i;
    int CardNumber;
    char CardStatus = 0; // 0 버림, 1 맨뒤

    scanf("%d", &CardNumber);

    InputToArray(CardArray, CardNumber);

    while(CardNumber!=1)
    {
        if(CardStatus==0)
        {
            DropCard(CardArray, &CardNumber);
            ShowArray(CardArray, CardNumber);
            CardStatus = 1;
        }
        else if(CardStatus==1)
        {
            BackCard(CardArray, CardNumber);
            ShowArray(CardArray, CardNumber);
            CardStatus = 0;
        }
    }

    printf("%d", CardArray[0]);

    return 0;
}
```

큐로 구현

```c
#include <stdio.h>
int CardArray[500000]={0,};

void InputToArray(int CardArray[], int CardNumber)
{   
    // 배열에 숫자 넣는 함수
    int i;
    for(i=0; i<CardNumber; i++)
    {
        CardArray[i] = i+1;
    }
}

void ShowArray(int CardArray[], int ArraySize)
{
    // 배열의 내용 보여주는 함수
    int i;
    for(i=0; i<ArraySize; i++)
    {
        printf("%d ", CardArray[i]);
    }
    printf("\n");
}

void DropCard(int CardArray[],int ArraySize, int * head, int * tail)
{
    int i;
    int TempHead = *head;
    int TempTail = *tail;

    CardArray[TempHead] = 0;

    // head 옮기기
    if(TempHead+1 > ArraySize)
        *head = (TempHead+1)%(ArraySize+1);
    else 
        *head = TempHead+1;
}

void BackCard(int CardArray[], int ArraySize, int * head, int * tail)
{
    int i;
    int TempHead = *head;
    int TempTail = *tail;

    // tail 옮기기
    if(TempTail+1 > ArraySize)
        *tail = (TempTail+1)%(ArraySize+1);
    else 
        *tail = TempTail+1;

    // 머리에서 나온부분 꼬리로 옮기기
     CardArray[*tail] = CardArray[TempHead];
     CardArray[TempHead] = 0; // 나간부분 지우기

    // head 옮기기
    if(TempHead+1 > ArraySize)
        *head = (TempHead+1)%(ArraySize+1);
    else 
        *head = TempHead+1;
}

int main(void)
{
    int i;
    int head, tail;
    int CardNumber, ArraySize;
    char CardStatus = 0; // 0 버림, 1 맨뒤

    scanf("%d", &CardNumber);
    head = 0;
    tail = CardNumber-1;
    ArraySize = CardNumber-1;

    // 배열에 넣기
    InputToArray(CardArray, CardNumber);

    while(head!=tail)
    {
        if(CardStatus==0)
        {
            DropCard(CardArray, ArraySize, &head, &tail);
            CardStatus = 1;
        }
        else if (CardStatus==1)
        {
            BackCard(CardArray, ArraySize, &head, &tail);
            CardStatus = 0;
        }
    }

    printf("%d", CardArray[head]);

    return 0;
}
```

숏 코딩

```c
#include<stdio.h>

main()
{
	int n,m=0;
	int i,j=0;
	int arr[1000000]={0};
	int arr2[1000000]={0};

	scanf("%d", &n);
	m=n+1;

	for(i=1; i<=n; i++)
	{
		arr[i] = i;
	}
	
	for(i=1; i<=n*2; i++)
	{
		if(i%2 == 1)
		{
			arr2[i] = arr[i];
		}
		else
		{
			arr[m++]=arr[i];
		}
	}

	printf("%d", arr2[n*2-1]);
}
```

```c
#include <stdio.h>

int maxsize=1000000;
int queue[1000000];
int front=0, back=0;

void push(int x)
{
    queue[back]=x;
    back += 1;
    if (back>=maxsize)
        back %= maxsize;
}

int pop()
{
    if (front==back)
        return -1;
    else
    {
        front += 1;
        front %= maxsize;
        if (front==0)
            return queue[maxsize-1];
        else
            return queue[front-1];
    }
}
int main()
{
    int n;
    scanf("%d", &n);
    for (int i=1;i<=n;i++)
        push(i);
    while ((back-front)%maxsize!=1)
    {
        pop();
        push(pop());
    }
    printf("%d", queue[front]);
    return 0;
}
```