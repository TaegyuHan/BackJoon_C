# 4949 균형잡힌 세상

URL : [https://www.acmicpc.net/problem/4949](https://www.acmicpc.net/problem/4949)

```c
#include <stdio.h>

#define STRING_LEN 102
#define TRUE 1

typedef struct _Stack
{
	char stack[STRING_LEN];
	int cur;
} Stack;

typedef struct _StrList
{
	char string[STRING_LEN];
} StrList;

void resultShow(char num)
{	// 결과 확인
	if (num == 0)
		printf("yes\n");
	else
		printf("no\n");
}

void PrenthesesCheck(StrList* SL, int lastCheck)
{	// 괄호 확인

	int i;
	Stack Stack = { {0, }, 0 };

	for (i = 0; SL->string[i] != NULL; i++)
	{
		//printf("%d", SL->string[i]);

		// 데이터 추가
		if (SL->string[i] == '(')
		{	// 괄호 오픈 데이터 추가
			Stack.stack[Stack.cur] = '1';
			Stack.cur++;
		}
		else if (SL->string[i] == '[')
		{	// 괄호 오픈 데이터 추가
			Stack.stack[Stack.cur] = '2';
			Stack.cur++;
		}
		else if (SL->string[i] == ')' &&
					   Stack.stack[Stack.cur - 1] == '1')
		{	// 괄호 오픈 후 괄호 닫기 데이터 삭제
			Stack.cur--;
			Stack.stack[Stack.cur] = 0;
		} 
		else if (SL->string[i] == ')')
		{
			Stack.stack[Stack.cur] = '-1';
			Stack.cur++;
			resultShow(Stack.stack[0]);
			return;
		}
		else if (SL->string[i] == ']' &&
			  		 Stack.stack[Stack.cur - 1] == '2')
		{	// 괄호 오픈 후 괄호 닫기 데이터 삭제
			Stack.cur--;
			Stack.stack[Stack.cur] = 0;
		}
		else if (SL->string[i] == ']')
		{
			Stack.stack[Stack.cur] = '-2';
			Stack.cur++;
			resultShow(Stack.stack[0]);
			return;
		}

	}
	//printf("\n");
	resultShow(Stack.stack[0]);
}

void InputDataString(StrList* SL)
{	// 문자열 괄호 입력
	fgets(SL->string, STRING_LEN, stdin);
}

int StingEndCheck(StrList* SL)
{
	if (SL->string[0] == 46 && SL->string[1] == 10)
	{
		//printf("StingEndCheck : %d\n", 0);
		return 1;
	}
	else
	{
		//printf("StingEndCheck : %d\n", 1);
		return 0;
	}
		
}

int main(void)
{
	StrList SL;
	int lastCheck = 0;

	while (TRUE)
	{
		InputDataString(&SL);
		if (StingEndCheck(&SL)) break;

		PrenthesesCheck(&SL, lastCheck);
	}

	return 0;
}
```

숏 코딩

```c
//균형잡힌 세상
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node
{
	int data;
	struct Node * next;

	void (*init)(struct Node *, int);
	void (*free)(struct Node *);
}Node;

Node * createNode(int);
void initNode(Node *, int);
void freeNode(Node *);

typedef struct Stack
{
	Node * head;

	void (*init)(struct Stack *);
	void (*free)(struct Stack *);
	void (*clear)(struct Stack *);

	void (*push)(struct Stack *, int);
	int (*pop)(struct Stack *);
	int (*size)(struct Stack *);
	int (*isEmpty)(struct Stack *);
	int (*top)(struct Stack *);
	void (*display)(struct Stack *);
}Stack;

Stack * createStack();
void initStack(Stack *);
void freeStack(Stack *);
void clearStack(Stack *);

void push(Stack *, int);
int pop(Stack *);
int size(Stack *);
int isEmptyStack(Stack *);
int top(Stack *);
void displayStack(Stack *);

int main()
{
	int count = 0;
	int size = 2;
	int * result = (int *)malloc(sizeof(int));

	char * string = (char *)malloc(sizeof(char) * 104);
	memset(string, 0, 104);

	Stack * stack = createStack();

	for(;;)
	{
		fgets(string, 104, stdin);
		string[strlen(string) - 1] = 0x00;
		int length = strlen(string);
		if(length > 101) break;

		if(strncmp((string + 0), ".", 1) == 0) break;
//		fprintf(stdout, "length : %ld\n", strlen(string));
//		fprintf(stdout, "문자열\n%s\n", string);

		count++;
		if(count == size)
		{
			size *= 2;
			result = realloc(result, sizeof(int) * size);
		}

		for(int i = 0; i < length; i++)
		{
			if(strncmp((string + i), "(", 1) == 0)
			{
				stack->push(stack, 2);
			}
			else if(strncmp((string + i), "[", 1) == 0)
			{
				stack->push(stack, 3);
			}
			else if(strncmp((string + i), ")", 1) == 0)
			{
				if(stack->top(stack) == 2) stack->pop(stack);
				else
				{
					stack->push(stack, -2);
				}
			}
			else if(strncmp((string + i), "]", 1) == 0)
			{
				if(stack->top(stack) == 3) stack->pop(stack);
				else
				{
					stack->push(stack, -3);
				}
			}
		}

		if(stack->top(stack) == -1)
		{
			result[count - 1] = 1;
		}
		else
		{
			result[count - 1] = 0;
		}
		
//		stack->display(stack);
		stack->clear(stack);
		for(int i = 0 ; i < strlen(string); i++)
			memset(string + i, 0, 1);
	}

	for(int i = 0; i < count; i++)
	{
		fprintf(stdout, "%s\n", result[i] == 1 ? "yes" : "no");
	}

	stack->free(stack);

	return 0;
}

Node * createNode(int data)
{
	Node * newNode = (Node *)malloc(sizeof(Node));

	newNode->init = initNode;
	newNode->init(newNode, data);

	return newNode;
}

void initNode(Node * node, int data)
{
	node->data = data;
	node->next = NULL;

	node->free = freeNode;

	return ;
}

void freeNode(Node * node)
{
	node->data = 0;
	node->next = NULL;

	free(node);
	
	return ;
}

Stack * createStack()
{
	Stack * newStack = (Stack *)malloc(sizeof(Stack));

	newStack->init = initStack;
	newStack->init(newStack);

	return newStack;
}

void initStack(Stack * stack)
{
	stack->head = NULL;

	stack->free = freeStack;
	stack->clear = clearStack;

	stack->push = push;
	stack->pop = pop;
	stack->size = size;
	stack->isEmpty = isEmptyStack;
	stack->top = top;
	stack->display = displayStack;

	return ;
}

void freeStack(Stack * stack)
{
	if(stack->isEmpty(stack))
	{
		free(stack);

		return ;
	}

	while(stack->head != NULL)
	{
		Node * node = stack->head;

		stack->head = stack->head->next;

		node->free(node);
		node = NULL;
	}

	stack->head = NULL;
	free(stack);

	return ;
}

void clearStack(Stack * stack)
{
	if(stack->isEmpty(stack))
	{
		return ;
	}

	for(int i = stack->size(stack); i > 0; i--)
	{
		stack->pop(stack);
	}
	
	stack->head = NULL;
	
	return ;
}

void push(Stack * stack, int data)
{
	Node * node = createNode(data);

	if(stack->isEmpty(stack))
	{
		stack->head = node;

		return ;
	}

	node->next = stack->head;
	stack->head = node;

	return ;
}

int pop(Stack * stack)
{
	if(stack->isEmpty(stack))
	{
		return 0;
	}

	int pop = 0;
	Node * node = stack->head;
	stack->head = stack->head->next;
	
	pop = node->data;

	node->free(node);
	node = NULL;
	

	return pop;
}

int size(Stack * stack)
{
	if(stack->isEmpty(stack))
	{
		return 0;
	}

	int size = 0;

	for(Node * temp = stack->head; temp != NULL && ++size; temp = temp->next)
	{
	}
	
	return size;
}

int isEmptyStack(Stack * stack)
{
	return stack->head == NULL ? 1 : 0;
}

int top(Stack * stack)
{
	if(stack->isEmpty(stack))
	{
		return -1;
	}

	return stack->head->data; 
}

void displayStack(Stack * stack)
{
	if(stack->isEmpty(stack))
	{
		fprintf(stdout, "stack이 비어있습니다.\n");

		return ;
	}

	for(Node * temp = stack->head; temp != NULL; temp = temp->next)
	{
		fprintf(stdout, "%4d", temp->data);
	}
	puts("");

	return ;
}
```

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#define STACK_LENGTH 110

/* 스택 정의 */
typedef struct _stack {
  int arr[110];
  int top;
} Stack;

/* 스택 연산 */
void push(Stack *stack, int data);
int pop(Stack *stack);
bool empty(Stack *stack);

/* main 함수 */
int main() {
  char testStr[110];
  char endStr[110];

  fgets(testStr, 110, stdin);
  strcpy(endStr, ".\n");

  while( strcmp(testStr, endStr) != 0) {
    Stack rawstack;
    Stack *stack = &rawstack;
    stack->top = -1;

    int j=0;
    for (; testStr[j] != '\0'; j++) {
      if (testStr[j] == '(')
        push(stack, (int) testStr[j]);
      else if (testStr[j] == '[')
        push(stack, (int) testStr[j]);
      else if (testStr[j] == ')') {
        int result = pop(stack);
        if (result != (int) '(')
          break;
      }
      else if (testStr[j] == ']') {
        int result = pop(stack);
        if (result != (int) '[')
          break;
      }
    }
    
    if (stack->top != -1 || testStr[j] != '\0')
      printf("no\n");
    else
      printf("yes\n");

    fgets(testStr, 110, stdin);
  }

  return 0;
}

/* 스택 연산 구현 */
void push(Stack *stack, int data) {
    stack->arr[ ++stack->top ] = data;
}
int pop(Stack *stack) {
    if (empty(stack))
      return 0;

    int data = stack->arr[ stack->top ];
    stack->top--;
    return data;
}
bool empty(Stack *stack) {
    return stack->top == -1;
}
```

```c
#include <stdio.h>
#define MAX_STACK_SIZE 101

int data[MAX_STACK_SIZE];
int top;
char str[MAX_STACK_SIZE];

void push(int i){
	
	top++;
	data[top] = str[i];
}

int pop(int i){
	
	if((str[i] == ')' && data[top] == '(') || (str[i] == ']' && data[top] == '[')){
		top--;
		return 1;
	}
	else{
		return 0;
	}
}

int main(int argc, char *argv[]){

	while(1){
		
		gets(str);
		
		top = -1;
		int n = 1;
		
		if(str[0] == 46){//.
			break;
		}
		
		for(int i = 0; str[i] != 46; i++){
			if(!n)
				continue;
			if(str[i]=='(')
				push(i);
			if(str[i]=='[')
				push(i);
			if(str[i]==']')
				n = pop(i);
			if(str[i]==')')
				n = pop(i);
		}
		
		if(top == -1 && n)
			printf("yes\n");
		else
			printf("no\n");
	}
		
	return 0;
}
```