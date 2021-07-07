# 1316 그룹 단어 체커

URL : [https://www.acmicpc.net/problem/1316](https://www.acmicpc.net/problem/1316)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    char i, j, k,
         tempStr,
         ResultSum = 0;
    char string[101];

    scanf("%d", &i);

    while(i--)
    {
        scanf("%s", string);
        // 첫번째로 도는 문자열
        for (j=0; string[j]!=NULL; j++)
        {
            tempStr = string[j];

            // 처음으로 같은문자가 안나오는 부분 찾기
            for (k=j+1; string[k]!=NULL; k++)
            {
                if(tempStr!=string[k])
                    break;
            }

            // 처음으로 같은문자가 안나오는 부분
            // 부터 같은 문자 나오는지 찾기
            for (k; string[k]!=NULL; k++)
            {
                if(tempStr==string[k])
                {
                    // 나오면 for문 나옴
                    tempStr = -1;
                    break;
                }
            }
            // 나오면 for문 나옴
            if (tempStr==-1)
                break;
        }
        // 나오면 for문 나옴
        if (tempStr==-1)
            continue;
        ResultSum++;
    }

    printf("%d", ResultSum);
    return 0;
}
```
<br>

숏 코딩

```c
#include <stdio.h>
int main()
{
	int n, i, index, 
			count=0;
	char word[101];
	int alpha[26]={0,};

	scanf("%d",&n);

	while(n-->0)
	{
		scanf("%s",word);

		for(i=0;word[i]!='\0';i++)
			if(word[i]!=word[i+1])
			{
				index=word[i]-'a';
				alpha[index]++;
				if(alpha[index]>1)
					break;
			}
		if(word[i]=='\0')count++;
		for(i=0;i<26;i++)
			alpha[i]=0;
	}
	printf("%d\n",count);
}
```

```c
#include <stdio.h>
int main() {
	int count =0,a;
	scanf("%d",&count);
	a=count;
	for(int i =0;i<a;i++){		
		char ch[101]={'\0'};	
		int alpha[26]={0};
		scanf("%s",ch);
		for(int j = 0;ch[j]!=NULL;j++){
			if(alpha[ch[j]-'a']==0){
				alpha[ch[j]-'a'] ++;
			}else if( ch[j]==ch[j-1]){
				alpha[ch[j]-'a'] ++;
			}else{
				count--;
				break;
			}

		}
	}
	printf("%d",count);
	return 0;
}
```

```c
#include <stdio.h>

int isGroup(char c[])
{
	char alpbt[26]={0,};
	alpbt[c[0]-97]=1;
	for(int tmp=1;c[tmp]!='\0';tmp++)
	{
		if(alpbt[c[tmp]-97]==1&&c[tmp]!=c[tmp-1]) 	return 0;
		if(alpbt[c[tmp]-97]<2) alpbt[c[tmp]-97]=1;
	}
	return 1;
}

int main()
{
	int casenum;
	int sum=0;
	
	scanf("%d",&casenum);
	for(;casenum>0;casenum--)
	{
		char tmp[100];
		scanf("%s",tmp);
		sum+=isGroup(tmp);
	}
	printf("%d",sum);
}
```