/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 15:39:27 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/09/16 16:29:29 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	init_dongles(t_table *t)
{
	int	i;

	i = 0;
	while (i < t->n_coders)
	{
		t->dongles[i].in_use = 0;
		t->dongles[i].free_at = t->start_time;
		t->dongles[i].queue.data = malloc(sizeof(t_request) * t->n_coders);
		if (!t->dongles[i].queue.data)
			allocation_error(t);
		t->dongles[i].queue.size = 0;
		i++;
	}
}

static void	init_coders(t_table *t)
{
	int	i;

	i = 0;
	while (i < t->n_coders)
	{
		t->coders[i].id = i + 1;
		t->coders[i].compiles = 0;
		t->coders[i].last_compile = t->start_time;
		t->coders[i].table = t;
		i++;
	}
}

void	init_table(t_table *t)
{
	pthread_mutex_init(&t->state, NULL);
	pthread_mutex_init(&t->print, NULL);
	pthread_mutex_init(&t->dlock, NULL);
	pthread_cond_init(&t->dcond, NULL);
	t->over = 0;
	t->ticket = 0;
	t->start_time = get_time_ms();
	t->dongles = malloc(sizeof(t_dongle) * t->n_coders);
	if (t->dongles)
		memset(t->dongles, 0, sizeof(t_dongle) * t->n_coders);
	t->coders = malloc(sizeof(t_coder) * t->n_coders);
	if (t->coders)
		memset(t->coders, 0, sizeof(t_coder) * t->n_coders);
	if (!t->dongles || !t->coders)
		allocation_error(t);
	init_coders(t);
	init_dongles(t);
}

void	start_threads(t_table *t)
{
	int	i;

	t->start_time = get_time_ms();
	i = 0;
	while (i < t->n_coders)
	{
		t->coders[i].last_compile = t->start_time;
		i++;
	}
	i = 0;
	while (i < t->n_coders)
	{
		if (pthread_create(&t->coders[i].thread, NULL,
				coder_routine, &t->coders[i]) != 0)
		{
			kill_started(t, i);
			allocation_error(t);
		}
		i++;
	}
	if (pthread_create(&t->monitor, NULL, monitor_routine, t) != 0)
	{
		kill_started(t, i);
		allocation_error(t);
	}
}
