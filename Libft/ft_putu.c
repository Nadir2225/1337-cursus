/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putu.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 11:14:49 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/12/24 19:57:05 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_putu(unsigned int nbr)
{
	int		i;
	char	display[10];
	int		count;

	i = 0;
	count = 0;
	if (nbr == 0)
	{
		write(1, "0", 1);
		count++;
	}
	while (nbr > 0)
	{
		display[i++] = (nbr % 10) + '0';
		nbr /= 10;
	}
	while (i > 0)
	{
		write(1, &display[--i], 1);
		count++;
	}
	return (count);
}
