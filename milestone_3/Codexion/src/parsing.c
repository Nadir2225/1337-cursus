/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/21 14:46:36 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/09/16 15:53:19 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	is_number(char *s)
{
	int	i;

	if (!s[0])
		return (0);
	i = 0;
	while (s[i])
	{
		if (s[i] < '0' || s[i] > '9')
			return (0);
		i++;
	}
	return (i <= 10);
}

static long	to_long(char *s)
{
	long	n;
	int		i;

	n = 0;
	i = 0;
	while (s[i])
	{
		n = n * 10 + (s[i] - '0');
		i++;
	}
	return (n);
}

static int	set_values(t_table *t, char **argv)
{
	if (to_long(argv[1]) < 1 || to_long(argv[1]) > INT_MAX)
		return (0);
	t->n_coders = to_long(argv[1]);
	t->t_burnout = to_long(argv[2]);
	t->t_compile = to_long(argv[3]);
	t->t_debug = to_long(argv[4]);
	t->t_refactor = to_long(argv[5]);
	t->must_compile = to_long(argv[6]);
	t->cooldown = to_long(argv[7]);
	t->edf = strcmp(argv[8], "edf") == 0;
	if (t->t_burnout > INT_MAX || t->t_compile > INT_MAX
		|| t->t_debug > INT_MAX || t->t_refactor > INT_MAX
		|| t->must_compile > INT_MAX || t->cooldown > INT_MAX)
		return (0);
	return (1);
}

void	parse_args(t_table *t, int argc, char **argv)
{
	int	i;

	if (argc != 9)
		usage_error();
	i = 1;
	while (i <= 7)
	{
		if (!is_number(argv[i]))
			usage_error();
		i++;
	}
	if (strcmp(argv[8], "fifo") != 0 && strcmp(argv[8], "edf") != 0)
		usage_error();
	if (!set_values(t, argv))
		usage_error();
}
