# 1874 스택 수열

URL : [https://www.acmicpc.net/problem/1874](https://www.acmicpc.net/problem/1874)

```c
#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0

char result[100001];

typedef int Data;

typedef struct _FirstNum
{
	int N; // (1 ≤ n ≤ 100,000)
} FirstNum;

typedef struct _OrderNum
{
	int N; // (1 ≤ n ≤ 100,000)
} OrderNum;

typedef struct _Node
{
	Data data;
	struct _Node* next;
} Node;

typedef struct _StackList
{
	int dataCount;
	int curNum;
	Node* head;
} StackList;

void StackInit(StackList* pstack)
{
	pstack->head = NULL;
}

int SIsEmpty(StackList* pstack)
{
	if (pstack->head == NULL)
		return TRUE;
	else
		return FALSE;
}

void SPush(StackList* pstack, Data data)
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	newNode->next = pstack->head;
	pstack->head = newNode;
}

Data SPop(StackList* pstack)
{
	Data rdata;
	Node* rnode;

	if (SIsEmpty(pstack))
	{
		printf("Stack Memory Error!\n");
		exit(-1);
	}

	rnode = pstack->head;
	rdata = pstack->head->data;

	pstack->head = pstack->head->next;

	free(rnode);
	return rdata;
}

void InputDataFirstNum(FirstNum* FN)
{
	scanf("%d", &FN->N);
}

void InputDataOrderNum(OrderNum* ON)
{
	scanf("%d", &ON->N);
}

int main(void)
{
	int i;
	int resultinedx = 0;

	FirstNum FN;
	OrderNum ON;
	StackList SL;

	// 데이터 숫자 입력
	InputDataFirstNum(&FN);

	// 노드 초기화
	SL.curNum = 1;
	StackInit(&SL);

	for (i=0; i < FN.N; i++)
	{	
		// 수열 데이터 받기
		InputDataOrderNum(&ON);

		// 입력 받은수가 크면 데이터 삽입
		if (ON.N >= SL.curNum)
		{	
			// 입력 받은 숫자 까지 Push
			while (ON.N >= SL.curNum)
			{
				SPush(&SL, SL.curNum);
				(SL.curNum)++;
				result[resultinedx++] = '+';
			}

			// 삽입한 마지막 숫자 Pop
			result[resultinedx++] = '-';
			SPop(&SL);
		} // 입력 받은수가 작으면
		else if (ON.N < SL.curNum)
		{
			if (ON.N != SPop(&SL))
			{	// 수열 불가능 
				printf("NO");
				return 0;
			}
			else
			{
				result[resultinedx++] = '-';
			}
		}
	}

	// 결과
	for (i = 0; i<resultinedx; i++)
	{
		printf("%c\n", result[i]);
	}
	return 0;
}
```

숏 코딩

```c
//스택 수열
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
	int n = 0;
	int max = 2;

	scanf("%d", &n);
	if(1 > n || n > 100000) return 0;

	int * sequence = (int *)malloc(sizeof(int) * n);
	if(sequence == NULL) return 0;
	memset(sequence, 0, n);

	int sp = 0;
	int * stackProcess = (int *)malloc(sizeof(int) * n * 2);
	if(stackProcess == NULL) return 0;
	memset(stackProcess, -1, n*2);

	Stack * stack = createStack();

	for(int i = 0; i < n; i++)
		scanf("%d", (sequence + i));

//	for(int i = 0; i < n; i++)
//		fprintf(stdout, "%4d", *(sequence + i));

	stack->push(stack, 1);
	stackProcess[sp] = 1;
	sp++;

	for(int i = 0; i < n; i++)
	{
//		fprintf(stdout, "sequence, top : %d, %d\n", sequence[i], stack->top(stack));
		if(sequence[i] > stack->top(stack))
		{
			for(int j = max; sequence[i] > stack->top(stack); j++)
			{
//				fprintf(stdout, "\t\t j : %d\n", j);
				stack->push(stack, j);
				stackProcess[sp] = 1;
				sp++;
				max++;
			}
			
//			fprintf(stdout, "\t\ttop : %d\n", stack->top(stack));
		}

		if(sequence[i] == stack->top(stack))
		{
//			fprintf(stdout, "\tpop : %d\n", stack->top(stack));
			stack->pop(stack);
			stackProcess[sp] = 0;
			sp++;
		}
		else if(sequence[i] < stack->top(stack))
		{
			stackProcess[0] = -1;
			break;
		}
	}

	for(int i = 0; i < n*2; i++)
	{
		if(stackProcess[i] == -1)
		{
			fprintf(stdout, "NO\n");
			break;
		}
		else if(stackProcess[i] == 0)
		{
			fprintf(stdout, "-\n");
		}
		else if(stackProcess[i] == 1)
		{
			fprintf(stdout, "+\n");
		}
	}

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
#include <stdlib.h>

typedef struct s_operation
{
    char sign;
    struct s_operation *next;
}   t_operation;

typedef struct s_operation_record
{
    t_operation *head;
    t_operation *tail;
}   t_operation_record;

typedef struct s_stack_node
{
    int data;
    struct s_stack_node *prev;
}   t_stack_node;

typedef struct s_stack
{
    t_stack_node *top;
}   t_stack;

int *create_array(int size, int type)
{
    int *new_array;
    int index;

    index = 0;
    new_array = (int*) malloc(sizeof(int)*size);
    while(index < size)
    {
        (type == 0) ? (new_array[index] = 0) : (new_array[index] = index + 1);
        index++;
    }

    return (new_array);
}

t_operation *create_operation(void)
{
    t_operation *new;
    
    new = (t_operation*) malloc(sizeof(t_operation));
    new -> next = NULL;
    
    return (new);
}

t_operation_record *create_record(void)
{
    t_operation_record *new;

    new = (t_operation_record*) malloc(sizeof(t_operation_record));
    new -> tail = NULL;

    return (new);
}

t_stack_node *create_stack_node(int data)
{
    t_stack_node *new;

    new = (t_stack_node*) malloc(sizeof(t_stack_node));
    new -> data = data;
    new -> prev = NULL;

    return (new);
}

t_stack *create_stack_list(void)
{
    t_stack *new;
    
    new = (t_stack*) malloc(sizeof(t_stack));
    new -> top = NULL;

    return (new);
}

void buffer_clear(void)
{
    while(getchar() != '\n');
}

void push_stack(t_operation_record **my_record, t_stack **my_stack, int data)
{
    t_stack_node *new_stack;
    t_operation *new_operation;

    new_stack = create_stack_node(data);
    new_operation = create_operation();
    new_operation->sign = '+';
    if ((*my_stack)->top == NULL)
    {
        (*my_stack)->top = new_stack;
    }
    else
    {
        new_stack->prev = (*my_stack)->top;
        (*my_stack)->top = new_stack;
    }

    if ((*my_record)->head == NULL)
    {
        (*my_record)->head = new_operation;
        (*my_record)->tail = new_operation;

    }
    else
    {
        (*my_record)->tail->next = new_operation;
        (*my_record)->tail = new_operation;

    }
}

void pop_stack(t_operation_record **my_record, t_stack **my_stack)
{
    t_operation *new_operation;
    t_stack_node *target_node;

    new_operation = create_operation();
    new_operation -> sign = '-';
    
    (*my_record) -> tail -> next = new_operation;
    (*my_record) -> tail = new_operation;
    if ((*my_stack) -> top ->  prev == NULL)
    {
        target_node = (*my_stack) -> top;
        (*my_stack) -> top = NULL;
    }
    else
    {
        target_node = (*my_stack) -> top;
        (*my_stack) -> top = (*my_stack) -> top -> prev;
    }
    target_node -> data = 0;
    target_node -> prev = NULL;
    free(target_node);
}

int check_stack_sequence(t_operation_record **my_record, int *sequence, int size)
{
    int index_seq;
    int index_asc;
    int *ascending;
    t_stack *my_stack;

    index_seq = 0;
    index_asc = 0;
    ascending = create_array(size, 1);
    my_stack = create_stack_list();
    while(index_seq < size )
    {
        if (my_stack -> top == NULL || my_stack -> top -> data < sequence[index_seq])
        {
            push_stack(my_record, &my_stack, ascending[index_asc]);
                index_asc++;
        }
        if (my_stack -> top != NULL)
        {
            if (my_stack -> top -> data > sequence[index_seq])
            {
                return (0);
            }
            else if (my_stack -> top -> data == sequence[index_seq])
            {
                pop_stack(my_record, &my_stack);
                index_seq++;
            }
        }
    }
    return (1);
}

void print_record(t_operation_record *my_record)
{
    t_operation *current;

    current = my_record -> head;
    while(current != NULL)
    {
        printf("%c\n",current -> sign);
        current = current->next;
    }
}

int main(void)
{
    t_operation_record *my_record;
    int total_number;
    int index;
    int *sequence;
    int aa;

    index = 0;
    my_record = create_record();
    scanf("%d",&total_number);
    //buffer_clear(); 
    sequence = create_array(total_number, 0);
    while(index < total_number)
    {
        scanf("%d",&sequence[index]);
        //buffer_clear();
        index++;
    }

    aa= check_stack_sequence(&my_record, sequence, total_number);
    if (aa)
    {
        print_record(my_record);
    }
    else
    {
        printf("NO\n");
    }

    return(0);
}
```

```c
#pragma warning(disable: 4996)
#include <stdio.h>
#include <stdlib.h>

#define TRUE    1
#define FALSE   0

#define STACK_LEN	100000

typedef int Data;

typedef struct _arrayStack
{
	Data stackArr[STACK_LEN];
	int topIndex;
} ArrayStack;

typedef ArrayStack Stack;

void StackInit(Stack* pstack)//스택 초기화
{
	pstack->topIndex = -1;
}

int SIsEmpty(Stack* pstack)// 스택 비어있는지 확인하고 비어있으면 1 차있으면 0
{
	if (pstack->topIndex == -1)
		return TRUE;
	else
		return FALSE;
}

void SPush(Stack* pstack, Data data) // data 값을 스택에 쌓음
{
	pstack->topIndex += 1;
	pstack->stackArr[pstack->topIndex] = data;
}

Data SPop(Stack* pstack)  // 스택 최상위에 있는거 삭제하고 삭제한 데이터 반환
{
	int rIdx;

	if (SIsEmpty(pstack))
	{
		printf("Stack Memory Error!");
		exit(-1);
	}

	rIdx = pstack->topIndex;
	pstack->topIndex -= 1;

	return pstack->stackArr[rIdx];
}

Data SPeek(Stack* pstack)// SPop와 다르게 삭제는 안하고 맨위에 뭐가 쌓였는지 확인함
{
	if (SIsEmpty(pstack))
	{
		printf("Stack Memory Error!");
		exit(-1);
	}

	return pstack->stackArr[pstack->topIndex];
}
int max_fun(int a, int b)//a가 기존 b가 새로운거, 비교하고 큰거 반환
{
	int max;
	if (a < b) {
		max = b;
		return max;
	}
	return a;
}
int main(void) {
	Stack stack;
	StackInit(&stack);
	int num;// num은 입력받을 갯수
	int a;//스택에 쌓을 정수
	char c[200001];//+- 기호 쌓을 문자
	int max = 0;//  1 2 3 4 5 6 중복안하고 2 끝나면 1부터 말고 3으로 시작할 수 있게 쓰는용
	int i, j;
	int c_index = -1;

	scanf("%d", &num);

	for (i = 0; i < num; i++) {
		scanf("%d", &a);   //   4 3 6 8 7 5 2 1

		if ((SIsEmpty(&stack)) || (SPeek(&stack) < a)) {//방금 받아낸 a[i]가 현재 스택에 쌓여있는 최고치보다 클경우 
			for (j = max + 1; j <= max_fun(max, a); j++) {

				SPush(&stack, j);
				c[++c_index] = '+';
			}
			max = max_fun(max, a);
			SPop(&stack);
			c[++c_index] = '-';

		}
		else if (SPeek(&stack) == a) {// 방금 받아낸거랑 현재 스택에 쌓여있는 최고치랑 같은경우에만

			SPop(&stack);
			c[++c_index] = '-';

		}
		else {  // 위에 두경우가 아니면 모두 else 하고 끝냄
			printf("NO");
			return 0;
		}
	}

	for (int i = 0; i <= c_index; i++)
		printf("%c\n", c[i]);

	return 0;

}
```