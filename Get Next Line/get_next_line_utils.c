/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 14:26:20 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/10/19 18:07:07 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_strchr(const char *s, int c)
{
	int	i;

	i = 0;
	while (s[i])
	{
		if (s[i] == c)
			return ((char *)&s[i + 1]);
		i++;
	}
	if (!(char)c)
		return ((char *)&s[i]);
	return (NULL);
}

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*substr;
	size_t	i;

	i = 0;
	s += start;
	substr = malloc((len + 1) * sizeof(char));
	if (!substr)
		return (NULL);
	while (*s && i < len)
	{
		substr[i] = *s;
		s++;
		i++;
	}
	substr[i] = 0;
	return (substr);
}

char	*ft_strdup(const char *s)
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

char	*ft_strcat(char *s1, char *s2)
{
	char	*str;
	int		len1;
	int		len2;
	int		i;

	len1 = 0;
	len2 = 0;
	i = 0;
	while(s1[len1])
		len1++;
	while(s2[len2])
		len2++;
	str = malloc(sizeof(char) * (len1 + len2 + 1));
	if (!str)
		return (NULL);
	while (i < len1 + len2)
	{
		str[i] = len1 > i ? s1[i] : s2[i - len1];
		i++;
	}
	str[i] = 0;
	return (str);
}

int contains_multiple(char *line)
{
	int	count;
	int	i;

	i = 0;
	count = 0;
	while (line[i])
	{
		if (line[i] == '\n')
		{
			count++;
			if (count >= 2)
				return 1;
		}
	}
	return (0);
}
