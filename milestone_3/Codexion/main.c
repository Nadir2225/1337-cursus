/* ************************************************************************** */
/*																			*/
/*														:::	  ::::::::   */
/*   main.c											 :+:	  :+:	:+:   */
/*													+:+ +:+		 +:+	 */
/*   By: nel-ouad <nel-ouad@student.1337.ma>		+#+  +:+	   +#+		*/
/*												+#+#+#+#+#+   +#+		   */
/*   Created: 2026/08/23 14:48:03 by nel-ouad		  #+#	#+#			 */
/*   Updated: 2026/09/16 17:45:08 by nel-ouad		 ###   ########.fr	   */
/*																			*/
/* ************************************************************************** */

#include "codexion.h"

int	main(int ac, char **av)
{
	t_table	table;

	parse_args(&table, ac, av);
	init_table(&table);
	start_threads(&table);
	join_all(&table);
	clean_table(&table);
	return (0);
}
