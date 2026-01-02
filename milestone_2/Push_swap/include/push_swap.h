/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/31 16:25:55 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/12/31 22:48:10 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
# define LIBFT_H

#include <stdarg.h>
# include <stdlib.h>
# include <unistd.h>

#define INT_MAX   2147483647
#define INT_MIN   -2147483648
#define LONG_MAX  9223372036854775807L

typedef struct s_number
{
	int					num;
	int					order;
	struct s_number		*prev;
	struct s_number		*next;
}	t_number;

// args parsing
char	**ft_split(char const *s, char c);
int		valid_number(char *str);
long	ft_atol(char *n);

// linked list funcs
t_number	*new_node(int num);
void		add_back(t_number **stack, t_number *new);
int			stack_size(t_number *stack);

// indexing
int		*stack_to_array(t_number *stack, int size);
void	bubble_sort(int *arr, int size);
void	assign_order(t_number *stack, int *sorted, int size);

// stack OPPS
void	sa(t_number **a);
void	sb(t_number **b);
void	ss(t_number **a, t_number **b);

void	pa(t_number **a, t_number **b);
void	pb(t_number **a, t_number **b);

void	ra(t_number **a);
void	rb(t_number **b);
void	rr(t_number **a, t_number **b);

void	rra(t_number **a);
void	rrb(t_number **b);
void	rrr(t_number **a, t_number **b);

// Utils
t_number	*find_node_by_order(t_number *stack, int order);
int			is_sorted(t_number *stack);
void		free_stack(t_number **stack);
void		error_exit(void);

#endif