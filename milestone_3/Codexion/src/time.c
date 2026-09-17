/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   time.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 15:41:01 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/09/15 21:32:00 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

long	get_time_ms(void)
{
	struct timeval	tv;

	gettimeofday(&tv, NULL);
	return ((long)tv.tv_sec * 1000 + tv.tv_usec / 1000);
}

void	ms_sleep(t_table *t, long ms)
{
	long	end;

	end = get_time_ms() + ms;
	while (get_time_ms() < end)
	{
		if (sim_over(t))
			return ;
		usleep(200);
	}
}
