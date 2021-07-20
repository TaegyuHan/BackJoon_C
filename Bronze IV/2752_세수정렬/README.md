# 2752 세수정렬

URL : [https://www.acmicpc.net/problem/2752](https://www.acmicpc.net/problem/2752)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

struct numberList
{
    int number[3];
};

void BubbleSort(int numberlist[])
{
    int i, j;
    int temp;

    for(i=0; i<3; i++)
    {
        for(j=i+1; j<3; j++)
        {
            if(numberlist[i] > numberlist[j])
            {
                temp = numberlist[i];
                numberlist[i] = numberlist[j];
                numberlist[j] = temp;
            }
        }
    }

    for(i=0; i<3; i++)
    {
        if(i==3) printf("%d", numberlist[i]);
        else printf("%d ", numberlist[i]);
    }
}

int main(void)
{

    int i;
    struct numberList numberList;

    for(i=0; i<3; i++)
        scanf("%d", &numberList.number[i]);

    BubbleSort(numberList.number);

	return 0;
}
```

숏 코드

```c
#include <stdio.h>

void swap(int *a, int *b){
	int temp = *a;
	*a = *b;
	*b = temp;
}

int main(){
	int a, b, c;

	scanf("%d %d %d", &a, &b, &c);

	if(a > b)
		swap(&a, &b);
	if(c < b)
		swap(&c, &b);
	if(a > b)
		swap(&a, &b);

	printf("%d %d %d\n", a, b, c);
	
	return 0;
}
```