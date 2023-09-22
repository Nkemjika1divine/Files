#include "sort.h"

/**
 * bubble_sort - performs the sorting using bubble sort algorith
 * @array: the array of integers to sort
 * @size: size of the arrayif integers
 */
void bubble_sort(int *array, size_t size)
{
	size_t i, count, flag, iter;
	int holder;

	iter = 0;
	count = 1;
	while iter != (size - 1)
	{
		flag = 0;
		for (i = 0; i < (size - i - count); i++)
		{
			if (array[i] > array[i + 1])
			{
				flag = 1;
				holder = array[i];
				array[i] = array[i + 1];
				array[i + 1] = holder;
			}
		}
		count += 1;
		print_array(array, size);
		iter += 1;
		if (flag == 0)
			break;
	}
}
