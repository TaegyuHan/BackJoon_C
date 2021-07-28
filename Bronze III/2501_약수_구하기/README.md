# 2501 약수 구하기

URL : [https://www.acmicpc.net/problem/2501](https://www.acmicpc.net/problem/2501)

```c
#include <stdio.h>

typedef struct _Number
{
	int N; // ( 1 <= N <= 10,000 )
	int K; // ( 1 <= K <= N )
} Number;

void InputData(Number * Number)
{
	scanf("%d %d",
		&Number->N,
		&Number->K );
}

int checkDivisor(Number* Number, int num)
{
	if ((Number->N % num) == 0)
		return 1;
	else
		return 0;
}

int main(void) {

	int i;
	int sum=0;
	Number Number;
	InputData(&Number);

	for (i = 1; i <= Number.N; i++)
	{
		sum += checkDivisor(&Number, i);
		if (Number.K == sum)
		{
			printf("%d", i);
			return 0;
		}
	}

	printf("0");

	return 0;
}
```

숏 코딩

```c
#include <stdio.h>
#include <stdlib.h>
struct list{
    int data;
    struct list *next;
};
int main(void)
{
    struct list *node, *head;
    int i,j,num,count,yak=0;
    scanf("%d %d",&num,&count);
    node=(struct list *)malloc(sizeof(struct list));
    head=node;
    for (i=1;i<=num;i++)
    {
        if ((num%i)==0)
        {
            node->data=i;
            node->next=(struct list *)malloc(sizeof(struct list));
            node=node->next;
            yak++;
        }
    }
    node=head;
    if (yak<count)
        printf("0");
    else
    {
        count--;
    	for (;node;node=node->next)
  	 	{
 	     	 if (count==0)
             {
                 printf("%d",node->data);
             }
            count--;
  	 	}
    }
    return 0;
}
```

```c
#include <stdio.h>
#include <math.h>

int main(){
  int n, k, range, cnt = 0, max, i;
  int factor[100];

  scanf("%d %d", &n, &k);

  range = (int) sqrt(n);

  for (i = 1; i <= range; i++){
    if (n % i == 0){ 
      factor[cnt] = i;
      cnt ++; 
    }   
  }

  max = cnt * 2;

  if (range * range == n)
    max --; 

  if (max < k)
    printf("0");
  else if (k <= cnt)
    printf("%d", factor[k - 1]);
  else{
    k --; 
    
    if (range * range == n)
      printf("%d", n / factor[2 * cnt - k - 2]);
    else
      printf("%d", n / factor[2 * cnt - k - 1]);
  }

  return 0;
}
```