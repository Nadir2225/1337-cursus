/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   queue.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/17 11:00:00 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/09/17 11:00:00 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void	enqueue_request(t_table *t, t_dongle *f, t_dongle *s, t_request r)
{
	pthread_mutex_lock(&t->dlock);
	heap_push(&f->queue, r);
	if (s != f)
		heap_push(&s->queue, r);
	pthread_cond_broadcast(&t->dcond);
	pthread_mutex_unlock(&t->dlock);
}

int	is_head(t_dongle *d, int coder_id)
{
	return (d->queue.size > 0 && d->queue.data[0].coder_id == coder_id);
}

int	grantable(t_table *t, int id)
{
	t_dongle	*f;
	t_dongle	*s;

	set_dongles(t, id, &f, &s);
	if (f->queue.size == 0 || s->queue.size == 0)
		return (0);
	if (!is_head(f, id) && grantable(t, f->queue.data[0].coder_id))
		return (0);
	if (!is_head(s, id) && grantable(t, s->queue.data[0].coder_id))
		return (0);
	return (1);
}
