#ifndef CODEXION_H

#include "utils.c"
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>

typedef struct s_params
{
    int     num_coders;
    long    time_to_burnout;
    long    time_to_compile;
    long    time_to_debug;
    long    time_to_refactor;
    int     num_compiles_required;
    long    dongle_cooldown;
    int     use_edf;
}   t_params;


typedef struct s_sim t_sim; 

/* One pending request sitting in a dongle's queue */
typedef struct s_request
{
    int     coder_id;        /* 1..num_coders                                */
    long    deadline;        /* last_compile_start + time_to_burnout (EDF)   */
    long    arrival_ms;      /* timestamp at enqueue (FIFO tiebreak / order) */
}   t_request;

/* A dongle on the table */
typedef struct s_dongle
{
    int             id;                          /* 0..num_coders-1                          */
    int             held_by;                     /* -1 if free, else holder's coder_id       */
    long            release_ms;                  /* ts of last release, for cooldown check   */
    pthread_mutex_t mutex;                       /* protects everything in this struct       */
    pthread_cond_t  cond;                        /* signaled on release / queue change       */
    t_request       queue[2];
    int             queue_len;
}   t_dongle;

/* A coder */
typedef struct s_coder
{
    int             id;                  /* 1..num_coders                                    */
    pthread_t       thread;
    int             left_dongle;         /* index into sim->dongles                          */
    int             right_dongle;        /* index into sim->dongles                          */
    int             compile_count;
    long            last_compile_start;  /* ms since sim->start_ms (init = 0 for first dl)   */
    pthread_mutex_t state_mutex;         /* protects compile_count + last_compile_start      */
    t_sim           *sim;                /* back-pointer to shared state                     */
}   t_coder;

/* Shared simulation state */
struct s_sim
{
    t_params        params;
    t_dongle        *dongles;            /* size = params.num_coders                         */
    t_coder         *coders;             /* size = params.num_coders                         */
    pthread_t       monitor;
    long            start_ms;            /* gettimeofday at sim start; all logs use now - start_ms */
    int             stop;                /* 1 when monitor decides to halt                   */
    pthread_mutex_t stop_mutex;          /* protects `stop` (read by all coders + monitor)   */
    pthread_mutex_t print_mutex;         /* serializes log lines                             */
};

#define INT_MIN -2147483648
#define INT_MAX 2147483647

long ft_atol(const char *str);
int init_sim(t_sim *sim, t_params params);
void destroy_sim(t_sim *sim);

#endif
