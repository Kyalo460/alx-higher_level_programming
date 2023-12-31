#include "lists.h"

/**
  *check_cycle - checks if a linked lists has a loop
  *@list: the first node
  *
  *Return: 0 if there is no loop 1 if there is one
  */
int check_cycle(listint_t *list)
{
	int i = 0;
	listint_t *current;

	if (list == NULL)
		return (0);

	current = list;

	while (current && list->next != NULL)
	{
		if (current->next == list)
			return (1);
		current = current->next;

		if (i > 100)
			return (1);
		i++;
	}

	return (0);
}
