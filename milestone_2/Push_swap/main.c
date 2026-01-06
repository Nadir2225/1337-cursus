/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/03 16:08:50 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/01/06 13:28:11 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "include/push_swap.h"

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

void	sort_small(t_number **stack_a, t_number **stack_b, int size)
{
	while (stack_size(*stack_a) > 3)
	{
		if ((*stack_a)->order < size - 3)
			pb(stack_a, stack_b);
		else
			ra(stack_a);
	}
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

void	sort_stack(t_number **stack_a, t_number **stack_b, int a_size)
{
	if (a_size > 5)
	{
		fill_stack_b(stack_a, stack_b);
		fill_stack_a(stack_a, stack_b);
	}
	else
		sort_small(stack_a, stack_b, stack_size(*stack_a));
}

int	sorted_stack(t_number *stack)
{
	while (stack)
	{
		if (!stack->next)
			break ;
		if (stack->num > stack->next->num)
			return (0);
		stack = stack->next;
	}
	return (1);
}

int	main(int argc, char **argv)
{
	t_number	*stack_a;
	t_number	*stack_b;
	int			a_size;
	int			*n_array;

	if (argc > 1)
	{
		stack_a = parse_argv(argv);
		if (!stack_a)
			ft_error(NULL, NULL);
		stack_b = NULL;
		a_size = stack_size(stack_a);
		n_array = stack_to_array(stack_a, a_size);
		bubble_sort(n_array, a_size);
		assign_order(stack_a, n_array, a_size);
		if (!sorted_stack(stack_a))
			sort_stack(&stack_a, &stack_b, a_size);
		free_stack(stack_a);
		free(n_array);
	}
	return (0);
}
