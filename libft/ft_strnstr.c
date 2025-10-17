/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 20:53:48 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/10/13 20:53:50 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	const char	*str_copy;
	const char	*to_find_copy;
	size_t		i;

	i = 0;
	if (!*little)
		return ((char *)big);
	while (*big && i < len)
	{
		if (*big == *little)
		{
			str_copy = big;
			to_find_copy = little;
			while (*to_find_copy && *str_copy == *to_find_copy)
			{
				str_copy++;
				to_find_copy++;
			}
			if (!*to_find_copy)
				return ((char *)big);
		}
		i++;
		big++;
	}
	return (0);
}
