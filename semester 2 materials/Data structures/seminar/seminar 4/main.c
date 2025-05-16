#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <malloc.h>
#include <stdlib.h>

struct bankCard {
	int age;
	char *holder;
	char* id;
};
typedef struct bankCard bankCard;

struct Nod {

	bankCard data;
	struct Nod* next;
};
typedef struct Nod Nod;

//method to parse and print the list
void parseList(Nod* list) {
	Nod* temp = list;
	while (temp != NULL) {
		printf("Name: %s\nID: %s\n", temp->data.holder, temp->data.id);
		temp = temp->next;
	}

}

Nod* insertBeggining(Nod* list, bankCard bc) {

	Nod* newNode = malloc(sizeof(Nod));
	newNode->data = bc;
	if (list) {

		newNode->next = list;
	}
	else {
		newNode->next = NULL;
	}
	return newNode;
}


Nod* insertEnd(Nod* list, bankCard bc) {

	Nod* t = list;
	Nod* newNode = malloc(sizeof(Nod));
	newNode->data = bc;
	newNode->next = NULL;

	if (t) {
		while (t->next!=NULL) {
			t = t->next;
		}
		t->next = newNode;
		return list;
	}
	else {
		return newNode;
	}

}

Nod* insertMiddle(Nod* list, bankCard bc,int dim) {
	Nod* t = list;
	Nod* newNode = malloc(sizeof(Nod));
	newNode->data = bc;
	if (t == NULL) {
		newNode->next = NULL;
		return newNode;
	}
	else {
		for (unsigned int i = 0; i < dim / 2 -1 ; i++) {
			t = t->next;
		}
		newNode->next = t->next;
		t->next = newNode;
	}
	return list;

}


Nod* deleteBeggining(Nod* list) {

	Nod* temp = list;
	list = list->next;
	temp->next = NULL;
	free(temp->data.holder);
	free(temp->data.id);
	free(temp);
	return list;

}

Nod* deleteEnd(Nod* list) {

	Nod* t = list;
	while (t->next->next != NULL)
		t = t->next;

	Nod* temp = t->next;
	t->next = NULL;
	free(temp->data.holder);
	free(temp->data.id);
	free(temp);
	return list;
}



Nod* deleteById(Nod* list, char *id) {
	Nod* t = list;
	if (t != NULL) {
		Nod* temp = t;
		if (strcmp(t->data.id, id) == 0) {
			list = deleteBeggining(list);
		}
		else {
			while (strcmp(t->next->data.id, id) != 0 && t != NULL) {
				t = t->next;
			}
			temp = t->next;
			t->next = temp->next;
			free(temp->data.holder);
			free(temp->data.id);
			free(temp);
		}
	}
	return list;
}


int main() {
	FILE* f = fopen("data.txt", "r");

	Nod* head = NULL;
	char* buffer[200];
	bankCard card2;
	while (fgets(buffer, sizeof(buffer),f)) {
		bankCard card;


		char seps[] = ",\n";
		char *token = strtok(buffer, seps);
		
		card.holder = malloc(strlen(token) + 1);
		strcpy(card.holder, token);
		token= strtok(NULL, seps);
		card.id = malloc(strlen(token) + 1);
		strcpy(card.id, token);

		token = strtok(NULL, seps);
		card.age = (int)atoi(token);

		card2 = card;
		head = insertEnd(head, card);



	}
	//head = insertMiddle(head, card2, 4);
	parseList(head);
	printf("\nTESTARE::\n\n");
	//
	// head = deleteByName(head, "Rusu Mihnea");
	//head = deleteEnd(head);
	parseList(head);
	fclose(f);


}