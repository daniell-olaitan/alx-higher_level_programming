#include "lists.h"

size_t list_len(listint_t *head);
int fetch_node(listint_t *head, size_t index);
int is_palindrome_r(listint_t *head, size_t h_idx, size_t t_idx);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 0 if list is not a palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	size_t len = list_len(*head);
	if (len < 2)
		return (1);

	return (is_palindrome_r(*head, 0, len - 1));
}

/**
 * list_len - computes the length of a singly linked list
 * @head: pointer to the head of the list
 *
 * Return: the length of the list
 */
size_t list_len(listint_t *head)
{
	size_t len = 0;
	listint_t *current = head;

	while (current != NULL)
	{
		len++;
		current = current->next;
	}

	return (len);
}

/**
 * fetch_node - fetches the data in the given index of a linked list
 * @head: pointer to the heado of the given list
 * @index: the index to be fetched
 *
 * Return: data fetched from the index
 */
int fetch_node(listint_t *head, size_t index)
{
	size_t idx = 0;

	while (idx < index)
	{
		head = head->next;
		idx++;
	}

	return (head->n);
}

/**
 * is_palindrome_r - checks if an array is a palindrome recursively
 * @head: the head node
 * @h_idx: head index
 * @t_idx: tail index
 *
 * Return: 1 if palindrome, 0 if otherwise
 */
int is_palindrome_r(listint_t *head, size_t h_idx, size_t t_idx)
{
	int a, b, l;

	l = t_idx - h_idx;
	if (l < 1)
		return (1);

	a = fetch_node(head, h_idx);
	b = fetch_node(head, t_idx);
	if ((a == b) && is_palindrome_r(head, ++h_idx, --t_idx))
		return (1);

	return (0);
}
