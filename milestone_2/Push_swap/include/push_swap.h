/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/31 16:25:55 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/01/03 22:02:33 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdarg.h>
# include <stdlib.h>
# include <unistd.h>

# define INT_MAX   2147483647
# define INT_MIN   -2147483647
# define LONG_MAX  9223372036854775807L

typedef struct s_number
{
	int					num;
	int					order;
	struct s_number		*next;
}	t_number;

// args parsing
char		**ft_split(char const *s, char c);
int			valid_number(char *str);
int			valid_array(char **array);
long		ft_atol(char *n);
t_number	*parse_argv(char **argv);
void		check_duplicates(t_number *stack);

// linked list funcs
t_number	*new_node(int num);
void		add_back(t_number **stack, t_number *new);
int			stack_size(t_number *stack);

// free functions
void		ft_error(char **array, t_number *stack);
void		free_stack(t_number *stack);
void		free_array(char **array);

// indexing
int			*stack_to_array(t_number *stack, int size);
void		bubble_sort(int *arr, int size);
void		assign_order(t_number *stack, int *sorted, int size);

// stack OPPS
void		sa(t_number **a);
void		sb(t_number **b);
void		ss(t_number **a, t_number **b);

void		pa(t_number **a, t_number **b);
void		pb(t_number **a, t_number **b);

void		ra(t_number **a);
void		rb(t_number **b);
void		rr(t_number **a, t_number **b);

void		rra(t_number **a);
void		rrb(t_number **b);
void		rrr(t_number **a, t_number **b);

// filling the stacks
void		fill_stack_a(t_number **stack_a, t_number **stack_b);
void		fill_stack_b(t_number **stack_a, t_number **stack_b);

// Utils
// t_number	*find_node_by_order(t_number *stack, int order);
// int			is_sorted(t_number *stack);
// void		free_stack(t_number **stack);
// void		error_exit(void);

#endif