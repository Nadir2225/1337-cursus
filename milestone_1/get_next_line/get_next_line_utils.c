/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 21:06:05 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/12/11 14:55:03 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

size_t	ft_strlen(const char *s)
{
	size_t			len;

	len = 0;
	while (s[len])
		len++;
	return (len);
}

static char	*ft_strdup(const char *s)
{
	int		i;
	char	*dup;

	i = 0;
	while (s[i])
		i++;
	dup = malloc(sizeof(char) * (i + 1));
	if (!dup)
		return (NULL);
	i = 0;
	while (s[i])
	{
		dup[i] = s[i];
		i++;
	}
	dup[i] = 0;
	return (dup);
}

char	*ft_strchr(const char *s, int c)
{
	int	i;

	if (!s)
		return (NULL);
	i = 0;
	while (s[i])
	{
		if (s[i] == c)
			return ((char *)&s[i]);
		i++;
	}
	return (NULL);
}

static void	join_helper(char *s1, char *s2, char *s, int *i)
{
	while (*s1)
	{
		s[*i] = *s1;
		s1++;
		(*i)++;
	}
	while (*s2)
	{
		s[*i] = *s2;
		s2++;
		(*i)++;
	}
}

char	*ft_strjoin(char *s1, char *s2)
{
	char			*str;
	int				i;

	i = 0;
	if (!s1)
		s1 = ft_strdup("");
	str = malloc((ft_strlen(s1) + ft_strlen(s2) + 1) * sizeof(char));
	if (!str)
		return (NULL);
	join_helper(s1, s2, str, &i);
	str[i] = 0;
	free(s1);
	return (str);
}
