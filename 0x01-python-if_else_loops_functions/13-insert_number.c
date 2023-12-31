#include "lists.h"

/**
 * This inserts node - Inserts a number into a sorted singly-linked list.
 * @head: This is a pointer the head of the linked list.
 * @number: This is the number to insert.
 *
 * Return: This will return null If the function fails
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}

