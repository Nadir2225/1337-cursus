/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   commands_3.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/03 20:22:27 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/01/03 20:22:33 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

void	rrr(t_number **a, t_number **b)
{
	t_number	*tmp;
	t_number	*head;

	if (a && *a && (*a)->next)
	{
		tmp = *a;
		while (tmp->next && tmp->next->next)
			tmp = tmp->next;
		head = tmp->next;
		tmp->next = NULL;
		head->next = *a;
		*a = head;
	}
	if (b && *b && (*b)->next)
	{
		tmp = *b;
		while (tmp->next && tmp->next->next)
			tmp = tmp->next;
		head = tmp->next;
		tmp->next = NULL;
		head->next = *b;
		*b = head;
	}
	write(1, "rrr\n", 4);
}
