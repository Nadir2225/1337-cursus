/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   dongle.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/17 15:39:37 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/09/17 15:39:44 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

t_request	make_request(t_coder *c)
{
	t_request	r;
	t_table		*t;

	t = c->table;
	r.coder_id = c->id;
	pthread_mutex_lock(&t->state);
	r.seq = t->ticket;
	t->ticket++;
	if (t->edf)
		r.key = c->last_compile + t->t_burnout;
	else
		r.key = r.seq;
	pthread_mutex_unlock(&t->state);
	return (r);
}

static void	wait_until(t_table *t, long deadline)
{
	long			diff;
	struct timeval	tv;
	struct timespec	ts;

	diff = deadline - get_time_ms();
	gettimeofday(&tv, NULL);
	ts.tv_sec = tv.tv_sec + (diff / 1000);
	ts.tv_nsec = (tv.tv_usec * 1000) + ((diff % 1000) * 1000000);
	if (ts.tv_nsec >= 1000000000)
	{
		ts.tv_sec++;
		ts.tv_nsec -= 1000000000;
	}
	pthread_cond_timedwait(&t->dcond, &t->dlock, &ts);
}

static void	wait_for_turn(t_coder *c, t_dongle *f, t_dongle *s)
{
	t_table	*t;
	long	deadline;

	t = c->table;
	while (!sim_over(t))
	{
		if (!grantable(t, c->id) || f->in_use || s->in_use)
			pthread_cond_wait(&t->dcond, &t->dlock);
		else
		{
			deadline = f->free_at;
			if (s->free_at > deadline)
				deadline = s->free_at;
			if (get_time_ms() >= deadline)
				return ;
			wait_until(t, deadline);
		}
	}
}

int	take_dongles(t_coder *c, t_dongle *f, t_dongle *s)
{
	t_table	*t;

	t = c->table;
	pthread_mutex_lock(&t->dlock);
	wait_for_turn(c, f, s);
	heap_remove(&f->queue, c->id);
	heap_remove(&s->queue, c->id);
	pthread_cond_broadcast(&t->dcond);
	if (sim_over(t))
	{
		pthread_mutex_unlock(&t->dlock);
		return (0);
	}
	f->in_use = 1;
	s->in_use = 1;
	pthread_mutex_unlock(&t->dlock);
	log_state(c, "has taken a dongle");
	if (f != s)
		log_state(c, "has taken a dongle");
	return (1);
}

void	release_dongles(t_table *t, t_dongle *f, t_dongle *s)
{
	pthread_mutex_lock(&t->dlock);
	f->in_use = 0;
	f->free_at = get_time_ms() + t->cooldown;
	s->in_use = 0;
	s->free_at = f->free_at;
	pthread_cond_broadcast(&t->dcond);
	pthread_mutex_unlock(&t->dlock);
}
