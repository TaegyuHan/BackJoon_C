# 10757 큰 수 A+B

URL : [https://www.acmicpc.net/problem/10757](https://www.acmicpc.net/problem/10757)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>
char InputNumberA[10001];
char InputNumberB[10001];
char Result[10002];
char NextNum=0;

int charToNum(char num)
{
    int result;

    result = (num<48) ? 0 : num-48;

    return result;
}

int strlen(char arry[])
{
    int i;
    int result=0;

    for(i=0; arry[i]!='\0'; i++)
        result++;

    return result;
}

int main()
{
    int i;
    int lenA, lenB;
    char numA, numB, Num;
    int Loop;

    scanf("%s", InputNumberA);
    scanf("%s", InputNumberB);

    lenA = strlen(InputNumberA);
    lenB = strlen(InputNumberB);
    Loop = (lenA > lenB) ?  lenA : lenB;

    for(i=0; i<Loop; i++)
    {
        numA = charToNum(InputNumberA[--lenA]);
        numB = charToNum(InputNumberB[--lenB]);

        // printf("%d %d %d\n", numA, numB, NextNum);

        Num = (numA + numB + NextNum)%10;
        NextNum = (numA + numB + NextNum)/10;

        Result[i] = Num;
        Result[i+1] = NextNum;

        // printf("%d %d %d %d\n", numA, numB, Result[i], Result[i+1]);
        // printf("%d %d\n", NextNum, Num);
    }

    if(Result[Loop]==0)
    {
        for(i=Loop-1; i>=0; i--)
        {
            printf("%d", Result[i]);
        }
    }
    else 
    {
        for(i=Loop; i>=0; i--)
        {
            printf("%d", Result[i]);
        }
    }

  return 0;

}
```

숏 코딩

```c
#include <stdio.h>
#include <string.h>
int main() {
    int max, val, carry;
    int i, ml, nl;
    char mbuf[10001], nbuf[10001];
    int  m[10001]={0,};
    int  n[10001]={0,};
    int  s[10001]={0,};

    scanf("%s",mbuf);

    scanf("%s",nbuf);

    ml=strlen(mbuf);
    nl=strlen(nbuf);
    for(i=0;i<ml;i+=1) {
        m[ml-i-1]=mbuf[i]-48;
    }
    for(i=0;i<nl;i+=1) {
        n[nl-i-1]=nbuf[i]-48;
    }

    max=ml;
    if(nl>ml) max=nl;

    carry=0;
    for(i=0;i<max;i+=1) {
        val=m[i]+n[i]+carry;
        carry=val/10;
        s[i]=val%10;
    }
    if(carry>0) {
        s[max]=carry;
        max+=1;
    }

    for(i=0;i<max;i+=1) {
        printf("%d",s[max-i-1]);
    }

    return 0;
}
```

```c
#include <stdio.h>
#include <string.h>

void reverse(char arr[]);

int main() 
{
	char A[10002] = { 0 }, B[10002] = { 0 }, res[10003] = { 0 };
	int carry = 0, i;
	
	scanf("%s%s", A, B);
	
	reverse(A);
	
	reverse(B);
	
	int len = strlen(A) > strlen(B) ? strlen(A) : strlen(B);
	
	for (i = 0; i < len; i++) 
	{
		int sum = A[i] - '0' + B[i] - '0' + carry;
		while (sum < 0) sum += '0';
		if (sum > 9) 
			carry = 1; 
		else 
			carry = 0;
		res[i] = sum % 10 + '0'; 
	}
	if (carry == 1) 
		res[len] = '1'; 
	reverse(res);
	
	printf("%s", res);
	
	return 0;
}

void reverse(char arr[])
{
	int len = strlen(arr);
	for (int i = 0; i < len / 2; i++)
	{
		char temp = arr[i];
		arr[i] = arr[len - i - 1];
		arr[len - i - 1] = temp;
	}
}
```

```c
#include <stdio.h>

int N;
char arr1[10005], arr2[10005];
int ans[12000];

int main(void)

{
	int i, j, k;
	int sv = 0;
	int idx = 0;

	int fn, bn;
	int flag = 0;
	scanf("\n%s", arr1);
	scanf("\n%s", arr2);

	i = 0, j = 0;
	while (arr1[i] != '\0'){
		++i;
	}
	while (arr2[j] != '\0'){
		++j;
	}

	while (i >= 0 || j >= 0){
		if (i != -1){
			--i;
		}
		if (j != -1){
			--j;
		}

		if (i == -1){
			fn = 0;
		}
		else{
			fn = arr1[i] - '0';
		}
		if (j == -1){
			bn = 0;
		}
		else{
			bn = arr2[j] - '0';
		}

		ans[++idx] = (fn + bn + sv) % 10;
		if (fn + bn + sv >= 10){
			sv = 1;
		}
		else{
			sv = 0;
		}
	}

	for (i = idx; i >= 1; --i){
		if (ans[i] != 0){
			flag = 1;
		}
		if (flag == 1){
			printf("%d", ans[i]);
		}
	}
	return 0;
}
```