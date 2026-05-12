#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void *hello_thread(void *arg)
{
	printf("hello i'm thread of the id %d\n", *((int *)arg));
}

int main(int ac, char **av)
{
	int n = atoi(av[1]);
	int i = 0;
	pthread_t *threads;
	int *ids;
	threads = (pthread_t *)malloc(n * sizeof(pthread_t *));
	ids = (int *)malloc(n * sizeof(int));

	while (i < n)
	{
		ids[i] = i + 1;
		pthread_create(&threads[i], NULL, hello_thread, &ids[i]);
		i++;
	}
	i = 0;
	while (i < n)
	{
		pthread_join(threads[i], NULL);
		i++;
	}
	free(threads);
	free(ids);
	return 0;
}