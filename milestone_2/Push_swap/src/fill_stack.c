/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fill_stack.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/03 22:00:53 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/01/18 11:46:42 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

void	fill_stack_b_init(int *chunks_number, int *size,
						int *pushed, t_number **stack_a)
{
	*chunks_number = 2;
	*pushed = 0;
	*size = stack_size(*stack_a);
	if (*size < 10)
		*chunks_number = 1;
	else if (*size > 100)
		*chunks_number = 12;
	else
		*chunks_number = 5;
}

void	fill_stack_b(t_number **stack_a, t_number **stack_b)
{
	int	chunks_number;
	int	size;
	int	pushed;
	int	current_chunk;

	current_chunk = 1;
	fill_stack_b_init(&chunks_number, &size, &pushed, stack_a);
	while (*stack_a)
	{
		if ((*stack_a)->order < current_chunk * (size / chunks_number))
		{
			pb(stack_a, stack_b);
			pushed++;
		}
		else
			ra(stack_a);
		if (pushed == (current_chunk * (size / chunks_number)))
			current_chunk++;
	}
}

int	max_on_top(t_number **stack, int max)
{
	int			size;
	int			index;
	t_number	*current_node;

	index = 0;
	size = stack_size(*stack);
	current_node = *stack;
	while (current_node)
	{
		if (current_node->order == max)
			return (index < size / 2);
		index++;
		current_node = current_node->next;
	}
	return (0);
}

void	fill_stack_a(t_number **stack_a, t_number **stack_b)
{
	int	current_order;
	int	size;

	size = stack_size(*stack_b);
	current_order = size - 1;
	while (current_order >= 0)
	{
		if (max_on_top(stack_b, current_order))
		{
			while ((*stack_b)->order != current_order)
				rb(stack_b);
		}
		else
		{
			while ((*stack_b)->order != current_order)
				rrb(stack_b);
		}
		pa(stack_a, stack_b);
		current_order--;
	}
}
