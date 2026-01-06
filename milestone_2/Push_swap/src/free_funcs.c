/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   free_funcs.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/03 13:48:31 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/01/06 13:01:17 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

void	free_array(char **array)
{
	int	i;

	if (!array)
		return ;
	i = 0;
	while (array[i])
	{
		free(array[i]);
		i++;
	}
	free(array);
}

void	free_int_array(int *array, int size)
{
	int	i;

	if (!array)
		return ;
	i = 0;
	while (i < size)
	{
		free(&array[i]);
		i++;
	}
	free(array);
}

void	free_stack(t_number *stack)
{
	t_number	*tmp;

	while (stack)
	{
		tmp = stack->next;
		free(stack);
		stack = tmp;
	}
}

void	ft_error(char **array, t_number *stack)
{
	if (array)
		free_array(array);
	if (stack)
		free_stack(stack);
	write(2, "Error\n", 6);
	exit(EXIT_FAILURE);
}
