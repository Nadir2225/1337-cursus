/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 21:06:05 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/11/09 13:27:16 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

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

	i = 0;
	while (s[i])
	{
		if (s[i] == c)
			return ((char *)&s[i]);
		i++;
	}
	return (NULL);
}

static void	join_helper(unsigned char *s1, unsigned char *s2, char *s, int *i)
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
	unsigned char	*str1;
	unsigned char	*str2;
	char			*str;
	int				i;

	i = 0;
	if (!s1)
		s1 = ft_strdup("");
	str1 = (unsigned char *)s1;
	str2 = (unsigned char *)s2;
	str = malloc((ft_strlen(s1) + ft_strlen(s2) + 1) * sizeof(char));
	if (!str)
		return (NULL);
	join_helper(str1, str2, str, &i);
	str[i] = 0;
	free(s1);
	return (str);
}
