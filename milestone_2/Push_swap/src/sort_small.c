/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_small.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/18 11:20:16 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/01/18 11:51:36 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

void	sort_3(t_number **a)
{
	int	x;
	int	y;
	int	z;

	x = (*a)->order;
	y = (*a)->next->order;
	z = (*a)->next->next->order;
	if (x > y && y < z && x < z)
		sa(a);
	else if (x > y && y > z)
	{
		sa(a);
		rra(a);
	}
	else if (x > y && y < z && x > z)
		ra(a);
	else if (x < y && y > z && x < z)
	{
		sa(a);
		ra(a);
	}
	else if (x < y && y > z && x > z)
		rra(a);
}

void	mini_fill_stack_a(t_number **stack_a, t_number **stack_b)
{
	sort_3(stack_a);
	while (*stack_b)
	{
		if ((*stack_b)->next)
		{
			if ((*stack_b)->num < (*stack_b)->next->num)
				rb(stack_b);
			else
				pa(stack_a, stack_b);
		}
		else
			pa(stack_a, stack_b);
	}
}

void	sort_small(t_number **stack_a, t_number **stack_b, int size)
{
	if (size == 2)
	{
		if ((*stack_a)->num > (*stack_a)->next->num)
			ra(stack_a);
		return ;
	}
	while (stack_size(*stack_a) > 3)
	{
		if ((*stack_a)->order < size - 3)
			pb(stack_a, stack_b);
		else
			ra(stack_a);
	}
	mini_fill_stack_a(stack_a, stack_b);
}
