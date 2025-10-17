/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 16:57:31 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/10/17 16:57:36 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	unsigned char	*str;
	char			*mapped_str;
	size_t			i;
	size_t			len;

	i = 0;
	str = (unsigned char *)s;
	len = ft_strlen(s);
	mapped_str = malloc(sizeof(char) * (len + 1));
	while (i < len)
	{
		mapped_str[i] = f(i, str[i]);
		i++;
	}
	mapped_str[i] = 0;
	return (mapped_str);
}
