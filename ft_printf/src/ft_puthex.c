/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_puthex.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 14:10:06 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/11/08 20:10:31 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../includes/ft_printf.h"

int	ft_puthex(unsigned int n, int is_upper)
{
	int		count;
	char	*hex;

	count = 0;
	hex = "0123456789abcdef";
	if (is_upper)
		hex = "0123456789ABCDEF";
	if (n >= 16)
		count += ft_puthex(n / 16, is_upper);
	ft_putchar_fd(hex[n % 16], 1);
	count++;
	return (count);
}
