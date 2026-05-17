/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_sim.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nel-ouad <nel-ouad@student.1337.ma>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/16 21:18:59 by nel-ouad          #+#    #+#             */
/*   Updated: 2026/05/16 21:19:20 by nel-ouad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static long get_time_ms(void)
{
    struct timeval tv;

    gettimeofday(&tv, NULL);
    return (tv.tv_sec * 1000L + tv.tv_usec / 1000L);
}

static void init_dongle(t_dongle *d, int id)
{
    d->id = id;
    d->held_by = -1;
    d->release_ms = 0;
    d->queue_len = 0;
    memset(d->queue, 0, sizeof(d->queue));
    pthread_mutex_init(&d->mutex, NULL);
    pthread_cond_init(&d->cond, NULL);
}

static void init_coder(t_coder *c, int id, t_sim *sim)
{
    int n;

    n = sim->params.num_coders;
    c->id = id;
    c->compile_count = 0;
    c->last_compile_start = 0;
    c->left_dongle = id - 1;
    c->right_dongle = id % n;
    c->sim = sim;
    pthread_mutex_init(&c->state_mutex, NULL);
}

int init_sim(t_sim *sim, t_params params)
{
    int i;
    int n;

    n = params.num_coders;
    sim->params = params;
    sim->stop = 0;
    sim->start_ms = get_time_ms();
    pthread_mutex_init(&sim->stop_mutex, NULL);
    pthread_mutex_init(&sim->print_mutex, NULL);
    sim->dongles = malloc(sizeof(t_dongle) * n);
    sim->coders = malloc(sizeof(t_coder) * n);
    if (!sim->dongles || !sim->coders)
    {
        free(sim->dongles);
        free(sim->coders);
        return (0);
    }
    i = 0;
    while (i < n)
    {
        init_dongle(&sim->dongles[i], i);
        init_coder(&sim->coders[i], i + 1, sim);
        i++;
    }
    return (1);
}

void destroy_sim(t_sim *sim)
{
    int i;
    int n;

    n = sim->params.num_coders;
    i = 0;
    while (i < n)
    {
        pthread_mutex_destroy(&sim->dongles[i].mutex);
        pthread_cond_destroy(&sim->dongles[i].cond);
        pthread_mutex_destroy(&sim->coders[i].state_mutex);
        i++;
    }
    pthread_mutex_destroy(&sim->stop_mutex);
    pthread_mutex_destroy(&sim->print_mutex);
    free(sim->dongles);
    free(sim->coders);
}