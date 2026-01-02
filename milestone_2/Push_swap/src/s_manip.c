/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   s_manip.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/31 22:22:02 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/01/02 12:38:55 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

t_number	*new_node(int num)
{
	t_number	*node;

	node = malloc(sizeof(t_number));
	if (!node)
		return (NULL);
	node->num = num;
	node->order = -1;
	node->prev = NULL;
	node->next = NULL;
	return (node);
}

void	add_back(t_number **stack, t_number *new)
{
	t_number	*tmp;

	if (!stack || !new)
		return ;
	if (!*stack)
	{
		*stack = new;
		return ;
	}
	tmp = *stack;
	while (tmp->next)
		tmp = tmp->next;
	tmp->next = new;
	new->prev = tmp;
}

int	stack_size(t_number *stack)
{
	int	count;

	count = 0;
	while (stack)
	{
		count++;
		stack = stack->next;
	}
	return (count);
}
