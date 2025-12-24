/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 21:06:10 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/12/11 14:44:30 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*read_and_join(int fd, char	*stash)
{
	char	*buff;
	ssize_t	bytes_read;

	buff = malloc(BUFFER_SIZE + sizeof(char));
	bytes_read = 1;
	while (bytes_read > 0 && !ft_strchr(stash, '\n'))
	{
		bytes_read = read(fd, buff, BUFFER_SIZE);
		if (bytes_read == -1)
		{
			free(buff);
			return (NULL);
		}
		buff[bytes_read] = '\0';
		stash = ft_strjoin(stash, buff);
	}
	free(buff);
	return (stash);
}

char	*extract_line(char *stash)
{
	int		len;
	int		i;
	char	*line;

	len = 0;
	i = 0;
	while (stash[len] && stash[len] != '\n')
		len++;
	if (stash[len] == '\n')
		len++;
	line = malloc((len + 1) * sizeof(char));
	if (!line)
		return (NULL);
	while (i < len)
	{
		line[i] = stash[i];
		i++;
	}
	line[i] = 0;
	return (line);
}

char	*new_stash(char	*stash)
{
	int		start;
	int		i;
	char	*new;

	start = 0;
	i = 0;
	while (stash[start] && stash[start] != '\n')
		start++;
	if (!stash[start])
	{
		free(stash);
		return (NULL);
	}
	new = malloc(ft_strlen(stash) - start + 1);
	if (!new)
		return (NULL);
	start++;
	while (stash[start])
	{
		new[i++] = stash[start++];
	}
	new[i] = 0;
	free(stash);
	return (new);
}

char	*get_next_line(int fd)
{
	static char	*stash;
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	stash = read_and_join(fd, stash);
	if (!stash)
		return (NULL);
	line = extract_line(stash);
	stash = new_stash(stash);
	if (!line[0])
	{
		free(stash);
		free(line);
		return (NULL);
	}
	return (line);
}
