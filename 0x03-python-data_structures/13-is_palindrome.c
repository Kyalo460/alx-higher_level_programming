#include "lists.h"

/**
  *is_palindrome - checks if a list is a palindrome
  *@head: the first node
  *
  *Return: Returns 1 if palindrome 0 if not
  */
int is_palindrome(listint_t **head)
{
	listint_t *head2 = NULL;
	listint_t *current = *head;
	listint_t *new;

	/*Make a new list that is the reversed version of the old list*/
	while (current)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (1);

		new->n = current->n;
		new->next = head2;
		head2 = new;
		current = current->next;
	}

	current = *head;
	new = head2;
	/*Compare if both lists are the same*/
	while (current != NULL)
	{
		if (current->n != new->n)
		{
			free_listint(head2);
			return (0);
		}
		current = current->next;
		new = new->next;
	}

	if (new != NULL || current != NULL)
	{
		free_listint(head2);
		return (0);
	}
	free_listint(head2);

	return (1);
}
