#include "lists.h"

/**
 * check_cycle - this checks if a linked list contains a cycle
 * @list: this is the linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *fst = list;
	listint_t *scd = list;

	if (list == NULL)
		return(0);
	while (scd != NULL && scd->next != NULL && fst != NULL)
	{
		fst = fst->next;
		scd = scd->next->next;

		if (fst == scd)
			return (1);
	}
	return (0);
}
