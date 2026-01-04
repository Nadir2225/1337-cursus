/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   commands_2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/03 20:21:29 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/01/03 21:38:47 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

void	ra(t_number **a)
{
	t_number	*tmp;
	t_number	*tail;

	if (!a || !*a || !(*a)->next)
		return ;
	tmp = *a;
	*a = (*a)->next;
	tmp->next = NULL;
	tail = *a;
	while (tail->next)
		tail = tail->next;
	tail->next = tmp;
	write(1, "ra\n", 3);
}

void	rb(t_number **b)
{
	t_number	*tmp;
	t_number	*tail;

	if (!b || !*b || !(*b)->next)
		return ;
	tmp = *b;
	*b = (*b)->next;
	tmp->next = NULL;
	tail = *b;
	while (tail->next)
		tail = tail->next;
	tail->next = tmp;
	write(1, "rb\n", 3);
}

void	rr(t_number **a, t_number **b)
{
	t_number	*tmp;
	t_number	*tail;

	if (a && *a && (*a)->next)
	{
		tmp = *a;
		*a = (*a)->next;
		tmp->next = NULL;
		tail = *a;
		while (tail->next)
			tail = tail->next;
		tail->next = tmp;
	}
	if (b && *b && (*b)->next)
	{
		tmp = *b;
		*b = (*b)->next;
		tmp->next = NULL;
		tail = *b;
		while (tail->next)
			tail = tail->next;
		tail->next = tmp;
	}
	write(1, "rr\n", 3);
}

void	rra(t_number **a)
{
	t_number	*tmp;
	t_number	*head;

	if (!a || !*a || !(*a)->next)
		return ;
	tmp = *a;
	while (tmp->next && tmp->next->next)
		tmp = tmp->next;
	head = tmp->next;
	tmp->next = NULL;
	head->next = *a;
	*a = head;
	write(1, "rra\n", 4);
}

void	rrb(t_number **b)
{
	t_number	*tmp;
	t_number	*head;

	if (!b || !*b || !(*b)->next)
		return ;
	tmp = *b;
	while (tmp->next && tmp->next->next)
		tmp = tmp->next;
	head = tmp->next;
	tmp->next = NULL;
	head->next = *b;
	*b = head;
	write(1, "rrb\n", 4);
}
