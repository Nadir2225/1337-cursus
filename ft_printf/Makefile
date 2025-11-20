# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/08 14:28:19 by nel-ouad          #+#    #+#              #
#    Updated: 2025/11/08 19:16:15 by nel-ouad         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libftprintf.a

CC = clang
CFLAGS = -Wall -Wextra -Werror -I includes
SRC = ft_printf.c src/ft_putchar_fd.c src/ft_puthex.c src/ft_putnbr_fd.c src/ft_putptr.c src/ft_putstr_fd.c src/ft_putu.c src/ft_strlen.c
OBJS = ft_printf.o src/ft_putchar_fd.o src/ft_puthex.o src/ft_putnbr_fd.o src/ft_putptr.o src/ft_putstr_fd.o src/ft_putu.o src/ft_strlen.o
AR = ar rcs
RM = rm -f

all: $(NAME)

$(NAME): $(OBJS)
	$(AR) $(NAME) $(OBJS)

test: 
	gcc -I includes $(SRC) test.c -o test.out

clean:
	$(RM) $(OBJS) test.out

fclean: clean
	$(RM) $(NAME)

re: fclean all
