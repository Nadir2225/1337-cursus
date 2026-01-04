/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/03 16:08:50 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/01/04 19:17:26 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "include/push_swap.h"

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
		fill_stack_b(&stack_a, &stack_b);
		fill_stack_a(&stack_a, &stack_b);
	}
	return (0);
}
