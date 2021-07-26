# 2875 대회 or 인턴

URL : [https://www.acmicpc.net/problem/2875](https://www.acmicpc.net/problem/2875)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct univ
{
    int W; // (0 ≤ M ≤ 100)
    int M; // (0 ≤ N ≤ 100)
    int Internship; // (0 ≤ K ≤ M+N)
} Univ;

void InputData(Univ * Univ)
{
    scanf("%d %d %d",
            &Univ->W,
            &Univ->M,
            &Univ->Internship );
    return;
}

void MaxTeam(Univ Univ)
{
    int teamCount;
    int W_Team, M_Team;
    int W_Remain, M_Remain;

    W_Team = Univ.W/2;
    M_Team = Univ.M;
    teamCount = (W_Team > M_Team) ? M_Team : W_Team;

    while(1)
    {

        W_Remain = Univ.W - (2*teamCount);
        M_Remain = Univ.M - teamCount;

        if(Univ.Internship - (W_Remain + M_Remain) <= 0) 
            break;

        teamCount--;
    }

    printf("%d", teamCount);

}

int main(void)
{
    Univ Univ;

    InputData(&Univ);
    MaxTeam(Univ);

    return 0;
}
```

숏 코딩

```c
int main(void)
{
	int girl, man; 
	int intern;
	int result = 0; 

	
	scanf("%d", &girl);
	scanf("%d", &man);
	scanf("%d", &intern);
	
	while (girl >= 2 && man >= 1 && girl + man >= intern + 3)
	{
		result = result + 1;
		girl = girl - 2; 
		man = man - 1; 
	}
	printf("%d\n", result);

	return 0;
}
```

```c
#include<stdio.h>

int N, M, K;

int maketeam() {
	if (M >= 1 && N >= 2) {
		M--;
		N = N - 2;
		return 1;
	}
	else
		return 0;
}

int main() {
	int count = 0;
	scanf("%d %d %d", &N, &M, &K);
	
	while (N+M-K>=3) {
		if (maketeam())
			count++;
		else
			break;
	}
	printf("%d", count);
	
	return 0;
}
```