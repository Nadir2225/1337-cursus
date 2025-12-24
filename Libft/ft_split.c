/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 17:02:45 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/10/28 14:50:29 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	count_words(char const *s, char c)
{
	int	count;
	int	i;
	int	in_word;

	count = 0;
	in_word = 0;
	i = 0;
	while (s[i])
	{
		if (!in_word && s[i] != c)
		{
			count++;
			in_word = 1;
		}
		else if (in_word && s[i] == c)
		{
			in_word = 0;
		}
		i++;
	}
	return (count);
}

static char	*ft_strldup(const char *s, int i, int len)
{
	int		k;
	char	*dup;

	k = 0;
	dup = malloc(sizeof(char) * (len + 1));
	if (!dup)
		return (NULL);
	while (s[i] && k < len)
	{
		dup[k++] = s[i];
		i++;
	}
	dup[k] = 0;
	return (dup);
}

static void	my_free(char **arr, int i)
{
	while (i >= 0)
		free(arr[i--]);
	free(arr);
}

static void	fill_array(char const *s, char c, char	**words_array)
{
	int	i;
	int	start;
	int	l;

	i = 0;
	l = 0;
	while (s[i])
	{
		if (s[i] != c)
		{
			start = i;
			while (s[i] && s[i] != c)
				i++;
			words_array[l] = ft_strldup(s, start, i - start);
			if (!words_array[l])
				return (my_free(words_array, l));
			l++;
		}
		else
			i++;
	}
}

char	**ft_split(char const *s, char c)
{
	char	**words_array;

	words_array = malloc(sizeof(char *) * (count_words(s, c) + 1));
	if (!words_array)
		return (NULL);
	fill_array(s, c, words_array);
	if (!words_array)
		return (NULL);
	words_array[count_words(s, c)] = NULL;
	return (words_array);
}
