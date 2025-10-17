/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 20:32:24 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/10/17 18:12:08 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include "libft.h" 

static void print_split(char **result)
{
    int i = 0;
    if (!result)
    {
        printf("Result is NULL\n");
        return;
    }
    while (result[i])
    {
        printf("result[%d] = '%s'\n", i, result[i]);
        i++;
    }
    printf("result[%d] = %s\n", i, result[i]); // should print (null)
}

int main(void)
{
    char **result;

    printf("=== Test 1 ===\n");
    result = ft_split("Hello world this is C", ' ');
    print_split(result);
    free(result);

    printf("\n=== Test 2 ===\n");
    result = ft_split("   split   these words  ", ' ');
    print_split(result);
    free(result);

    printf("\n=== Test 3 ===\n");
    result = ft_split("one,two,,three,", ',');
    print_split(result);
    free(result);

    printf("\n=== Test 4 ===\n");
    result = ft_split("", ' ');
    print_split(result);
    free(result);

    printf("\n=== Test 5 ===\n");
    result = ft_split(NULL, ' ');
    print_split(result);
    free(result);

    return 0;
}
