/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 09:12:45 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/10/17 16:42:28 by nel-ouad         ###   ########.fr       */
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
	size_t			start;
	size_t			end;
	unsigned char	*str1;
	char			*trimmed;

	if (!s1 || !set)
		return (NULL);
	str1 = (unsigned char *)s1;
	start = 0;
	while (str1[start] && ft_contains(str1[start], set))
		start++;
	end = ft_strlen(s1);
	while (end > start && ft_contains(str1[end - 1], set))
		end--;
	trimmed = (char *)malloc(sizeof(char) * (end - start + 1));
	if (!trimmed)
		return (NULL);
	ft_strlcpy(trimmed, (const char *)(str1 + start), end - start + 1);
	return (trimmed);
}
