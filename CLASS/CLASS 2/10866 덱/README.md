# 10866 덱

URL : [https://www.acmicpc.net/problem/10866](https://www.acmicpc.net/problem/10866)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>
#include <string.h>

// 배열 출력하기
// void showArry(int arr[], int DequeCnt); 

// 문자열 비교 함수
// int strcmp(char str1[], const char str2[]); 

// 정수 X를 덱의 앞에 넣는다.
void push_front(int arr[], int DequeCnt, int num); 

// 정수 X를 덱의 뒤에 넣는다.
void push_back(int arr[], int DequeCnt, int num); 

// 덱의 가장 앞에 있는 정수를 출력한다. 
// 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
void front(int arr[], int DequeCnt); 

// 덱의 가장 뒤에 있는 정수를 출력한다. 
// 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
void back(int arr[], int DequeCnt);

// 덱에 들어있는 정수의 개수를 출력한다.
void size(int DequeCnt);

// 덱이 비어있으면 1을, 아니면 0을 출력한다.
void empty(int DequeCnt);

// 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 
// 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
void pop_front(int arr[], int DequeCnt);

// 의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 
// 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
void pop_back(int arr[], int DequeCnt);

int main(void)
{
    int Deque[100001] = {0,};
    int cnt, tempNum, DequeCnt=0;
    char type[11];
    
    scanf("%d", &cnt);

    while(cnt--)
    {

        scanf("%s", type);

        if(!strcmp(type, "push_front"))
        {
            scanf("%d", &tempNum);
            push_front(Deque, DequeCnt, tempNum);
            DequeCnt++;
        }
        else if(!strcmp(type, "push_back"))
        {
            scanf("%d", &tempNum);
            push_back(Deque, DequeCnt, tempNum);
            DequeCnt++;
        }
        else if(!strcmp(type, "pop_front"))
        {
            pop_front(Deque, DequeCnt);
            if(DequeCnt==0) continue;
            DequeCnt--;
        }
        else if(!strcmp(type, "pop_back"))
        {
            pop_back(Deque, DequeCnt);
            if(DequeCnt==0) continue;
            DequeCnt--;
        }
        else if(!strcmp(type, "empty"))
        {
            empty(DequeCnt);
        }
        else if(!strcmp(type, "front"))
        {
            front(Deque, DequeCnt);
        }
        else if(!strcmp(type, "back"))
        {
            back(Deque, DequeCnt);
        }
        else if(!strcmp(type, "size"))
        {
            size(DequeCnt);
        }

    }
	return 0;
}

// void showArry(int arr[], int DequeCnt)
// {
//     int i;
//     for(i=0; i<DequeCnt; i++)
//         printf("%d ", arr[i]);
//     printf("\n");
// }

// 문자열 비교 함수
// int strcmp(char str1[], const char str2[])
// {
//     int i;
//     for(i=0; str2[i]!=NULL; i++)
//     {
//         if(str2[i]!=str1[i])
//             return 0;
//     }

//     return 1;
// }

// 정수 X를 덱의 앞에 넣는다.
void push_front(int arr[], int DequeCnt, int num)
{
    int i;
    for(i=DequeCnt; i>=0; i--)
        arr[i+1] = arr[i];
    arr[0] = num;
}

// 정수 X를 덱의 뒤에 넣는다.
void push_back(int arr[], int DequeCnt, int num)
{
    arr[DequeCnt] = num;
}

// 덱의 가장 앞에 있는 정수를 출력한다. 
// 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
void front(int arr[], int DequeCnt)
{
    if(DequeCnt==0)
        printf("-1\n");
    else
        printf("%d\n", arr[0]);
}

// 덱의 가장 뒤에 있는 정수를 출력한다. 
// 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
void back(int arr[], int DequeCnt)
{
    if(DequeCnt==0)
        printf("-1\n");
    else
        printf("%d\n", arr[DequeCnt-1]);
}

// 덱에 들어있는 정수의 개수를 출력한다.
void size(int DequeCnt)
{
    printf("%d\n", DequeCnt);
}

// 덱이 비어있으면 1을, 아니면 0을 출력한다.
void empty(int DequeCnt)
{   
    if(DequeCnt==0)
        printf("1\n");
    else
        printf("0\n");
}

// 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 
// 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
void pop_front(int arr[], int DequeCnt)
{
    int i;
    if(DequeCnt==0)
    {
        printf("-1\n");
        return;
    }

    printf("%d\n", arr[0]);

    for(i=1; i<DequeCnt; i++)
        arr[i-1] = arr[i];
}

// 의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 
// 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
void pop_back(int arr[], int DequeCnt)
{
    if(DequeCnt==0)
    {
        printf("-1\n");
        return;
    }

    printf("%d\n", arr[DequeCnt-1]);
}
```

숏 코딩

```c
#include <stdio.h>
#include <string.h>

#define MAX_DEQ 10100

#define Increase(x) x = (x + 1) % MAX_DEQ
#define Decrease(x) x = x != 0 ? x - 1 : MAX_DEQ - 1
#define DeqEmpty() ((front + 1) % MAX_DEQ == back)

int main(void)
{
	int deque[MAX_DEQ];
	int front, back;

	int T, i;
	char input[15];
	int n;

	scanf("%d", &T);

	front = MAX_DEQ - 1;
	back = 0;

	for (i = 0; i < T; i++)
	{
		scanf("%s", input);

		if (!strcmp(input, "push_back"))
		{
			scanf("%d", &n);
			deque[back] = n;
			Increase(back);
		}

		else if (!strcmp(input, "push_front"))
		{
			scanf("%d", &n);
			deque[front] = n;
			Decrease(front);
		}

		else if (!strcmp(input, "front"))
			printf("%d\n", DeqEmpty() ? -1 : deque[front != MAX_DEQ - 1 ? front + 1 : 0]);

		else if (!strcmp(input, "back"))
			printf("%d\n", DeqEmpty() ? -1 : deque[back != 0 ? back - 1 : MAX_DEQ - 1]);

		else if (!strcmp(input, "pop_front"))
		{
			if (DeqEmpty())
				printf("-1\n");
			else
			{
				Increase(front);
				printf("%d\n", deque[front]);
			}
		}

		else if (!strcmp(input, "pop_back"))
		{
			if (DeqEmpty())
				printf("-1\n");
			else
			{
				Decrease(back);
				printf("%d\n", deque[back]);
			}
		}

		else if (!strcmp(input, "size"))
			printf("%d\n", back > front ? back - front - 1 : back + MAX_DEQ - front - 1);

		else
			printf("%d\n", DeqEmpty());
	}
}
```

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int deque[10000]; // 덱을 담을 배열
	int index = 0;
	int i, j;

	int count = 0; // 입력받을 횟수
	scanf("%d", &count);

	for (i = 0; i < count; i++) {

		char str[12]; // 명령어
		scanf("%s", str);

		if (!strcmp(str, "push_front")) {
			int x; // 담을 숫자
			scanf("%d", &x);
			for (j = index+1; j > 0; j--) {
				deque[j] = deque[j - 1];
			}
			deque[0] = x;
			index++;
		}
		else if (!strcmp(str, "push_back")) {
			int x; // 담을 숫자
			scanf("%d", &x);
			deque[index++] = x;
		}
		else if (!strcmp(str, "pop_front")) {
			if (index==0) {
				printf("-1\n");
			}
			else {
				printf("%d\n", deque[0]);
				for (j = 0; j < index; j++) {
					deque[j] = deque[j + 1];
				}
				index--;
			}
		}
		else if (!strcmp(str, "pop_back")) {
			if (index==0) {
				printf("-1\n");
			}
			else {
				printf("%d\n", deque[index-1]);
				index--;
			}
		}
		else if (!strcmp(str, "size")) {
			printf("%d\n", index);
		}
		else if (!strcmp(str, "empty")) {
			if (index==0)
				printf("1\n");
			else
				printf("0\n");
		}
		else if (!strcmp(str, "front")) {
			if (index==0)
				printf("-1\n");
			else
				printf("%d\n", deque[0]);
		}
		else if (!strcmp(str, "back")) {
			if (index==0)
				printf("-1\n");
			else
				printf("%d\n", deque[index - 1]);
		}
	}
	return 0;
}
```

```c
#include <stdio.h>

int main(void){
    int N, a, b, deque[20000]={0,}, i, back=10000, front=10001;
    char input[10];
    
    scanf("%d", &N);
    
    for(i=0;i<N;i++){
        scanf("%s", &input);
        
        if(strcmp(input,"push_front")==0){
            scanf("%d", &a);
            deque[front++]=a;
        }
        
        else if(strcmp(input,"push_back")==0){
            scanf("%d", &b);
            deque[back--]=b;
        }
        
        else if(strcmp(input,"pop_front")==0){
            if((front-back-1) != 0){
                printf("%d\n", deque[front-1]);front--;}
            else{
                printf("%d\n", -1);}
        }
        
        else if(strcmp(input,"pop_back")==0){
            if((front-back-1) != 0){
                printf("%d\n", deque[back+1]);back++;}
            else{
                printf("%d\n", -1);}
        }
        
        else if(strcmp(input,"size")==0){
            printf("%d\n", (front-back-1));}
        
        else if(strcmp(input,"empty")==0){
            if((front-back-1)==0){
                printf("%d\n", 1);}
            else{
                printf("%d\n", 0);}
        }
        
        else if(strcmp(input,"front")==0){
            if((front-back-1) != 0){
                printf("%d\n", deque[front-1]);}
            else{
                printf("%d\n", -1);}
        }
        
        else if(strcmp(input,"back")==0){
            if((front-back-1) != 0){
                printf("%d\n", deque[back+1]);}
            else{
                printf("%d\n", -1);}
        }
    }
    
    return 0;
}
```