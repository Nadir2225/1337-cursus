*This project has been created as part of the 42 curriculum by nel-ouad.*

# Get Next Line (GNL) — Mandatory Part Only

## Description

A minimal implementation of `get_next_line`, a function that returns one line at a time from a file descriptor. This version includes **only the mandatory part** (no bonus).

## Instructions

### Compilation

```bash
cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 *.c -I .
```

It can work just fine with or without specifying the `BUFFER_SIZE` macro.

### Usage

```c
char *line = get_next_line(fd);
```

Returns a heap‑allocated string (must be freed). Returns `NULL` on EOF or error.

## File Structure

```
get_next_line.h
get_next_line.c
get_next_line_utils.c
```

## Resources

* man pages: `read`, `open`, `malloc`, `free`
* 42 subject PDF
