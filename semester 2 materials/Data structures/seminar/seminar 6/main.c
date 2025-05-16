#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <malloc.h>
#include <stdlib.h>

#define CARD_NUMBER_LENGTH 16
#define EXPIRING_DATE_FORMAT_LENGTH 5 // MM/YY

struct BankCard
{
	char* holder;
	char card_no[CARD_NUMBER_LENGTH + 1];
	float balance;
	char exp_date[EXPIRING_DATE_FORMAT_LENGTH + 1];
	char* currency;
};

typedef struct BankCard BankCard;

struct NodeD
{
	BankCard data;
	// mem address of the next and previous items (nodes) in the chain
	struct NodeD* next; 
	struct NodeD* prev;
};

typedef struct NodeD NodeD;

struct DoubleList
{
	NodeD* head; 
	NodeD* tail;
};

typedef struct DoubleList DoubleList;

// insert a node into a double list (at the end)
DoubleList insert_node(DoubleList list, BankCard bc)
{
	NodeD* new_node = malloc(sizeof(NodeD));
	new_node->data = bc;
	new_node->next = NULL;
	new_node->prev = list.tail;

	if (list.head == NULL)
	{
		// the list is empty: list.head == list.tail == NULL
		list.head = new_node;
		list.tail = new_node;
	}
	else
	{
		// there is one node at least in double list
		list.tail->next = new_node;  // the tail becomes the node before the last one (new_node)
		list.tail = new_node;		 // update the tail of the lista after adding the new_node at the end
	}

	return list;
}

void parse_list(DoubleList list)
{
	NodeD* temp = list.head;
	printf("Double list head-to-tail:\n");
	while (temp != NULL)
	{
		printf("%s\n", temp->data.holder);
		temp = temp->next;
	}

	temp = list.tail;
	printf("\nDouble list tail-to-head;\n");
	while (temp != NULL)
	{
		printf("%s\n", temp->data.holder);
		temp = temp->prev;
	}
}

DoubleList deleteHolder(DoubleList list, char* holder)
{
    if(list.head != NULL){
        //there is one node at least in my double list
        NodeD* temp = list.head;
        
        while(temp != NULL){
            //the temp is not the node to be deleted
            NodeD* nextNode = temp->next;

			if(strcmp(temp->data.holder, holder) == 0){
				if(temp->prev != NULL)
					temp->prev->next = temp->next;
				else
					list.head = temp->next;
				if(temp->next != NULL)
					temp->next->prev = temp->prev;
				else
					list.tail = temp->prev;
				free(temp);
			}

			temp = nextNode;
        }

        if(temp != NULL){
            //the node to be deleted has been identified as temp
            if(temp == list.head){
                //head will be deleted
                list.head = list.head->next;
                if(list.head != NULL){
                    list.head->prev = NULL; // the second node becomes the new head of the double list
                }
                else{
                    list.tail = NULL; // double list becomes an empty list
                }
            }
            else{
                if(temp == list.tail){
                    list.tail = list.tail->prev; // update of tail with previous node
                    list.tail->next = NULL; // make the previous node as being the new tail of the list
                }
                else{
                    //temp is neither head nor tail
                    temp->prev->next = temp->next; //temp->prev is the node before the temp
                    temp->next->prev = temp->prev; //temp->next is the node right after the temp
                }
            }
            //deallocate the node temp
            free(temp->data.holder);
            free(temp->data.currency);
            free(temp);
        }
    }
    return list;
}

DoubleList delete_node_middle(DoubleList list, char* card_number)
{
    if(list.head != NULL){
        //there is one node at least in my double list
        NodeD* temp = list.head;
        
        while(temp != NULL && strcmp(temp->data.card_no, card_number) != 0){
            //the temp is not the node to be deleted
            temp = temp -> next;
        }

        if(temp != NULL){
            //the node to be deleted has been identified as temp
            if(temp == list.head){
                //head will be deleted
                list.head = list.head->next;
                if(list.head != NULL){
                    list.head->prev = NULL; // the second node becomes the new head of the double list
                }
                else{
                    list.tail = NULL; // double list becomes an empty list
                }
            }
            else{
                if(temp == list.tail){
                    list.tail = list.tail->prev; // update of tail with previous node
                    list.tail->next = NULL; // make the previous node as being the new tail of the list
                }
                else{
                    //temp is neither head nor tail
                    temp->prev->next = temp->next; //temp->prev is the node before the temp
                    temp->next->prev = temp->prev; //temp->next is the node right after the temp
                }
            }
            //deallocate the node temp
            free(temp->data.holder);
            free(temp->data.currency);
            free(temp);
        }

    }
    return list;
}


int main()
{
	FILE* f = fopen("CardData.txt", "r");
	DoubleList d_list;
	d_list.head = NULL;
	d_list.tail = NULL;

	unsigned char buffer[200];
	while (fgets(buffer, sizeof(buffer), f))
	{
		BankCard card;
		char seps[] = ",\n";
		char* token = strtok(buffer, seps); // splitting started from the beginning of buffer array
		strcpy(card.card_no, token);

		token = strtok(NULL, seps); // continue the splitting of buffer from the current point
		strcpy(card.exp_date, token);

		token = strtok(NULL, seps); // continue the splitting of buffer from the current point
		card.holder = malloc(strlen(token) + 1);
		strcpy(card.holder, token);

		token = strtok(NULL, seps); // continue the splitting of buffer from the current point
		card.currency = malloc(strlen(token) + 1);
		strcpy(card.currency, token);

		token = strtok(NULL, seps); // continue the splitting of buffer from the current point
		card.balance = (float)atof(token);

		// insert card data into a simple list
		d_list = insert_node(d_list, card);
	}

	fclose(f);

	printf("Initial double list after creation:\n");
	parse_list(d_list);

	d_list = deleteHolder(d_list, "Suto Mara");
	printf("\nDouble list after deletion of 'Rosu Liviu':\n");
	parse_list(d_list);

	// deallocate the entire list by calling the one single node deletion
	// for the card number taken from the head everytime
	while (d_list.head != NULL)
	{
		d_list = deleteHolder(d_list, d_list.head->data.holder);
	}
	printf("\nDouble list after deallocation:\n");
	parse_list(d_list);


    //delete all nodes based on holder name (same holder name) -> Done
    //swap 2 nodes in the double list by changing the prev and next pointers -> to do

	return 0;
}