/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atol.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/31 17:00:09 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/01/04 17:02:12 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

int	valid_number(char *str)
{
	int	i;

	i = 0;
	if (!str)
		return (0);
	if (!str[i])
		return (0);
	if (str[i] == '+' || str[i] == '-')
		i++;
	if (!str[i])
		return (0);
	while (str[i])
	{
		if (str[i] < '0' || str[i] > '9')
			return (0);
		i++;
	}
	return (1);
}

int	valid_array(char **array)
{
	int	i;

	i = 0;
	while (array[i])
	{
		if (!valid_number(array[i]))
			return (0);
		i++;
	}
	return (1);
}

void	check_duplicates(t_number *stack)
{
	t_number	*current_node;
	t_number	*stack_copy;

	if (!stack)
		return ;
	if (!stack->next)
		return ;
	current_node = stack;
	stack_copy = current_node->next;
	while (current_node)
	{
		while (stack_copy)
		{
			if (current_node->num == stack_copy->num)
				ft_error(NULL, stack);
			stack_copy = stack_copy->next;
		}
		current_node = current_node->next;
		if (!current_node)
			stack_copy = NULL;
		else
			stack_copy = current_node->next;
	}
}

long	ft_atol(char *n)
{
	long	result;
	int		sign;

	result = 0;
	sign = 1;
	if (*n == '+' || *n == '-')
	{
		if (*n == '-')
			sign = -1;
		n++;
	}
	while (*n)
	{
		result = result * 10 + (*n - '0');
		if ((sign == 1 && result > INT_MAX)
			|| (sign == -1 && (-result) < INT_MIN))
			return (LONG_MAX);
		n++;
	}
	return (result * sign);
}
