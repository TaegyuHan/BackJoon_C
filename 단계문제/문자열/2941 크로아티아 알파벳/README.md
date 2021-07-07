# 2941 크로아티아 알파벳

URL : [https://www.acmicpc.net/problem/2941](https://www.acmicpc.net/problem/2941)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    char string[101]; // 문자열 저장 배열
    char i;
    char ResultSum=0; // 결과 저장

    scanf("%s", string);

    // 문자열 확인
    for(i=0; string[i]!=NULL; i++)
    {
        ResultSum++;
        if(string[i]=='=' && string[i-1]=='c') // c=
            ResultSum -= 1;
        else if(string[i]=='-' && string[i-1]=='c') // c-
            ResultSum -= 1;
        else if(string[i]=='=' && string[i-1]=='z' && string[i-2]=='d') // dz=
            ResultSum -= 2;
        else if(string[i]=='-' && string[i-1]=='d') // d-
            ResultSum -= 1;
        else if(string[i]=='j' && string[i-1]=='l') // lj
            ResultSum -= 1;
        else if(string[i]=='j' && string[i-1]=='n') // nj
            ResultSum -= 1;
        else if(string[i]=='=' && string[i-1]=='s') // s=
            ResultSum -= 1;
        else if(string[i]=='=' && string[i-1]=='z') // z=
            ResultSum -= 1;
    }

    printf("%d", ResultSum);

    return 0;
}
```

<br>

숏 코딩

```c
int main() {

	char s[101];
	int i, result = 0;

	scanf("%s", s);

	for (i = 0; i < strlen(s); i++) {
		if (97 <= s[i] && s[i] <= 122) {
			if (s[i] == 'j' && (s[i - 1] == 'l' || s[i - 1] == 'n'))
				continue;
			else if (s[i] == 'z' && s[i - 1] == 'd' && s[i+1] == '=')
				continue;
			else result += 1;
		}
	}
	printf("%d", result);
	return 0;
}
```

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
	char str[100];
	int len, cnt;

	scanf("%s", str);
	len = strlen(str);
	cnt = len;

	for (int i = 0; i < len; i++) {
		if ((str[i] == 'n' || str[i] == 'l') && str[i + 1] == 'j')
			cnt--;
		if (str[i] == '=' || str[i] == '-')
			cnt--;
		if (str[i] == 'd'&&str[i + 1] == 'z' && str[i + 2] == '=')
			cnt--;
	}

	printf("%d", cnt);
}
```

```c
#include <stdio.h>
#include <string.h>

int count(char *str, char *cmp){
	int cnt=0;
	char *ptr = strstr(str, cmp);
	
	while(ptr!=NULL){
		ptr = strstr(ptr+1, cmp);
		cnt ++;
	}
	return cnt;
}

int main(){ 
	char str[100]={0};
	scanf("%s", str);
	int len = strlen(str);
	
	len -=count(str, "=");
	len -=count(str, "-");
	len -=count(str, "dz=");
	len -=count(str, "lj");
	len -=count(str, "nj");
	
	printf("%d", len);
	
	return 0;
}
```