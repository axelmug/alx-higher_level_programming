#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: list head
 * @number: number to store in the new node
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *x;
	listint_t *y;

	x = *head;

	y = malloc(sizeof(listint_t));
	if (y == NULL)
		return (NULL);
	y->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		y->next = *head;
		*head = y;
		return(y);
	}

	while(x->next != NULL)
	{
		if ((x->next)->n >= number)
		{
			y->next = x->next;
			x->next = y;
			return(y);
		}
		x = x->next;
	}

	y->next = NULL;
	x->next = y;
	return(y);
}