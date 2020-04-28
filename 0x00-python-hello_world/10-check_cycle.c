#include "lists.h"
/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: The struct.
 * Return: 0 or 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *checks = list, *temp = list;

	while (checks != NULL && temp != NULL && checks->next != NULL)
	{
		checks = checks->next->next;
		temp = temp->next;
		if (checks == temp)
			return (1);
	}
	return (0);
}
