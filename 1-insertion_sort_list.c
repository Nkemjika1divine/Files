#include "sort.h"

/**
 * insertion_sort_list - sorts a doubly linked list with insertion sort algori
 * @list: a double pointer to the list to sort
 */
void insertion_sort_list(listint_t **list)
{
	listint_t *head, *sorted, *unsorted;
	int holder;

	if (list == NULL)
		return;

	if ((*list) == NULL || (*list)->next == NULL)
		return;

	head = *list;
	unsorted = (*list)->next;
	sorted = *list;
	while (unsorted->next != NULL)
	{
		holder = unsorted->n;
		while (sorted->prev != NULL && sorted->n > holder)
		{
			unsorted->n = sorted->n;
			sorted = sorted->prev;
		}
		sorted->n = holder;
		sorted = unsorted->next;
		unsorted = unsorted->next;
	}
	(*list) = head;
