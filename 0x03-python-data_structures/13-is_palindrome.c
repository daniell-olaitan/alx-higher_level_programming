#include "lists.h"

listint_t *reverse_list(listint_t *head);
listint_t *add_node(listint_t *head, int data);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 0 if list is not a palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *h = *head, *t;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	t = reverse_list(*head);
	while (h != NULL)
	{
		if (h->n != t->n)
			return (0);

		t = t->next;
		h = h->next;
	}

	return (1);
}

/**
 * reverse_list - reverses a given singly linked list
 * @head: pointer to the head of the list
 *
 * Return: the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *h = NULL, *current = head;

	while (current != NULL)
	{
		h = add_node(h, current->n);
		current = current->next;
	}

	return (h);
}

/**
 * add_node - adds a node as the head of a list
 * @head: the head of the list
 * @data: the data of the node
 *
 * Return: pointer to the head of the list
 */
listint_t *add_node(listint_t *head, int data)
{
	listint_t h;

	h.n = data;
	h.next = head;

	return (&h);
}
