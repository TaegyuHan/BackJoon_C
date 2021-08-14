# x 1966 프린터 큐

URL : [https://www.acmicpc.net/problem/1966](https://www.acmicpc.net/problem/1966)

원형 큐 풀이중

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TEST_LEN 101
#define IMPORT_NUMBER 10

typedef struct _Data
{
	int TestCount;
	char PageCount;
	char Number;
	int TestList[TEST_LEN];
	int FIdx;
	int BIdx;
} Data;

typedef struct _Table
{
	char Importance[IMPORT_NUMBER];
} Table;

void InputIntData(int* num) { scanf("%d", num); }
void InputCharData(char* num) { scanf("%d", num); }

void MovFIdx(Data* D)
{
	(D->FIdx)++;

	if (D->FIdx < TEST_LEN)
		return;
	else
		D->FIdx = D->FIdx % TEST_LEN;
}

void MovBIdx(Data* D)
{
	(D->BIdx)++;

	if (D->BIdx < TEST_LEN)
		return;
	else
		D->BIdx = D->BIdx % TEST_LEN;
}

void BackToFront(Data* D)
{
	MovFIdx(D);
	D->TestList[D->FIdx] = D->TestList[D->BIdx];
	MovBIdx(D);
}

int PageOut(Data* D)
{
	int result = D->TestList[D->BIdx];
	MovBIdx(D);
	return result;
}

int PageCheck(Data* D, int imp)
{
	if (D->TestList[D->BIdx] == imp)
		return 1;
	else
		return 0;
}

int main(void)
{
	int i, j;
	int ImportNum, OutCount;
	Data* D = (Data*)malloc(sizeof(Data));
	memset(D, 0, sizeof(Data));

	// Page 입력
	InputIntData(&(D->TestCount));

	for (i = 0; i < D->TestCount; i++)
	{
		Table* T = (Table*)malloc(sizeof(Table));
		memset(T, 0, sizeof(Table));

		InputCharData(&(D->PageCount));
		InputCharData(&(D->Number));

		for (j = 0; j < D->PageCount; j++)
		{
			InputIntData(&(D->TestList[j]));
			MovFIdx(D);

			(T->Importance[D->TestList[j]])++;
		}

		ImportNum = IMPORT_NUMBER - 1;
		OutCount = 0;

		// Page 출력
		while (D->PageCount)
		{
			while (T->Importance[ImportNum])
			{
				printf("PageCheck : %d \n", PageCheck(D, ImportNum));
				printf("T->Importance[ImportNum] : %d \n", T->Importance[ImportNum]);

				if (PageCheck(D, ImportNum))
				{
					PageOut(D); // 인쇄
					printf("PageOut : %d\n", PageOut(D));
					(D->PageCount)--; // 남은 인쇄 페이지 감소
					(T->Importance[ImportNum])--; // 중요도 인쇄 페이지 감소

					// 현재 중요도 단계의 남은 종이 없으면
					// 중요도 낮추기
					if (!(T->Importance[ImportNum]))
					{
						ImportNum--;
					}
				}
				else 
				{
					BackToFront(D); // 뒤로 보내기
				}
			}

			if (!(T->Importance[ImportNum]))
			{
				ImportNum--;
			}

		}
	}

	free(D);
	return 0;
}
```

시간 초과

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    int cnt;
    char tempNum, tempIndex, tempLoop;
    char printcheck;
    char printOut=0;
    char i, j;
    char fileList[2][102];
    int fileNum, position;
    
    // test 횟수
    scanf("%d", &cnt);

    while(cnt--)
    {
        // 파일 개수, 파일 위치
        scanf("%d %d",  &fileNum, &position);

        // 파일 중요도 및 순서
        for(i=0; i<fileNum; i++)
        {
            fileList[0][i] = i;
            scanf("%d", &fileList[1][i]);
        }

        while(printOut!=fileNum)
        {

            printcheck=1;  // 맨 앞의 파일을 뽑아야 하는것인지 확인
            tempNum = fileList[1][0];
            tempLoop = fileNum-printOut;
            if(tempLoop==0) break;

            // 뒤에 중요도 높은 파일 있으면
            // 현재 파일 뒤로 보내기
            for(i=1; i<tempLoop; i++)
            {
                if(fileList[1][i]>tempNum)
                {
                    fileList[0][tempLoop] = fileList[0][0];
                    fileList[1][tempLoop] = fileList[1][0];
                    for(j=1; j<=tempLoop; j++)
                    {
                        fileList[0][j-1] = fileList[0][j];
                        fileList[1][j-1] = fileList[1][j];
                    }
                    printcheck=0; // 뽑으면 안됌
                    break;
                }
            }

            if(printcheck==1)
            {
                printOut++;
                fileList[0][tempLoop] = fileList[0][0];
                fileList[1][tempLoop] = fileList[1][0];
                for(j=1; j<=tempLoop; j++)
                {
                    fileList[0][j-1] = fileList[0][j];
                    fileList[1][j-1] = fileList[1][j];
                }

                if(fileList[0][tempLoop]==position)
                {
                    printf("%d\n", printOut);
                    break;
                }
            }
        }
    }

    return 0;
}
```

우선순위 큐

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int fileList[2][103]={0,};

/* 배열 출력하는 함수  */
void ShowString(int fileNum)
{
    int i, j;

    for(j=1; fileList[0][j]!=NULL; j++)
    {
        printf("index:%d number:%d\n", fileList[0][j], fileList[1][j]);
    }
}

void InsertPriorityQueue(int Node)
{
    // 최상위 노드인 경우 return
    if (Node==1) return;

    int ParentNode = Node/2; // 부모 노드
    int temp1; // 들어온 순서
    int temp2; // 중요도

    // 부모 노드와 현재 노드 비교
    if(fileList[1][ParentNode] < fileList[1][Node])
    {
        // 서로 변경하기
        // // 순서
        temp1 = fileList[0][ParentNode];
        fileList[0][ParentNode] = fileList[0][Node];
        fileList[0][Node] = temp1;
        
        // 중요도
        temp2 = fileList[1][ParentNode];
        fileList[1][ParentNode] = fileList[1][Node];
        fileList[1][Node] = temp2;

        InsertPriorityQueue(ParentNode);
    }
    else if(fileList[1][ParentNode] == fileList[1][Node])
    {
        
    }
    else
        return;
}

void InputData(int position)
{
    // 데이터 데이터 index 받기
    fileList[0][position] = position; // 순서
    scanf("%d", &fileList[1][position]); // 중요도

    // 데이터 정렬
    InsertPriorityQueue(position);
}

int main(void)
{
    char i, j;
    int cnt;
    int fileNum, position;
    
    // test 횟수
    scanf("%d", &cnt);

    while(cnt--)
    {
        // 파일 개수, 파일 위치
        scanf("%d %d",  &fileNum, &position);

        // 데이터 받기
        for(i=1; i<=fileNum; i++)
        {
            InputData(i);
        }

        ShowString(fileNum);
        
    }

    return 0;
}
```

2021-08-06

```c
#include <stdio.h>

#define DATA_LEN 101
#define TABLE_INDEX_LEN 10

#define MAX_IMPORTANCE 9
#define MIN_IMPORTANCE 1

#define TRUE 1
#define FALSE 0

int TEST_COUNT; 

typedef struct _Data
{
    int data;
    int index;
} Data;

typedef struct _Print
{
    int printNum; // N(1 ≤ N ≤ 100) 
    int index; // M(0 ≤ M < N)
} Print;

typedef struct _Queue
{
    Data arry[DATA_LEN];
    int FrontIndex;
    int BackIndex;
} Queue;

typedef struct _Table
{
    int index[TABLE_INDEX_LEN];
} Table;

void QueueInit(Queue* Queue)
{
    Queue->FrontIndex = 0;
    Queue->BackIndex = 0;
};

int QueueCheckEmpty(Queue* Queue)
{
    if (Queue->FrontIndex == Queue->BackIndex)
        return TRUE;
    else
        return FALSE;
}

void QueueInsertData(Queue* Queue, int i)
{
    int data;

    scanf("%d", &data);

    if (QueueCheckEmpty(Queue))
    {
        Queue->FrontIndex = 0;
        Queue->BackIndex = 1;
        Queue->arry[Queue->FrontIndex].data = data;
        Queue->arry[Queue->FrontIndex].index = i;
    }
    else
    {
        Queue->arry[Queue->BackIndex].data = data;
        Queue->arry[Queue->FrontIndex].index = i;
        Queue->BackIndex = (++Queue->BackIndex) % 100;
    }
}

int TablePopMaxImportnace(Table* Table)
{
    int i;
    for (i = MAX_IMPORTANCE; i >= MIN_IMPORTANCE; i--)
    {
        if (Table->index[i] <= 0)
            continue;
        else
            return i;
    }
}

void QueueFrontToBackData(Queue* Queue)
{
    Queue->arry[Queue->BackIndex] = Queue->arry[Queue->FrontIndex];
    Queue->BackIndex = (++Queue->BackIndex) % 100;
    Queue->FrontIndex = (++Queue->FrontIndex) % 100;
}

int QueueFrontCheckData(Queue* Queue)
{
    if (QueueCheckEmpty(Queue))
        return -1;

    return Queue->arry[Queue->FrontIndex].data;
}

int QueueFrontPopData(Queue* Queue)
{
    if (QueueCheckEmpty(Queue))
        return -1;

    int result = Queue->arry[Queue->FrontIndex].data;
    Queue->FrontIndex = (++Queue->FrontIndex) % 100;
    return result;
}

void QueuePopData(Queue* Queue, Table* Table)
{
    int importNum = TablePopMaxImportnace(Table);

    while (importNum != QueueFrontCheckData(Queue))
        QueueFrontCheckData(Queue);

    printf("%d", QueueFrontPopData(Queue));

}

void TableInsertData(Table* Table, int num)
{
    (Table->index[num])++;
}

void InputIntData(int* n)
{
    scanf("%d", n);
}

int main()
{
    Print Print;
    Queue Queue;

    int i, j;

    // TEXT 횟수
    InputIntData(&TEST_COUNT);
    for (i = 0; i < TEST_COUNT; i++)
    {
        Table Table = { 0, };

        // 큐 데이터 입력
        QueueInit(&Queue);
        InputIntData(&(Print.printNum)); // 페이지 개수
        InputIntData(&(Print.index)); // array 번째

        // 데이터 넣기
        for (j = 0; j < Print.printNum; j++)
        {
            QueueInsertData(&Queue, j);
            TableInsertData(&Table, Queue.arry[j].data);
        }

        QueuePopData(&Queue, &Table);
    }

    return 0;
}
```