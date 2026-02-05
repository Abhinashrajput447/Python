#include <stdio.h>
#include <stdlib.h>

struct Node {
  int data;
  struct Node* next;
}*head = NULL, *newNode;

void create() {
  struct Node* newNode;
  newNode = (struct Node*)malloc(sizeof(struct Node));

  int val;
  printf("Enter value for LL creation : ");
  scanf("%d", &val);
  newNode -> data = val;
  newNode -> next = NULL;

  if(head == NULL) {
    head = newNode;
  }
}

void insert_beg() {
  struct Node* newNode;
  newNode = (struct Node*)malloc(sizeof(struct Node));

  int val;
  printf("Enter value : ");
  scanf("%d", &val);

  newNode -> data = val;
  newNode -> next = NULL;

  if(head == NULL) {
    printf("LL is Empty\n");
    return;
  }else{
    newNode -> next = head;
    head = newNode;
  }
}

void display() {
  struct Node* temp = head;
  
  while(temp != NULL) {
    printf("%d --> ", temp -> data);
    temp = temp->next;
  }
}

void insert_end() {
  // struct Node* temp = head;
  struct Node* newNode, *temp = head;
  newNode = (struct Node*)malloc(sizeof(struct Node*));

  int val;
  printf("Enter value for LL creation from End : ");
  scanf("%d", &val);
  newNode -> data = val;
  newNode -> next = NULL;

  if(head == NULL) {
    printf("LL is Empty\n");
    return;
  }else{
    while(temp-> next != NULL) {
      temp=temp->next;
    }
    temp -> next = newNode;
    newNode -> next = NULL;
  }

}

void delete() {
  struct Node* t = head;
  int pos, cnt = 1;
  printf("Enter pos for deletion : ");
  scanf("%d", &pos);
  while(cnt != pos-1) {
    cnt++;
    t = t -> next;
  }
  t-> next = t->next->next;
}


int main() {
  create();
  insert_end();
  insert_end();
  insert_end();
  insert_end();
  delete();
  display();
  return 0;
}