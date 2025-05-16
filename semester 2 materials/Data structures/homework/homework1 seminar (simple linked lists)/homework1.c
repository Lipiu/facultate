#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CARD_ARRAYS_LENGHTS 20
#define CARD_NUMBER_LENGHT 16
#define EXPIRING_DATE_FORMAT_LENGHT 5 // MM/YY

//defining the structures
struct BankCard{
	char* holder; // 4 bytes
	char card_no[CARD_NUMBER_LENGHT+1]; //+ 1 null terminator byte ; 17 bytes +3
	float balance;// 4 bytes
	char exp_date[EXPIRING_DATE_FORMAT_LENGHT + 1]; //+1 for null terminator ; 6 bytes +2 
	char* currency; //4 
};
typedef struct BankCard BankCard;
//-------------------------------
struct Node{
    BankCard data;
    struct Node* next;
};
typedef struct Node Node;
//-------------------------------
struct LinkedList{
    struct Node* head;
    int size;
};
typedef struct LinkedList LinkedList;
//-------------------------------

//method to parse and print the list
void parse(LinkedList* list)
{
	Node* temp = list->head;
	while (temp != NULL)
	{
		printf("%s %s\n", temp->data.holder, temp->data.card_no);

		temp = temp->next; // update temp with the next node in the chain
	}
}

//method to insert a node into simple list
Node* insertNode(LinkedList* list, BankCard bc){

    Node* newNode = malloc(sizeof(Node));
    newNode->data = bc;
    newNode->next = NULL;

    if(list->head == NULL){
        //list contains at least one node
        list->head = newNode;
    }
    else{
        Node* temp = list->head;
        while(temp->next != NULL){
            temp = temp->next;
        }
        temp->next = newNode;
    }
    list->size++;
    return list->head;
}

//method to insert node in the middle of the simple list
Node* insertMiddle(LinkedList* list, BankCard bc){
    Node* middleNode = (Node*)malloc(sizeof(Node));
    middleNode->data = bc;
    middleNode->next = NULL;
    
    //if list is empty
    if(list->head == NULL){
        list->head = middleNode;
    }
    else{
        int midPos = list->size / 2;

        if(midPos == 0){
            middleNode->next = list->head;
            list->head = middleNode;
            list->size++;
            return list->head;
        }

        Node* temp = list->head;
        for(int i = 0; i < midPos - 1; i++){
            temp = temp->next;
        }
        middleNode->next = temp->next;
        temp->next = middleNode;
    }
    list->size++;
    return list->head;
}

//method to delete beginning node
Node* deleteBeginningNode(LinkedList* list){
    Node* temp = list->head;

    //empty list
    if(temp == NULL){
        printf("Empty list!\n");
        return;
    }
    //head of list is the node to be deleted
    else{
        Node* temp = list->head;
        list->head = list->head->next;
        free(temp);
        list->size--;
    }   
}

Node* deleteEndNode(LinkedList* list){
    Node* temp = list->head;

    //empty list case
    if(list->head == NULL){
        printf("Empty list!\n");
        return list;
    }

    //only one node
    if(list->head->next == NULL){
        free(list->head);
        list->head = NULL;
    }
    else{
        while(temp->next != NULL && temp->next->next != NULL){
            temp = temp->next;
        }
        Node* lastNode = temp->next;
        temp->next = NULL;
        free(lastNode);   
    }
    list->size--;
    return list;
}

int main() {
	FILE* f = fopen("CardData.txt","r"); //relative path

    LinkedList* list;
    list->head = NULL;
    list->size = 0;

	unsigned char buffer[200];
	while (fgets(buffer, sizeof(buffer), f)) {

        BankCard card;
		char seps[] = ",\n";
		char* token = strtok(buffer, seps);
		strcpy(card.card_no, token);
		token = strtok(NULL, seps);

	    strcpy(card.exp_date, token);
		token = strtok(NULL, seps);

		card.holder = malloc(strlen(token) + 1);
		strcpy(card.holder, token);

		token = strtok(NULL, seps);
		card.currency = malloc(strlen(token) + 1);
		strcpy(card.currency, token);

		token = strtok(NULL, seps);
		card.balance = (float) atof(token);
        
        //insert card data into a simple list
        insertNode(list, card);
    }


	fclose(f);

    //testing
    printf("Simple list after creation:\n");
	parse(list);

    printf("\nSimple list after inserting node in middle:\n");

    //defining the new node to be inserted in the middle
    BankCard newBankCard;
    newBankCard.holder = "Middle holder";
    newBankCard.balance = 0;
    strcpy(newBankCard.card_no, "6523999900001232");
    newBankCard.currency = "RON";
    strcpy(newBankCard.exp_date, "No expire date");

    insertMiddle(list, newBankCard);
    parse(list);

    printf("\nList after deleting first node:\n");
    deleteBeginningNode(list);
    parse(list);

    printf("\nList after deleting last node:\n");
    deleteEndNode(list);
    parse(list);


	return 0;
}