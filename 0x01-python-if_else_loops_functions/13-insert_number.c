#include "lists.h"

/**
  *insert_node - adds a node to an ordered list
  *@head: the first node
  *@number: the value of the node to be added
  *
  *Return: returns the new node's address
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *temp;
	listint_t *new;

	new = malloc(sizeof(listint_t) * 1);

	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	current = *head;

	if (current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current)
	{

		if (current->n > number)
			break;
		temp = current;
		current = current->next;
	}

	temp->next = new;
	new->next = current;

	return (new);
}
