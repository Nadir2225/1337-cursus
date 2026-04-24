#include <stdio.h>
#include <stdlib.h>

void validate_args(char **av)
{
	printf("%d", atoi("20JH5"));
	if (0)
		printf("%s", *av);
}

int main(int ac, char **av)
{
	if (ac != 8)
	{
		printf("wrong number of arguments please respect the following format:\n");
		printf("<program_name> <number_of_coders> <time_to_burnout> ");
		printf("<time_to_compile> <time_to_debug> <time_to_refactor> ");
		printf("number_of_compiles_required> <dongle_cooldown>\n");
		return (1);
	}
	validate_args(av);
	return (0);
}