NAME	= codexion

CC		= cc
CFLAGS	= -Wall -Wextra -Werror -pthread -I includes

SRC		= src/parsing.c \
		  src/init.c \
		  src/coders.c \
		  src/dongle.c \
		  src/heap.c \
		  src/queue.c \
		  src/errors.c \
		  src/monitor.c \
		  src/log.c \
		  src/time.c \
		  src/clean.c

all: $(NAME)

$(NAME):
	$(CC) $(CFLAGS) main.c $(SRC) -o $(NAME)

clean:
	$(RM) $(NAME)

fclean: clean


re: fclean all

.PHONY: all clean fclean re
