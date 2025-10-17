/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 19:05:07 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/10/14 19:05:09 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*str1;
	char	*str2;
	char	*str;
	int		i;

	i = 0;
	str1 = (char *)s1;
	str2 = (char *)s2;
	str = malloc((ft_strlen(str1) + ft_strlen(str2) + 1) * sizeof(char));
	if (!str)
		return (NULL);
	while (*str1)
	{
		str[i] = *str1;
		str1++;
		i++;
	}
	while (*str2)
	{
		str[i] = *str2;
		str2++;
		i++;
	}
	str[i] = 0;
	return (str);
}
