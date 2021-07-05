#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int CheckHan(short CheckNum);

int main(void)
{
  int InpNum, ResultNum = 0;
  short i;

  scanf("%d", &InpNum);

  for (i = 1; i <= InpNum; i++)
  { // 입력 받은 수 까지 첫번째 for문
    if (i < 100)
    { // 100 미만은 한수
      ResultNum += 1;
      continue;
    }
    // 한수 확인 함수 호출
    ResultNum += CheckHan(i);
  }
  // 결과 호출
  printf("%d", ResultNum);
  return 0;
}

int CheckHan(short CheckNum)
{
  // 숫자 배열
  char numberList[4] = {
      CheckNum / 1000,         // 1000의 자리
      (CheckNum % 1000) / 100, // 100의 자리
      (CheckNum % 100) / 10,   // 10의 자리
      CheckNum % 10            // 1의 자리
  };

  // 등차 수열 확인 변수
  unsigned char i;
  char tmp,
      num1, num2, num3;

  for (i = 0; i < 4; i++)
  { // 첫번째 자리수 확인
    if (numberList[i] != 0)
      break;
  }

  // 변수에 옮기기
  num1 = numberList[i];
  num2 = numberList[i + 1];
  num3 = numberList[i + 2];

  // 등차 계산
  tmp = num2 - num1;
  if (num2 + tmp == num3)
    return 1;

  return 0;
}