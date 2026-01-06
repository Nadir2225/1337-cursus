/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   indexing.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/03 16:24:34 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/01/06 13:01:43 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

int	*stack_to_array(t_number *stack, int size)
{
	int	*arr;
	int	i;

	arr = malloc(sizeof(int) * size);
	if (!arr)
		ft_error(NULL, stack);
	i = 0;
	while (stack)
	{
		arr[i] = stack->num;
		stack = stack->next;
		i++;
	}
	return (arr);
}

void	bubble_sort(int *arr, int size)
{
	int	tmp;
	int	i;
	int	j;
	int	k;

	k = 0;
	while (k < size - 1)
	{
		i = 0;
		j = 1;
		while (j < size - k)
		{
			if (arr[i] > arr[j])
			{
				tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
			i++;
			j++;
		}
		k++;
	}
}

void	assign_order(t_number *stack, int *sorted, int size)
{
	int	i;

	while (stack)
	{
		i = 0;
		while (i < size)
		{
			if (stack->num == sorted[i])
			{
				stack->order = i;
				break ;
			}
			i++;
		}
		stack = stack->next;
	}
}
