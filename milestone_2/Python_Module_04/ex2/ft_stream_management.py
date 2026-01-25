import sys

def ft_stream_management():
    print('=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n')
    id = input('Input Stream active. Enter archivist ID: ')
    status = input('Input Stream active. Enter status report: ')

    print(
        f"\n[STANDARD] Archive status from {id}: {status}",
        file=sys.stdout
    )
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys.stderr
    )
    print(
        "[STANDARD] Data transmission complete\n",
        file=sys.stdout
    )

    print("Three-channel communication test successful.")

if __name__ == '__main__':
    ft_stream_management()