# 10828 스택

URL : [https://www.acmicpc.net/problem/10828](https://www.acmicpc.net/problem/10828)

```c
#include <stdio.h>
int QueueArray[10001];

// 문자열 비교 함수
int strcmp(char str1[], const char str2[])
{
    int i;
    for(i=0; str2[i]!=NULL; i++)
    {
        if(str2[i]!=str1[i])
            return 0; // 같지 않으면 0
    }
    return 1; // 같으면 1
}

void push(int Array[], int * index, int InputNubmer)
{
    int TempIndex = * index;
    Array[TempIndex] = InputNubmer;

    // 배열에 1 추가
    *index = TempIndex + 1;
    return;
}

void pop(int Array[], int * index)
{
    int TempIndex = * index;

    if(TempIndex==0)
        printf("-1\n");
    else
    {
        printf("%d\n", Array[TempIndex-1]);
        Array[TempIndex-1] = 0;
        // 배열에 1 추가
        *index = TempIndex - 1;
    }
    return;
}

void size(int * index)
{
    int TempIndex = * index;
    printf("%d\n", TempIndex);
}

void empty(int * index)
{
    int TempIndex = * index;

    if(TempIndex==0)
        printf("1\n");
    else
        printf("0\n");
}

void top(int Array[], int * index)
{
    int TempIndex = * index;
    if(TempIndex==0)
        printf("-1\n");
    else
        printf("%d\n", Array[TempIndex-1]);
}

int main(void)
{
    int CommandNum; // (1 ≤ CommandNum ≤ 10,000)
    int InputNubmer; // (1 ≤ InputNubmer ≤ 100,000) 
    char InputCommandType[6];
    int index=0; // 배열 삽입 위치

    // 커맨드 입력 횟수
    scanf("%d", &CommandNum);

    while(CommandNum--)
    {
        scanf("%s", InputCommandType);

        if(strcmp(InputCommandType, "push"))
        {
            scanf("%d", &InputNubmer);
            push(QueueArray, &index, InputNubmer);
        }
        else if(strcmp(InputCommandType, "pop"))
        {
            pop(QueueArray, &index);
        }
        else if(strcmp(InputCommandType, "size"))
        {
            size(&index);
        }
        else if(strcmp(InputCommandType, "empty"))
        {
            empty(&index);
        }
        else if(strcmp(InputCommandType, "top"))
        {
            top(QueueArray, &index);
        }
    }
    return 0;
}
```

숏 코딩

```c
#include <stdio.h>
#include <string.h>

int stack[10000];
int top=-1;

void push(int n){
	stack[++top]=n;
}

void pop(){
	if(top==-1) printf("%d\n",-1);
	else printf("%d\n",stack[top--]);
}

void stack_Size(){
	printf("%d\n",top+1);
}

void is_Empty(){
	if(top==-1) printf("%d\n",1);
	else printf("%d\n",0);
}

int main() {
	int n,m,i;
	char s[6];
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%s",s);
		if(s[0]=='p'){
			if(s[1]=='u'){
				scanf("%d",&m);
				push(m);
			}
			else pop();
		}
		else if(s[0]=='s') stack_Size();
		else if(s[0]=='e') is_Empty();
		else printf("%d\n",m=(top==-1?-1:stack[top]));
	}
	return 0;
}
```

```c
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){

	int arr[10000];
	int T,i,idx=0,tmp;
	char str[10];
	
	arr[0]=-1;
	
	scanf("%d",&T);
	
	for(i=0; i<T; i++){
		
		scanf("%s",&str);
		
		if(!strcmp(str, "push")){
			scanf("%d",&tmp);
			idx++;
			arr[idx]=tmp;
		}
		else if(!strcmp(str, "pop")){
			if(idx==0){
				printf("-1\n");
			}
			else{	
				printf("%d\n",arr[idx]);
				idx--;
			}
		}
		else if(!strcmp(str, "top")){
			printf("%d\n",arr[idx]);
		}
		else if(!strcmp(str, "size")){
			printf("%d\n",idx);			
		}
		else if(!strcmp(str, "empty")){
			if(idx==0){
				printf("1\n");
			}
			else{
				printf("0\n");
			}
		}
	}
	
	return 0;
}
```

```c
#include <stdio.h>
#include <string.h>
int stack[10000];
int main() {
	int N, i, j, num, top=0;
	scanf("%d", &N);
	for(i=0; i<N; i++) {
		char cmd[BUFSIZ];
		scanf("%s", cmd);
		if(strcmp(cmd, "push") == 0) {
			scanf("%d", &num);
			stack[top] = num;
			top++;
		}
		if(strcmp(cmd, "pop") == 0) {
			if(top <= 0)
				printf("-1\n");
			else {
				printf("%d\n", stack[top-1]);
				top--;
			}
		}
		if(strcmp(cmd, "size") == 0) {
			printf("%d\n", top);
		}
		if(strcmp(cmd, "empty") == 0) {
			if(top <= 0)
				printf("1\n");
			else
				printf("0\n");

		}

		if(strcmp(cmd, "top") == 0) {
			if(top <= 0)
				printf("-1\n");
			else 
				printf("%d\n", stack[top-1]);
		}
	}
	return 0;
}
```