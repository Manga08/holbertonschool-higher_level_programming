#include "lists.h"
/**
 * is_palindrome - Funtion that checks if a singly linked list is a palindrome
 * @head: Head
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	int ct1, ct2, buff[4096];
	listint_t *temp;

	if (!head)
		return (0);
	temp = *head;
	if (!*head || (*head)->next == NULL)
		return (1);

	for (ct1 = 0; temp; temp = temp->next, ct1++)
		buff[ct1] = temp->n;
	for (ct2 = 0, ct1--; ct1 > ct2; ct1--, ct2++)
	{
		if (buff[ct2] == buff[ct1])
			;
		else
			return (0);
	}
	return (1);
}
