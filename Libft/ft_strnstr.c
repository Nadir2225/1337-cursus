/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 20:53:48 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/10/28 14:50:13 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

// little[to_find_i] && big[str_i] == little[to_find_i] && str_i < len
static int	while_expression(char b, char l, size_t i, size_t len)
{
	return (l && b == l && i < len);
}

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t	str_i;
	size_t	to_find_i;
	size_t	i;

	i = 0;
	if (!*little)
		return ((char *)big);
	while (big[i] && i < len)
	{
		if (big[i] == little[0])
		{
			str_i = i;
			to_find_i = 0;
			while (while_expression(big[str_i], little[to_find_i], str_i, len))
			{
				str_i++;
				to_find_i++;
			}
			if (!little[to_find_i])
				return ((char *)&big[i]);
		}
		i++;
	}
	return (NULL);
}
