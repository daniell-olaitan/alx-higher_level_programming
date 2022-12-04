#include "lists.h"

size_t list_len(listint_t *head);
int *convert_to_array(listint_t *head, size_t len);
int is_palindrome_recursive(int *arr, size_t i, size_t j);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 0 if list is not a palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	int *int_array;
	size_t len = list_len(*head);
	if (len < 2)
		return (1);

	else
	{
		int_array = convert_to_array(*head, len);
		if (int_array == NULL)
			exit(1);

		return (is_palindrome_recursive(int_array));
	}
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
 * convert_to_array - converts a singly linked list to array
 * @head: pointer to the head of the list
 * @len: length of the list
 *
 * Return: pointer to the array
 */
int *convert_to_array(listint_t *head, size_t len)
{
	listint_t *current = head;
	int *int_arr;
	size_t idx = 0;

	int_arr = malloc(sizeof(int) * len);
	if (int_arr == NULL)
		return (NULL);

	while (current != NULL)
	{
		int_arr[idx] = current->n;
		idx++;
		current = current-next;
	}

	return (int_arr);
}

/**
 * is_palindrome_recursive - checks if an array is a palindrome
 * @arr: array of integer
 * @i:...
 * @j:...
 *
 * Return: 1 if palindrome, 0 if otherwise
 */
int is_palindrome_recursive(int *arr, size_t i, sie_t j)
{
	int l;

	l = j - i;
	if (l < 1)
		return (1);

	if ((arr[i] == arr[j]) && is_palindrome_recursive(arr, ++i, --j))
		return (1);

	return (0);
}
