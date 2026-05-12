/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/26 13:43:31 by marvin            #+#    #+#             */
/*   Updated: 2026/05/12 15:27:02 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int	validate_number(char *num, int arg_num)
{
	size_t	i;

	i = 0;
	while (num[i] == ' ' || num[i] == '\t' || num[i] == '\n' || num[i] == '\r')
		i++;
	if (num[i] == '-' || num[i] == '+')
		i++;
	if (i == strlen(num))
	{
		printf("argument %d is not a positive integer\n", arg_num);
		return (0);
	}
	while (i < strlen(num))
	{
		if (num[i] < '0' || num[i] > '9')
		{
			printf("argument %d is not a positive integer\n", arg_num);
			return (0);
		}
		i++;
	}
	return (1);
}

int	validate_args(char **av)
{
	int	arg;
	int	i;

	if (0)
		printf("%s", *av);
	i = 1;
	while (i < 8)
	{
		if (!validate_number(av[i], i))
			return (0);
		arg = atoi(av[i]);
		if (arg <= 0)
		{
			printf("argument %d is not a positive integer\n", i);
			return (0);
		}
		i++;
	}
	if (strcmp(av[8], "fifo") != 0 && strcmp(av[8], "edf") != 0)
	{
		printf("argument 8 must be either 'fifo' or 'edf'\n");
		return (0);
	}
	return (1);
}

int	main(int ac, char **av)
{
	if (ac != 9)
	{
		printf("wrong number of arguments please respect ");
		printf("the following format:\n");
		printf("<program_name> <number_of_coders> <time_to_burnout> ");
		printf("<time_to_compile> <time_to_debug> <time_to_refactor> ");
		printf("<number_of_compiles_required> <dongle_cooldown> <scheduler>\n");
		exit(1);
	}
	if (validate_args(av))
		return (1);
	return (0);
}
