/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putptr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 13:47:31 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/11/08 20:12:24 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../includes/ft_printf.h"

void	ft_putlonghex(unsigned long n, int *count)
{
	if (n >= 16)
		ft_putlonghex(n / 16, count);
	ft_putchar_fd("0123456789abcdef"[n % 16], 1);
	(*count)++;
}

int	ft_putptr(void *p)
{
	unsigned long	addr;
	int				count;

	addr = (unsigned long)p;
	count = 0;
	if (!p)
	{
		count += ft_putstr_fd("(nil)", 1);
		return (count);
	}
	write(1, "0x", 2);
	count += 2;
	if (addr == 0)
		count += ft_putchar_fd('0', 1);
	else
		ft_putlonghex(addr, &count);
	return (count);
}
