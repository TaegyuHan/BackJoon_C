# 4101 크냐?

URL : [https://www.acmicpc.net/problem/4101](https://www.acmicpc.net/problem/4101)

```c
#include <stdio.h>

typedef struct _NumberCheck
{
	int A;
	int B;
} NumberCheck;

void InputData(NumberCheck* NC)
{
	scanf("%d %d",
			&NC->A,
			&NC->B );
}

int CheckNum(NumberCheck* NC)
{
	if (NC->A > NC->B)
		return 1;
	else if (NC->A <= NC->B)
		return -1;
}

void ShowResult(int state)
{
	if (state == 1)
		printf("Yes\n");
	else if (state == -1)
		printf("No\n");
}

int main(void) 
{
	int state;
	NumberCheck NC = { 1, 1 };

	while (1)
	{
		InputData(&NC);
		if (NC.A == 0 && NC.B == 0) break;
		state = CheckNum(&NC);
		ShowResult(state);
	}

	return 0;
}
```

숏 코딩

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct result{
	char res[10];
    struct result *next;
};
int main(void)
{
    struct result *node,*head;
    int num1,num2;
    head=(struct result *)malloc(sizeof(struct result));
    node=head;
    while(1)
    {
        scanf("%d %d",&num1,&num2);
        if (num1==0 && num2==0)
        {
            node=NULL;
            break;
        }
        if (num1>num2)
            strcpy(node->res,"Yes");
        else
            strcpy(node->res,"No");
        node->next=(struct result *)malloc(sizeof(struct result));
        node=node->next;
    }
    node=head;
    for (;node;node=node->next)
        printf("%s\n",node->res);
    return 0;
}
```

```c
#include<stdio.h>
int main()
{
    int a, b;
    while(1)
    {
        scanf("%d %d", &a, &b);
        if(a == 0 && b == 0)
        {
            return 0;
        }
        else if(a > b)
        {
            printf("Yes\n");
        }
        else
        {
            printf("No\n");
        }
        
    }
    return 0;
}
```

```c
#include <stdio.h>
int main() {
  int a,b;
  while(1){
      scanf("%d",&a);
      scanf("%d",&b);
      if(a>b){
          printf("Yes\n");
      }
      else if(a==0&&b==0){
    
      }

      else if(a<=b){
          printf("No\n");
      }

      if(a==0&&b==0){break;}
  }
      return 0;
}
```