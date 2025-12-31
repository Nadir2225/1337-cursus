/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/31 16:24:17 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/12/31 16:49:46 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"



char	**parseArgv(int argc, char **argv)
{
	long	myNum;
	int		i;

	if(argc == 2)
		argv = ft_split(argv[1]);
	i = 0;
	while (argv[i])
	{
		myNum = ft_atol(argv[i]);
		if (myNum)
		i++;
	}
}
