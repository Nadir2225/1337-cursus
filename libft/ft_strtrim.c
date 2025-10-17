/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 09:12:45 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/10/15 09:12:46 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdlib.h>

static int	ft_contains(char c, const char *set)
{
	while (*set)
	{
		if (c == *set)
			return (1);
		set++;
	}
	return (0);
}

char	*ft_strtrim(char const *s1, char const *set)
{
	size_t	start;
	size_t	end;
	char	*str1;
	char	*trimmed;

	if (!s1 || !set)
		return (NULL);
	str1 = (char *)s1;
	start = 0;
	while (str1[start] && ft_contains(str1[start], set))
		start++;
	end = ft_strlen(str1);
	while (end > start && ft_contains(str1[end - 1], set))
		end--;
	trimmed = (char *)malloc(sizeof(char) * (end - start + 1));
	if (!trimmed)
		return (NULL);
	ft_strlcpy(trimmed, str1 + start, end - start + 1);
	return (trimmed);
}
