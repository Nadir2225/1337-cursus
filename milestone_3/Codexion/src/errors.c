/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   errors.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/21 15:11:46 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/08/23 15:33:29 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void	usage_error(void)
{
	fprintf(stderr, "Usage: ./codexion number_of_coders time_to_burnout "
		"time_to_compile time_to_debug time_to_refactor "
		"number_of_compiles_required dongle_cooldown scheduler\n");
	fprintf(stderr, "All numbers must be positive integers, "
		"scheduler must be 'fifo' or 'edf'\n");
	exit(1);
}

void	allocation_error(t_table *t)
{
	fprintf(stderr, "Error: allocation failed\n");
	clean_table(t);
	exit(1);
}
