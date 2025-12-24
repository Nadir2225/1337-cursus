# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/13 20:32:34 by nel-ouad          #+#    #+#              #
#    Updated: 2025/12/24 20:48:16 by nel-ouad         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CC = cc
CFLAGS = -Wall -Wextra -Werror -I .

NAME = libft.a
SRC = ft_atoi.c ft_lstadd_back.c ft_memchr.c ft_split.c ft_strncmp.c \
	ft_bzero.c ft_memcmp.c ft_strchr.c ft_strnstr.c ft_calloc.c ft_memcpy.c \
	ft_strdup.c ft_strrchr.c ft_isalnum.c ft_memmove.c ft_striteri.c \
	ft_strtrim.c ft_isalpha.c ft_memset.c ft_strjoin.c ft_substr.c ft_isascii.c \
	ft_putchar_fd.c ft_strlcat.c ft_tolower.c ft_isdigit.c ft_putendl_fd.c \
	ft_strlcpy.c ft_toupper.c ft_isprint.c ft_putnbr_fd.c ft_strlen.c ft_itoa.c \
	ft_putstr_fd.c ft_strmapi.c ft_printf.c ft_putchar_fd_pf.c ft_puthex.c ft_putnbr_fd_pf.c \
	ft_putptr.c ft_putstr_fd_pf.c ft_putu.c
BONUS_SRCS  = ft_lstadd_front.c ft_lstclear.c ft_lstdelone.c ft_lstiter.c \
	ft_lstlast.c ft_lstmap.c ft_lstnew.c ft_lstsize.c
OBJS = $(SRC:.c=.o)
BONUS_OBJS  = $(BONUS_SRCS:.c=.o)
AR = ar rcs
RM = rm -f

all: $(NAME)

$(NAME): $(OBJS)
	$(AR) $(NAME) $(OBJS)

bonus: $(BONUS_OBJS)
	$(AR) $(NAME) $(BONUS_OBJS)

clean:
	$(RM) $(OBJS) $(BONUS_OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all
