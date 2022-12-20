#include "lists.h"

listint_t *reverse_half(listint_t *head);
void r_reverse(listint_t *tail);
listint_t *fetch_node(listint_t *head, size_t idx);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 0 if list is not a palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	size_t len = 0;
	listint_t *h = *head, *t;
	listint_t *current = *head, *node;

	if (h == NULL || h->next == NULL)
		return (1);

	while (current != NULL)
	{
		len++;
		current = current->next;
	}

	len = (len - 1) / 2;
	node = fetch_node(h, len);
	t = reverse_half(node);
	while (t != NULL)
	{
		if (h->n != t->n)
		{
			r_reverse(t);
			return (0);
		}

		t = t->next;
		h = h->next;
	}

	r_reverse(t);
	return (1);
}

/**
 * reverse_half - reverses the second half of the given singly linked list
 * @head: pointer to the beginning of the second half of the list
 *
 * Return: the reversed list
 */
listint_t *reverse_half(listint_t *head)
{
	listint_t *prev = NULL, *next = head, *current = head->next;

	while (next != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		if (next != NULL)
			current = next;
	}

	return (current);
}

/**
 * r_reverse - rereverses a reversed list
 * @tail: pointer to the tail of the list
 *
 */
void r_reverse(listint_t *tail)
{
	listint_t *prev = NULL, *next = tail, *current = tail;

	while (next != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
}

/**
 * fetch_node - fetches the node corresponding to a given index
 * @head: pointer to the head of the list
 * @idx: the given index
 *
 * Return: pointer to the node
 */
listint_t *fetch_node(listint_t *head, size_t idx)
{
	size_t i = 0;
	listint_t *current = head;

	while (i < idx)
	{
		current = current->next;
		i++;
	}

	return (current);
}
