/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 20:32:24 by nel-ouad          #+#    #+#             */
/*   Updated: 2025/10/13 20:32:26 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include "libft.h" // Make sure ft_strtrim is declared here

int main(void)
{
    char *result;

    // Test 1: Trim spaces
    result = ft_strtrim("   Hello Worldf    ", " ");
    printf("Test 1: '%s'\n", result); // Expected: "Hello World"
    free(result);

    // Test 2: Trim specific chars
    result = ft_strtrim("xxxHello Worldxxx", "x");
    printf("Test 2: '%s'\n", result); // Expected: "Hello World"
    free(result);

    // Test 3: Trim multiple chars
    result = ft_strtrim("!?Hello World?!", "!?");
    printf("Test 3: '%s'\n", result); // Expected: "Hello World"
    free(result);

    // Test 4: Nothing to trim
    result = ft_strtrim("Hello", "x");
    printf("Test 4: '%s'\n", result); // Expected: "Hello"
    free(result);

    // Test 5: All chars trimmed
    result = ft_strtrim("xxxx", "x");
    printf("Test 5: '%s'\n", result); // Expected: "" (empty string)
    free(result);

    // Test 6: Empty string input
    result = ft_strtrim("", " ");
    printf("Test 6: '%s'\n", result); // Expected: "" (empty string)
    free(result);

    // Test 7: Empty set (nothing trimmed)
    result = ft_strtrim("  Hello  ", "");
    printf("Test 7: '%s'\n", result); // Expected: "  Hello  "
    free(result);

    return 0;
}

