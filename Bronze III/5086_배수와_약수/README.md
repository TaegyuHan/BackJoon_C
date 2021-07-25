# 5086 배수와 약수

URL : [https://www.acmicpc.net/problem/5086](https://www.acmicpc.net/problem/5086)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct number
{
    int A; // (1 <= A <= 10,000)
    int B; // (1 <= B <= 10,000)
    int checkState; // ( 0 : 약수, 1 : 배수, 2 : 모두아니다. )
} Number;

void inputData(Number * Number)
{
    scanf("%d %d",
            &Number->A, 
            &Number->B  );
}

void divisor(Number * Number)
{
    Number->checkState = 2;
    if(Number->B%Number->A == 0)
        Number->checkState = 0;
}

void multiple(Number * Number)
{
    Number->checkState = 2;
    if(Number->A%Number->B == 0)
        Number->checkState = 1;
}

void showResult(Number Number)
{
    switch(Number.checkState)
    {
        case 0:
            printf("factor\n");
            break;
        case 1:
            printf("multiple\n");
            break;
        case 2:
            printf("neither\n");
            break;
    }
}

int main(void)
{
    int i;
		Number Number = {1, 1, 2};

    // 0 0의 수를 받으면 멈춤
    while(1)
    {
        inputData(&Number);
        if(Number.A==0 && Number.B==0) break;

        (Number.A < Number.B) ? 
            divisor(&Number) : multiple(&Number);

        showResult(Number);
    }

    return 0;
}
```

숏 코딩

```c
# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# define OR ||
# define AND &&
# define T 1
# define F 0
# define Length 500
typedef struct beackJun5086 {
	int OneVal;
	int TwoVal;
	char Result[Length];
	struct beackJun5086* Link;
} beackJun5086, *PTRbeackJun5086;

typedef struct nodeType {
	beackJun5086* headNode;
	beackJun5086* tailNode;
	int dataCnt;
} nodeType, *PTRnodeType;

PTRbeackJun5086 createNode() {
	PTRbeackJun5086 Temp = (PTRbeackJun5086)malloc(sizeof(beackJun5086));
	return Temp;
} // end of createNode function

PTRnodeType STARTnode() {
	PTRnodeType Temp = (PTRnodeType)malloc(sizeof(nodeType));
	return Temp;
} // end of STAnode function

void __init__(nodeType** node) {
	(** node).headNode = NULL;
	(** node).tailNode = NULL;
	(** node).dataCnt = 0;
} // end of __init__ function

void __error__(char* errMessage) {
	fprintf(stderr, "%s\n", errMessage);
	exit(1);
} // end of __error__ function

void __factorMultiple__(beackJun5086** node) {
	//1. 첫번째 숫자가 두번째 숫자의 약수이다.
	//2. 첫번째 숫자가 두번째 숫자의 배수이다.
	//3. 첫번째 숫자가 두번쨰 숫자의 약수와 배수 모두 아니다
	int ResultOne = F;
	int ResultTwo = F;
	
	if ((** node).OneVal < (** node).TwoVal) { // CASE _1
		if ((** node).TwoVal % (** node).OneVal == 0) {
			ResultOne = T;
			strcpy((** node).Result, "factor\n");
		}
	}
	if ((** node).OneVal > (** node).TwoVal) { // CASE _2
		if ((** node).OneVal % (** node).TwoVal == 0) {
			ResultTwo = T;
			strcpy((** node).Result, "multiple\n");
		}
	}
	if (ResultOne == F AND ResultTwo == F) { 
		strcpy((** node).Result, "neither\n");
	}
} // end of __factorMultiple__ function

void __Printfunc__(nodeType** node) {
	int i; // index
	PTRbeackJun5086 index = NULL;
	index = (**node).headNode;
	for (i = 0; i < (** node).dataCnt; i++) {
		printf("%s", index->Result);
		index = index->Link;
	}
} // end of __Printfunc__ function

int main(void) {
	//_____________________________________________________________________
	PTRnodeType STRnode = STARTnode();
	if (STRnode == NULL) { __error__("memory allocation error ... !!!"); }
	else { // STRnode !	= NULL
		STRnode->dataCnt = 0;
		STRnode->headNode = NULL;
		STRnode->tailNode = NULL;
	}
	//_____________________________________________________________________
	while (T) {
		PTRbeackJun5086 newNode = createNode();
		if (newNode == NULL) { __error__("memory allocation error ... !!!"); }
		else { //newNode != NULL
			memset(newNode, 0, sizeof(beackJun5086));
			scanf("%d %d", &newNode->OneVal, &newNode->TwoVal);
			
			if (newNode->OneVal == 0 OR newNode->TwoVal == 0) {
				break;
			}
			STRnode->dataCnt++;
			__factorMultiple__(&newNode);
			if (STRnode->dataCnt == 1) {
				STRnode->headNode = newNode;
				STRnode->tailNode = newNode;
			}
			else { // STRnode->dataCnt > 1
				STRnode->tailNode->Link = newNode;
				STRnode->tailNode = newNode;
			}
		}
	}
	if (STRnode->dataCnt != 0) {
		__Printfunc__(&STRnode);
	}
	return 0;
} // end of main function
```

```c
#include <stdio.h>
#include <stdlib.h>
struct node{
    int data;
    struct node *next;
};
int main(void)
{
    int a,b,i,n;
    struct node *Nnode,*head;
    Nnode=(struct node *)malloc(sizeof(struct node));
    head=Nnode;
    scanf("%d %d",&a,&b);
    while (1)
    {
        if (a==0 && b==0)
            break;
        if (a%b==0)
            Nnode->data=2;
        else if (b%a==0)
            Nnode->data=1;
            else
            Nnode->data=0;
        scanf("%d %d",&a,&b);
        if (a==0 && b==0)
            break;
        Nnode->next=(struct node *)malloc(sizeof(struct node));
        Nnode=Nnode->next;
    }
    for(;head;head=head->next)
    {
        if (head->data==2)
            printf("multiple\n");
        else if (head->data==1)
            printf("factor\n");
            else
            printf("neither\n");
    }
    return 0;
}
```