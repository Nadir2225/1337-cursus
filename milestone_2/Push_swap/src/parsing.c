/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/31 16:24:17 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/01/03 20:40:14 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

void	splitted_array_validator(t_number *stack, char **array)
{
	if (!array)
		ft_error(NULL, stack);
	if (!valid_array(array))
		ft_error(array, stack);
}

t_number	*parse_argv(char **argv)
{
	t_number	*stack;
	char		**splitted_array;
	long		my_num;
	int			i;
	int			k;

	i = 1;
	stack = NULL;
	while (argv[i])
	{
		k = 0;
		splitted_array = ft_split(argv[i++], ' ');
		splitted_array_validator(stack, splitted_array);
		while (splitted_array[k])
		{
			my_num = ft_atol(splitted_array[k++]);
			if (my_num == LONG_MAX)
				ft_error(splitted_array, stack);
			add_back(&stack, new_node(my_num));
		}
		free_array(splitted_array);
	}
	check_duplicates(stack);
	return (stack);
}
