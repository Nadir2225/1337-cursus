/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/26 13:43:31 by marvin            #+#    #+#             */
/*   Updated: 2026/04/26 13:43:31 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void validate_args(char **av)
{
	if (0)
		printf("%s", *av);
	for (int i = 1; i < 8; i++)
	{
		int arg = atoi(av[i]);
		if (arg <= 0)
		{
			printf("argument %d is not a positive integer\n", i);
			exit(1);
		}
	}
	if (strcmp(av[8], "fifo") != 0 && strcmp(av[8], "edf") != 0)
	{
		printf("argument 8 must be either 'fifo' or 'edf'\n");
		exit(1);
	}
}

int main(int ac, char **av)
{
	if (ac != 9)
	{
		printf("wrong number of arguments please respect the following format:\n");
		printf("<program_name> <number_of_coders> <time_to_burnout> ");
		printf("<time_to_compile> <time_to_debug> <time_to_refactor> ");
		printf("number_of_compiles_required> <dongle_cooldown> <scheduler>\n");
		exit(1);
	}
	validate_args(av);
	return (0);
}