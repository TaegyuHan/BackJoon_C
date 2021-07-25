# 5565 영수증

URL : [https://www.acmicpc.net/problem/5565](https://www.acmicpc.net/problem/5565)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

#define INPUT_DATA_COUNT 9

typedef struct book
{
    int price; // 1 <= price <= 10,000
} Book;

void inputData(Book * Book)
{
    scanf("%d", &Book->price);
}

int main(void)
{
    int i;
    int SumBookPrice;
	Book Book;

    scanf("%d", &SumBookPrice);

    for(i=0; i<INPUT_DATA_COUNT; i++)
    {
        inputData(&Book);
        SumBookPrice -= Book.price;
    }

    printf("%d", SumBookPrice);

    return 0;
}
```