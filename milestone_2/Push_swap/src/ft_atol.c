/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atol.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/31 17:00:09 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/12/31 17:39:45 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

int	valid_number(char *str)
{
	int	i;
	int	in_num;
	int	sign_found;

	i = 0;
	in_num = 0;
	sign_found = 0;
	while (str[i])
	{
		if ((str[i] - 48 >= 0) && (str[i] - 48 <= 9) && in_num == 0)
		{
			in_num = 1;
		}
		else if ((in_num == 0 && sign_found == 0)
			&& (str[i] == '+' || str[i] == '-'))
			sign_found = 1;
		else if (!((str[i] - 48 >= 0) && (str[i] - 48 <= 9)))
			return (0);
		i++;
	}
	return (1);
}

long	ft_atol(char *n)
{
	int	sign;
	long	result;

	result = 0;
	sign = 1;
	if (*n == '+' || *n == '-')
	{
		if (*n == '-')
			sign *= -1;
		n++;
	}
	while (*n >= '0' && *n <= '9')
	{
		result = (result * 10) + *n - '0';
		n++;
	}
	return (result * sign);
}
