/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 11:14:49 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/11/08 20:08:22 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../includes/ft_printf.h"

static void	neg_number(long *nbr, int *count)
{
	if (*nbr < 0)
	{
		write(1, "-", 1);
		*nbr *= -1;
		(*count)++;
	}
	if (*nbr == 0)
	{
		write(1, "0", 1);
		(*count)++;
	}
}

int	ft_putnbr_fd(int n, int fd)
{
	long	nbr;
	int		i;
	char	display[12];
	int		count;

	nbr = n;
	i = 0;
	count = 0;
	neg_number(&nbr, &count);
	while (nbr > 0)
	{
		display[i++] = (nbr % 10) + '0';
		nbr /= 10;
	}
	while (i > 0)
	{
		write(fd, &display[--i], 1);
		count++;
	}
	return (count);
}
