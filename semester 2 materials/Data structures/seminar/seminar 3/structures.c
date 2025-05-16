#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

#define CARD_ARRAYS_LENGHTS 20
#define CARD_NUMBER_LENGHT 16
#define EXPIRING_DATE_FORMAT_LENGHT 5 // MM/Y
struct BankCard{
	char* holder; // 4 bytes
	char card_no[CARD_NUMBER_LENGHT+1]; //+ 1 null terminator byte ; 17 bytes +3
	float balance;// 4 bytes
	char exp_date[EXPIRING_DATE_FORMAT_LENGHT + 1]; //+1 for null terminator ; 6 bytes +2 
	char* currency; //4 
}; //35 bytes ? ->35 + 5 = 40 -> it has to be a multiple of 4
typedef struct BankCard BankCard;

int main() {

	BankCard v_card[CARD_ARRAYS_LENGHTS];
	BankCard* p_card = NULL;
	printf("Size of the structure BankCard is = %d bytes \n", sizeof(BankCard));
	printf("Size of the array v_card is = %d bytes \n", sizeof(v_card));
	printf("Size of the pointer p_card is = %d bytes \n", sizeof(p_card));

	FILE* f = fopen("CardData.txt","r"); //relative path

	unsigned char buffer[200];
	unsigned char count = 0;
	while (fgets(buffer, sizeof(buffer), f) &&count< CARD_ARRAYS_LENGHTS) {

		char seps[] = ",\n";
		char* token = strtok(buffer, seps);
		strcpy(v_card[count].card_no, token);
		token = strtok(NULL, seps);

		strcpy(v_card[count].exp_date, token);
		token = strtok(NULL, seps);

		v_card[count].holder = malloc(strlen(token) + 1);
		strcpy(v_card[count].holder, token);

		token = strtok(NULL, seps);
		v_card[count].currency = malloc(strlen(token) + 1);
		strcpy(v_card[count].currency, token);

		token = strtok(NULL, seps);
		v_card[count].balance =(float) atof(token);

			count += 1;//the next offset to be considered for the next line	
	}

	printf("\nCard data from the v_card array\n"); //printing v_card
	for (unsigned char i = 0; i < count; i++) {
		printf("%s %s \n", v_card[i].card_no, v_card[i].holder);


	}
	p_card = malloc(count * sizeof(BankCard));
	
	for (unsigned char i = 0; i < count; i++) {
		p_card[i] = v_card[i]; //v_card and p_card share the same heap mem areas for holder and currency
		//create separate heap memory locations for p_card
		p_card[i].holder = malloc(strlen(v_card[i].holder) + 1);
		strcpy(p_card[i].holder, v_card[i].holder);

		p_card[i].currency = malloc(strlen(v_card[i].currency) + 1);
		strcpy(p_card[i].currency, v_card[i].currency);
	}


	printf("\nCard data from the p_card array\n"); //printing p_card
	for (unsigned char i = 0; i < count; i++) {
		printf("%s %s \n", p_card[i].card_no, p_card[i].holder);


	}

	v_card[0].holder[0] = 'X'; //changing the first letter of the first name of the first holder in v_Card
	printf("Arrays after changing the holder's first letter of the first itme\n");

	printf("\nCard data from the v_card array after change\n"); //printing v_card
	for (unsigned char i = 0; i < count; i++) {
		printf("%s %s \n", v_card[i].card_no, v_card[i].holder);


	}
	printf("\nCard data from the p_card array after change\n"); //printing p_card
	for (unsigned char i = 0; i < count; i++) {
		printf("%s %s \n", p_card[i].card_no, p_card[i].holder);


	}

	//deallocations of arrays
	//v_card allocated on stack seg
	for (unsigned char i = 0; i < count; i++) {
		free(v_card[i].holder);
		free(v_card[i].currency);
	}


	//p_card is allocated on the heap segment
	//step 1: deallocate holder and currency
	for (unsigned char i = 0; i < count; i++) {

		free(p_card[i].holder);
		free(p_card[i].currency);
	}
	
	//step 2: deallocate the array of cards
	free(p_card);


	fclose(f);

	return 0;
}