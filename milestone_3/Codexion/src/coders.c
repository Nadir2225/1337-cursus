/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   coders.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/17 15:39:55 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/09/17 15:39:58 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void	set_dongles(t_table *t, int id, t_dongle **first, t_dongle **second)
{
	int	left;
	int	right;

	left = id - 1;
	right = id % t->n_coders;
	if (left < right)
	{
		*first = &t->dongles[left];
		*second = &t->dongles[right];
	}
	else
	{
		*first = &t->dongles[right];
		*second = &t->dongles[left];
	}
}

static void	do_compile(t_coder *c)
{
	t_table	*t;

	t = c->table;
	pthread_mutex_lock(&t->state);
	c->last_compile = get_time_ms();
	pthread_mutex_unlock(&t->state);
	log_state(c, "is compiling");
	ms_sleep(t, t->t_compile);
	pthread_mutex_lock(&t->state);
	c->compiles++;
	pthread_mutex_unlock(&t->state);
}

int	one_cycle(t_coder *c, t_dongle *first, t_dongle *second)
{
	t_table	*t;

	t = c->table;
	enqueue_request(t, first, second, make_request(c));
	if (!take_dongles(c, first, second))
		return (0);
	do_compile(c);
	release_dongles(t, first, second);
	log_state(c, "is debugging");
	ms_sleep(t, t->t_debug);
	log_state(c, "is refactoring");
	ms_sleep(t, t->t_refactor);
	return (!sim_over(t));
}

static void	*lone_coder(t_coder *c, t_dongle *d)
{
	enqueue_request(c->table, d, d, make_request(c));
	take_dongles(c, d, d);
	while (!sim_over(c->table))
		usleep(500);
	release_dongles(c->table, d, d);
	return (NULL);
}

void	*coder_routine(void *arg)
{
	t_coder		*c;
	t_dongle	*first;
	t_dongle	*second;

	c = arg;
	set_dongles(c->table, c->id, &first, &second);
	if (first == second)
		return (lone_coder(c, first));
	if (c->id % 2 == 0)
		ms_sleep(c->table, c->table->t_compile);
	while (one_cycle(c, first, second))
		continue ;
	return (NULL);
}
