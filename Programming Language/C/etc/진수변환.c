#include <stdio.h>

#define SIZE 32

int From, To = 0;
char From_num[16] = {0};

int to_demical(void);
int ctoi(char ch);
char itoc(int value);
int repeat(int square);
void convert_to(int decimal_value);

int main(void) {
	printf("원래 진수와 변환할 진수를 순서대로 공백을 두고 입력하세요.\n");
	scanf("%d %d", &From, &To);
	
	printf("원래 진수의 값을 입력하세요.\n");
	scanf("%s", From_num);
	
	convert_to(to_decimal());
}

int to_decimal() {
	int i;
	int index_max = 0, decimal_value = 0;
	
	// Get From_num's length
	for(i = 0; From_num[i]; i++)
        index_max++;
    
    for (i = 0; From_num[i]; i++)
    	decimal_value += ctoi(From_num[i]) * repeat((index_max - 1) - i);
    
    return decimal_value;
}

int ctoi(char ch) {
    if(ch >= '0' && ch <= '9')
        return (ch - '0');
    else if (ch >= 'a' && ch <= 'z')
        return (10 + ch - 'a');
	else if (ch >= 'A' && ch <= 'Z')
		return (10 + ch - 'A');
    else
        return 1;
}

char itoc(int value) {
	if (value >= 0 && value <= 9)
		return (value + '0');
	else {
		return 'a' + (value - 10);
	}
}

int repeat(int square) {
    int i;
	int tmp = 1;
     
    if(square == 0)
        return 1;
    for(i = 0; i < square; i++)
        tmp *= From;
    return tmp;
}

void convert_to(int decimal_value) {
	int i;
	int value = decimal_value;
	char converted_value[SIZE] = {0};
	char result[SIZE] = {0};
	
	while (value != 0) {
		converted_value[SIZE - 1 - i] = itoc(value % To);
		value /= To;
		i++;
	}
	
	for (i = 0; i < SIZE; i++)
		if (converted_value[i] != '\0')
			printf("%c", converted_value[i]);
}
