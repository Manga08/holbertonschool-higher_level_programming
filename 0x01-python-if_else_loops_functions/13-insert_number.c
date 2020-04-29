#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: The head.
 * @number: The number.
 * Return: The new node.
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *next_ptr;
	listint_t *previous_ptr = NULL;
	listint_t *node;

	if (!head)
		return (NULL);
	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	if (!(*head))
	{
		node->next = NULL;
		*head = node;
		return (node);
	}
	if (number < (*head)->n)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	next_ptr = *head;
	while (next_ptr != NULL && next_ptr->n <= number)
	{
		previous_ptr = next_ptr;
		next_ptr = next_ptr->next;
	}
	node->next = next_ptr;
	previous_ptr->next = node;
	return (node);
}
