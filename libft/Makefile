# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nel-ouad <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/13 20:32:34 by nel-ouad          #+#    #+#              #
#    Updated: 2025/10/13 20:32:36 by nel-ouad         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CC = cc
CFLAGS = -Wall -Wextra -Werror -I .
SRC = *.c
# OBJS = $(SRC:.c=.o)

# NAME = libft.a

all: $(OBJS)
	$(CC) $(CFLAGS) $(SRC) -o test

clean:
	rm -f test

# fclean: clean
# 	rm -f $(NAME)

re: fclean all

all: $(NAME)

.PHONY: all clean fclean re
