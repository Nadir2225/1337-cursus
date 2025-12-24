/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 20:27:49 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/12/24 19:57:08 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlen(const char *s)
{
	unsigned char	*str;
	size_t			len;

	len = 0;
	str = (unsigned char *)s;
	while (str[len])
		len++;
	return (len);
}
