/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 16:57:21 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/10/27 17:20:55 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	ft_ilen(long n)
{
	long	nb;
	size_t	len;

	nb = n;
	len = 0;
	if (n == 0)
		len = 1;
	while (nb > 0)
	{
		nb /= 10;
		len++;
	}
	return (len);
}

static void	ft_fillnbr(char *a_number, long nbr, size_t len, int sign)
{
	if (nbr == 0)
		a_number[0] = '0';
	while (nbr > 0)
	{
		a_number[(len - 1) + !sign] = (nbr % 10) + '0';
		nbr /= 10;
		len--;
	}
}

char	*ft_itoa(int n)
{
	char	*a_number;
	size_t	len;
	long	nbr;
	int		sign;

	nbr = n;
	if (nbr < 0)
	{
		sign = 0;
		nbr *= -1;
	}
	else
		sign = 1;
	len = ft_ilen(nbr);
	a_number = malloc(sizeof(char) * (len + 1 + !sign));
	if (!a_number)
		return (NULL);
	if (!sign)
		a_number[0] = '-';
	ft_fillnbr(a_number, nbr, len, sign);
	a_number[len + !sign] = 0;
	return (a_number);
}
