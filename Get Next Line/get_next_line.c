/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 14:25:05 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/10/19 18:22:06 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

int line_append(char **line, char *buffer, size_t bytes_read, char **prev_chunk)
{
	size_t	i;
	int		found;

	i = 0;
	found = 0;
	while (buffer[i] && buffer[i] != '\n')
		i++;
	*line = ft_strcat(*line, ft_substr(buffer, 0, i));
	if (i < bytes_read)
	{
		*line = ft_strcat(*line, "\n");
		found = 1;
	}
	i++;
	char *pos = ft_strchr(buffer, '\n');
	if (pos)
		*prev_chunk = ft_strdup(pos + 1);
	else
		*prev_chunk = NULL;
	return (found);
}

char	*get_next_line(int fd)
{
	static char	*prev_chunk;
	char		*line;
	char		buffer[BUFFER_SIZE + 1];
	size_t		bytes_read;
	int			found;

	line = ft_strdup(prev_chunk);
	found = 0;
	bytes_read = read(fd, buffer, BUFFER_SIZE);
	buffer[bytes_read] = 0;
	while (bytes_read > 0 && !found)
	{
		found = line_append(&line, buffer, bytes_read, &prev_chunk);
		if (contains_multiple(line) && found)
			prev_chunk = ft_strchr(buffer, '\n');
		bytes_read = read(fd, buffer, BUFFER_SIZE);
		buffer[bytes_read] = 0;
	}
	return (line);
}

#include <fcntl.h>
#include <stdio.h>
int main(void)
{
    int fd;
    char *line;

    fd = open("get_next_line.h", O_RDONLY);
    if (fd == -1)
    {
        perror("Error opening file");
        return (1);
    }

    printf("Reading from file:\n\n");
    while ((line = get_next_line(fd)) != NULL)
    {
        printf("LINE: %s", line);
        free(line);
    }

    close(fd);
    return (0);
}
