*This project has been created as part of the 42 curriculum by nel-ouad.*

## Description

**Codexion** is a concurrency project that consists of simulating a group of coders sharing a limited number of dongles around a table.  
Each coder needs two dongles to compile, then debugs and refactors before starting again, and burns out if too much time passes between two compiles.

The goal is to keep every coder alive while multiple threads compete for the same shared resources, without data races and without deadlocks.

This project implements **only the mandatory part** of Codexion.

## Instructions

### Compilation

make

### Execution

./codexion \<number_of_coders\> \<time_to_burnout\> \<time_to_compile\> \<time_to_debug\> \<time_to_refactor\> \<number_of_compiles_required\> \<dongle_cooldown\> \<scheduler\>

All times are expressed in milliseconds, `scheduler` is either `fifo` or `edf`, and the program prints a timestamped log of every state change until a coder burns out or all of them reach the required number of compiles.

## Algorithm

Each coder runs in its own thread and claims its two dongles by **ordering them by index and queueing a request on both**, which removes the circular wait that would otherwise deadlock the table.  
A request is only granted when the coder holds the claim on both of its dongles, meaning no higher-priority rival is waiting on either of them, so no coder can be starved by its neighbours.

Requests are kept in a **binary heap** per dongle, and the priority key depends on the selected scheduler: `fifo` orders them by arrival ticket, while `edf` orders them by the coder's burnout deadline so the most endangered coder is served first.  
A separate monitor thread watches the deadlines and stops the simulation as soon as a coder burns out or all of them are done.

## Resources

- 42 philosophers subject
- *The Little Book of Semaphores* (dining philosophers chapter)
- POSIX threads documentation (`pthread_mutex`, `pthread_cond`)


