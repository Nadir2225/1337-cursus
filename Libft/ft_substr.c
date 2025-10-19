/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 17:45:41 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/10/17 15:26:28 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

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
