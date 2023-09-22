#include "sort.h"

/**
 * insertion_sort_list - sorts a doubly linked list with insertion sort algori
 * @list: a double pointer to the list to sort
 */
void insertion_sort_list(listint_t **list)
{
	listint_t *head, *unsorted, *hole;
	int holder;

	if (list == NULL)
		return;

	if ((*list) == NULL || (*list)->next == NULL)
		return;

	head = *list;
	unsorted = (*list)->next;
	while (unsorted->next != NULL)
	{
		holder = unsorted->n;
		hole = unsorted;
		while (hole->prev != NULL && hole->prev->n > holder)
		{
			hole->n = hole->prev->n;
			hole = hole->prev;
		}
		hole->n = holder;
		unsorted = unsorted->next;
	}
	(*list) = head;
