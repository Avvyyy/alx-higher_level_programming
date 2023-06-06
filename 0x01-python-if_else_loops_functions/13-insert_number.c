#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Function to insert a number to a sorted singly linked list
 * @head: Head node of the list
 * @number: Number to be inserted in the list
 *
 * Return: Address of new node else NULL
 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
	}
	
	current = *head;
	
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	new->next=current->next;
	current->next = new;

	return (new);
}
