/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 11:14:49 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/10/27 17:45:25 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	long	nbr;
	int		i;
	char	display[12];

	nbr = n;
	i = 0;
	if (nbr < 0)
	{
		write(fd, "-", 1);
		nbr *= -1;
	}
	if (nbr == 0)
		write(fd, "0", 1);
	while (nbr > 0)
	{
		display[i++] = (nbr % 10) + '0';
		nbr /= 10;
	}
	while (i > 0)
		write(fd, &display[--i], 1);
}
