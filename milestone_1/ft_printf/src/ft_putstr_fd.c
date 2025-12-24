/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 11:14:22 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/11/08 16:09:43 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../includes/ft_printf.h"

int	ft_putstr_fd(char *s, int fd)
{
	if (!s)
	{
		write(1, "(null)", 6);
		return (6);
	}
	write(fd, s, ft_strlen(s));
	return ((int)ft_strlen(s));
}
