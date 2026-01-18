# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/04 19:38:31 by nel-ouad          #+#    #+#              #
#    Updated: 2026/01/18 12:01:32 by nel-ouad         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = push_swap

CC = cc
CFLAGS = -Wall -Wextra -Werror -I include
SRC = main.c src/commands_2.c  src/commands.c  src/fill_stack.c  src/free_funcs.c  src/ft_atol.c  src/ft_split.c  src/indexing.c  src/parsing.c  src/stack_utils.c src/sort_small.c
RM = rm -f

all: $(NAME)

$(NAME):
	$(CC) $(CFLAGS) $(SRC) -o $(NAME)

clean:
	$(RM) $(NAME)

fclean: clean

re: fclean all

.PHONY: all clean fclean re
