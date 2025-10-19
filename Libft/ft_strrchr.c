/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 20:28:17 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/10/19 14:22:14 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	int		i;
	char	*s2;

	i = 0;
	s2 = NULL;
	while (s[i])
	{
		if (s[i] == (char)c)
			s2 = (char *)&s[i];
		i++;
	}
	if (!(char)c)
		return ((char *)&s[i]);
	return ((char *)s2);
}
