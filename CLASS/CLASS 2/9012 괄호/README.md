# 9012 괄호

URL : [https://www.acmicpc.net/problem/9012](https://www.acmicpc.net/problem/9012)

```c
#include <stdio.h>

typedef struct _StrList
{
	char string[51];
} StrList;

typedef struct _Stack
{
	char stack[51];
	int cur;
} Stack;

void InputDataCount(int* cnt)
{	// 횟수 입력
	scanf("%d", cnt);
}

void InputDataString(StrList* SL)
{	// 문자열 괄호 입력
	scanf("%s", SL->string);
}

void resultShow(char num)
{	// 결과 확인
	if (num == 0)
		printf("YES\n");
	else
		printf("NO\n");
}

void PrenthesesCheck(StrList* SL)
{	// 괄호 확인
	int i;
	Stack Stack = { {0, }, 0 };

	for (i = 0; SL->string[i]!=NULL; i++)
	{
		if (SL->string[i] == '(')
		{	// 괄호 오픈 데이터 추가
			Stack.stack[Stack.cur] = 'O';
			Stack.cur++;
		}
		else if (SL->string[i] == ')' && 
				 Stack.stack[Stack.cur - 1] == 'O')
		{	// 괄호 오픈 후 괄호 닫기 데이터 삭제
			Stack.cur--;
			Stack.stack[Stack.cur] = 0;
		}
		else
		{	// 그냥 괄호 닫기 데이터 추가
			Stack.stack[Stack.cur] = 'C';
			Stack.cur++;
		}
	}
	resultShow(Stack.stack[0]);
}

int main(void)
{
	int cnt;
	int i;
	StrList SL;
	InputDataCount(&cnt);

	// 받은 수만큼 반복
	for(i=0; i<cnt; i++)
	{
		InputDataString(&SL);
		PrenthesesCheck(&SL);
	}

	return 0;
}
```

숏코딩

```c
//괄호
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

	void (*push)(struct Stack *, int);
	int (*pop)(struct Stack *);
	void (*clear)(struct Stack *);
	int (*size)(struct Stack *);
	int (*isEmpty)(struct Stack *);
	int (*top)(struct Stack *);
	void (*display)(struct Stack *);
}Stack;

Stack * createStack();
void initStack(Stack *);
void freeStack(Stack *);

void push(Stack *, int);
int pop(Stack *);
void clearStack(Stack *);
int size(Stack *);
int isEmptyStack(Stack *);
int top(Stack *);
void displayStack(Stack *);

int main()
{
	int n = 0;
	
	scanf("%d", &n);
	getchar();

	int * result = (int *)malloc(sizeof(int) * n);
	memset(result, 0, n);

	char ** string = (char **)malloc(sizeof(char *) * n);
	if(string == NULL) return 0;

	for(int i = 0; i < n; i++)
	{
		*(string + i) = (char *)malloc(sizeof(char) * 52); 
		if(*(string + i) == NULL) return 0;
		memset(*(string + i), 0, 52);
	}

	Stack * stack = createStack();

	for(int i = 0; i < n; i++)
	{
		fgets((*(string + i)), 52, stdin);
		int length = strlen((*(string + i))) - 1;
		if(length < 2 || length > 50) return 0;
		*(*(string + i) + strlen(*(string + i)) - 1) = 0x00;
	}

	for(int i = 0; i < n; i++)
	{
		int length = strlen((*(string + i)));
//		fprintf(stdout, "string[%d] : %s\n", length, string[i]);
		for(int j = 0; j < length; j++)
		{
//fprintf(stdout, "[%d, %d] %s ", i, j, (*(string + i) + j));
			if(strncmp((*(string + i) + j), "(", 1) == 0)
			{
//				puts("true");
				stack->push(stack, 0);
			}
			else
			{
//				puts("false");
				if(stack->top(stack) == 0) stack->pop(stack);
				else stack->push(stack, 1);
			}
		}

		if(stack->top(stack) == -1)
		{
			*(result + i) = 1;
		}
		else
		{
			*(result + i) = 0;
		}

//		stack->display(stack);
		stack->clear(stack);
//		stack->display(stack);
	}

	for(int i = 0; i < n; i++)
	{
		if(*(result + i) == 1) fprintf(stdout, "YES");
		else fprintf(stdout, "NO");
		fprintf(stdout, "\n");
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

	stack->push = push;
	stack->pop = pop;
	stack->size = size;
	stack->isEmpty = isEmptyStack;
	stack->top = top;
	stack->clear = clearStack;
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
		return -1;
	}

	int pop = 0;
	Node * node = stack->head;
	stack->head = stack->head->next;
	
	pop = node->data;

	node->free(node);
	node = NULL;

	return pop;
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
		fprintf(stdout, "stack이 비어있습니다.");
	}

	for(Node * node = stack->head; node != NULL; node = node->next)
	{
		fprintf(stdout, "%4d", node->data);
	}
	puts("");

	return ;
}
```

```c
/* baekjoon online judege  */
/* No.10828-Stack implementation */

#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <stdlib.h>

struct node {
	struct node *	prev;
	int		index;
	int		content;
};

struct node *top;

void push(int num);
int pop(void);
int size(void);
int empty(void);
int print_top(void);

int main(int argc, char const *argv[])
{
	top = (struct node *)malloc(sizeof(struct node));
	top->prev = NULL;
	top->index = 0;
	top->content = -1;

	int i;

	//check the number of commands
	int cmd_num;
	scanf("%d\n", &cmd_num);
	//make allocations of command and answers
	char *cmd = (char *)malloc(sizeof(char) * 50);
	int *ans_list = (int *)malloc(sizeof(int) * cmd_num);
	int k = 0;
	int success = 1;
	for (i = 0; i < cmd_num; i++) {
		success = 1;
		scanf("%s", cmd);

		for (k = 0; k < (int)strlen(cmd); k++) {
			if (!strncmp(&cmd[k], "(", 1)) {
				push(1);
			} else if (!strncmp(&cmd[k], ")", 1)) {
				int top = pop();
				if (top == -1) {
					ans_list[i] = 0;
					memset(cmd, 0, 50);
					success = 0;
					break;
				}
			}
		}

		if (success == 1) {
			if (size() != 0) {
				int tmp_size = size();
				for (k = 0; k < tmp_size; k++)
					pop();
				ans_list[i] = 0;
			} else {
				ans_list[i] = 1;
			}
		}
		memset(cmd, 0, 50);
	}

	for (i = 0; i < cmd_num; i++) {
		if (ans_list[i] == 1)
			printf("YES\n");
		else
			printf("NO\n");
	}

	free(cmd);
	free(ans_list);

	return 0;
}

void push(int num)
{
	struct node *new_node = (struct node *)malloc(sizeof(struct node));

	new_node->prev = top;
	new_node->index = top->index + 1;
	new_node->content = num;

	top = new_node;
}

int pop(void)
{
	int ret = top->content;

	if (top->prev == NULL)
		return -1;
	struct node *new_top = top->prev;
	free(top);
	top = new_top;
	return ret;
}

int size(void)
{
	return top->index;
}

int empty(void)
{
	if (top->index <= 0)
		return 1;
	else
		return 0;
}

int print_top(void)
{
	return top->content;
}
```