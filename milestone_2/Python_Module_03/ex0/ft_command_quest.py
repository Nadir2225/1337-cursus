import sys

def ft_command_quest():
    i = 1
    print('=== Command Quest ===')
    if (len(sys.argv) > 1):
        print(f'Program name: {sys.argv[0]}')
        print(f'Arguments received: {len(sys.argv) - 1}')
        for arg in sys.argv[1:]:
            print(f'Argument {i}: {arg}')
            i += 1
    else:
        print('No arguments provided!')
        print(f'Program name: {sys.argv[0]}')
    print(f'Total arguments: {len(sys.argv)}')
    print()

if __name__ == '__main__':
    ft_command_quest()