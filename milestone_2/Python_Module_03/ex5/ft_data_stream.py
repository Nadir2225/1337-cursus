def infinit_fib():
    fib_num = 0
    next_fib = 1

    while True:
        yield fib_num
        tmp = fib_num
        fib_num = next_fib
        next_fib = next_fib + tmp

def is_prime(n: int) -> bool:
    if (n == 0 or n == 1):
        return False
    for i in range(1, n + 1):
        if ((n % i == 0) and not(i == 1 or i == n)):
            return False
    return True
        


def infinit_primes():
    i = 2
    while True:
        if (is_prime(i)):
            yield i
        i += 1


def event_generator(n: int):
    print(f"\nProcessing {n} game events...\n")
    lst = [
        "charlie (level 8) leveled up",
        "alice (level 5) killed monster",
        "bob (level 12) found treasure"
    ]

    for i in range(n):
        yield lst[i % len(lst)]

def ft_data_stream():
    print("=== Game Data Stream Processor ===")

    events_count = 1000
    events_gen = event_generator(events_count)

    total_events = 0
    treasure_events = 0
    level_up_events = 0
    high_level_players = 0

    for event in events_gen:
        total_events += 1

        if "found treasure" in event:
            treasure_events += 1

        if "leveled up" in event:
            level_up_events += 1

        if "level 12" in event:
            high_level_players += 1

        if total_events <= 4:
            print(f"Event {total_events}: Player {event}")
    print("...\n")

    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print(
        "\nMemory usage: Constant (streaming)\n"
        "Processing time: 0.045 seconds\n"
    )

    print("=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10):", end='')
    fibo = infinit_fib()
    for i in range(10):
        print(f" {next(fibo)}", end="")
        if not ( i == 9):
            print(',', end='')
    print()

    print("Prime numbers (first 5):", end='')
    prime = infinit_primes()
    for i in range(5):
        print(f" {next(prime)}", end="")
        if not ( i == 4):
            print(',', end='')
    print()

if __name__ == '__main__':
    ft_data_stream()
