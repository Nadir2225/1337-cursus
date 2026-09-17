/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   heap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/17 15:40:08 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/09/17 15:40:12 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	req_less(t_request a, t_request b)
{
	if (a.key != b.key)
		return (a.key < b.key);
	if (a.seq != b.seq)
		return (a.seq < b.seq);
	return (a.coder_id < b.coder_id);
}

static void	sift_up(t_heap *h, int size)
{
	t_request	tmp;
	int			i;

	i = size;
	while (i > 0 && req_less(h->data[i], h->data[(i - 1) / 2]))
	{
		tmp = h->data[(i - 1) / 2];
		h->data[(i - 1) / 2] = h->data[i];
		h->data[i] = tmp;
		i = (i - 1) / 2;
	}
}

static void	sift_down(t_heap *h, int i)
{
	t_request	tmp;
	int			size;
	int			child;

	size = h->size;
	while ((i * 2) + 1 < size)
	{
		child = (i * 2) + 1;
		if (child + 1 < size)
			if (req_less(h->data[child + 1], h->data[child]))
				child++;
		if (req_less(h->data[child], h->data[i]))
		{
			tmp = h->data[i];
			h->data[i] = h->data[child];
			h->data[child] = tmp;
		}
		else
			break ;
		i = child;
	}
}

void	heap_push(t_heap *h, t_request r)
{
	h->data[h->size] = r;
	h->size++;
	sift_up(h, h->size - 1);
}

void	heap_remove(t_heap *h, int coder_id)
{
	int	i;

	i = 0;
	while (i < h->size && h->data[i].coder_id != coder_id)
		i++;
	if (i == h->size)
		return ;
	h->size--;
	h->data[i] = h->data[h->size];
	sift_down(h, i);
	sift_up(h, i);
}
