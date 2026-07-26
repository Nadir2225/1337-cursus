/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/26 13:43:31 by marvin            #+#    #+#             */
/*   Updated: 2026/05/18 14:58:23 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./codexion.h"

void    print_params(t_params params)
{
    printf("num_coders: %d\n", params.num_coders);
    printf("time_to_burnout: %ld\n", params.time_to_burnout);
    printf("time_to_compile: %ld\n", params.time_to_compile);
    printf("time_to_debug: %ld\n", params.time_to_debug);
    printf("time_to_refactor: %ld\n", params.time_to_refactor);
    printf("num_compiles_required: %d\n", params.num_compiles_required);
    printf("dongle_cooldown: %ld\n", params.dongle_cooldown);
    printf("use_edf: %d\n", params.use_edf);
}

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

int fill_params(t_params *params, long arg, int i)
{
	if (i == 1 || i == 6)
	{
		if (arg < 1)
		{
			free(params);
			printf("argument %d should be 1 or more\n", i);
			return (0);
		}
		if (arg > INT_MAX || arg < INT_MIN)
		{
			free(params);
			printf("argument %d should be an integer bigger than 1\n", i);
			return (0);
		}
		if (i == 1)
			params->num_coders = arg;
		else
			params->num_compiles_required = arg;
	}
	switch (i)
	{
		case 2:
			params->time_to_burnout = arg;
			break;
		case 3:
			params->time_to_compile = arg;
			break;
		case 4:
			params->time_to_debug = arg;
			break;
		case 5:
			params->time_to_refactor = arg;
			break;
		case 7:
			params->dongle_cooldown = arg;
			break;
	}
	return (1);
}

int	validate_args(char **av, t_params *params)
{
	long			arg;
	int			i;

	if (0)
		printf("%s", *av);
	i = 1;
	while (i < 8)
	{
		if (!validate_number(av[i], i))
			return (0);
		arg = ft_atol(av[i]);
		if (arg <= 0)
		{
			free(params);
			printf("argument %d is not a positive integer or long\n", i);
			return (0);
		}
		if (!fill_params(params, arg, i))
			return(0);
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
	t_sim		sim;
	t_params	*params;
	if (ac != 9)
	{
		printf("wrong number of arguments please respect ");
		printf("the following format:\n");
		printf("<program_name> <number_of_coders> <time_to_burnout> ");
		printf("<time_to_compile> <time_to_debug> <time_to_refactor> ");
		printf("<number_of_compiles_required> <dongle_cooldown> <scheduler>\n");
		exit(1);
	}
	params = (t_params *)malloc(sizeof(t_params));
	if (!validate_args(av, params))
		return (1);
	params->use_edf = !strcmp(av[8], "edf");
	print_params(*params);

	if (!init_sim(&sim, *params))
		return (1);
	/* launch coder threads + monitor here */
	/* pthread_join all */
	destroy_sim(&sim);
	return (0);
}
