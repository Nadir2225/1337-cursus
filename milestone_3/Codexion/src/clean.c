/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   clean.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 15:43:41 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/09/16 15:58:52 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void	join_all(t_table *t)
{
	int	i;

	i = 0;
	while (i < t->n_coders)
	{
		pthread_join(t->coders[i].thread, NULL);
		i++;
	}
	pthread_join(t->monitor, NULL);
}

void	broadcast_all(t_table *t)
{
	pthread_mutex_lock(&t->dlock);
	pthread_cond_broadcast(&t->dcond);
	pthread_mutex_unlock(&t->dlock);
}

void	clean_table(t_table *t)
{
	int	i;

	i = 0;
	while (t->dongles && i < t->n_coders)
	{
		free(t->dongles[i].queue.data);
		i++;
	}
	free(t->dongles);
	free(t->coders);
	pthread_mutex_destroy(&t->state);
	pthread_mutex_destroy(&t->print);
	pthread_mutex_destroy(&t->dlock);
	pthread_cond_destroy(&t->dcond);
}

int	kill_started(t_table *t, int count)
{
	int	i;

	pthread_mutex_lock(&t->state);
	t->over = 1;
	pthread_mutex_unlock(&t->state);
	broadcast_all(t);
	i = 0;
	while (i < count)
	{
		pthread_join(t->coders[i].thread, NULL);
		i++;
	}
	fprintf(stderr, "Error: pthread_create failed\n");
	return (0);
}
