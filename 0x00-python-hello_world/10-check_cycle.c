#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: the given list
 *
 * Return: 0 if there is no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL)
		return (0);
	else if (list->next == NULL)
		return (0);

	tortoise = list->next;
	hare = (list->next)->next;
	while (hare)
	{
		if (tortoise == hare)
			return (1);

		tortoise = tortoise->next;
		hare = hare->next;
		if (hare == NULL)
			break;

		hare = hare->next;
	}

	return (0);
}
