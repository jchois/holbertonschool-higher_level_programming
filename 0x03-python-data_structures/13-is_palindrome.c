#include "lists.h"
/**
 * is_palindrome - check if is a palindrome
 * @head: pointer to head of the list
 * Return: 1 if a palindrome 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (1);
	return (check_palindrome(head, *head));
}
/**
 * check_palindrome - check if palindrome with recursion
 * @left_ptr: Pointer to left side of the list
 * @right_ptr: Pointer to right side of the list
 * Return: 1 if a palindrome 0 otherwise
 */
int check_palindrome(listint_t **left_ptr, listint_t *right_ptr)
{
	if (!right_ptr)
		return (1);
	if (check_palindrome(left_ptr, right_ptr->next)
			&& ((*left_ptr)->n == right_ptr->n))
	{
		(*left_ptr) = (*left_ptr)->next;
		return (1);
	}
	return (0);
}
