/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 13:51:49 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/11/20 16:34:44 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdarg.h>
#include "includes/ft_printf.h"

int	is_format_specifier(unsigned char c)
{
	char	*set;

	set = "cspdiuxX%";
	while (*set)
	{
		if (*set == c)
			return (1);
		set++;
	}
	return (0);
}

static int	print_format(va_list args, unsigned char f)
{
	if (f == 'd' || f == 'i')
		return (ft_putnbr_fd(va_arg(args, int), 1));
	else if (f == 'c')
		return (ft_putchar_fd((char)va_arg(args, int), 1));
	else if (f == 's')
		return (ft_putstr_fd(va_arg(args, char *), 1));
	else if (f == 'p')
		return (ft_putptr(va_arg(args, void *)));
	else if (f == 'u')
		return (ft_putu(va_arg(args, unsigned int)));
	else if (f == 'x')
		return (ft_puthex(va_arg(args, unsigned int), 0));
	else if (f == 'X')
		return (ft_puthex(va_arg(args, unsigned int), 1));
	else if (f == '%')
		return (ft_putchar_fd('%', 1));
	else if (f == '\0')
		return (-1);
	return (0);
}

int	ft_printf(const char *s, ...)
{
	va_list	args;
	char	*s1;
	int		count;

	s1 = (char *)s;
	va_start(args, s);
	count = 0;
	while (*s1)
	{
		if (*s1 == '%' && is_format_specifier((unsigned char)*(s1 + 1)))
		{
			count += print_format(args, (unsigned char)*(s1 + 1));
			s1 += 2;
		}
		else
		{
			write(1, s1++, 1);
			count++;
		}
	}
	if (count == 0)
		return (-1);
	va_end(args);
	return (count);
}
