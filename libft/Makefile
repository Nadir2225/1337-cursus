# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/13 20:32:34 by nel-ouad          #+#    #+#              #
#    Updated: 2025/10/17 15:27:02 by nel-ouad         ###   ########.fr        #
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
