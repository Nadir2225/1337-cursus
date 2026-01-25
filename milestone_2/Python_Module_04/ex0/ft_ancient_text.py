def ft_ancient_text():
    print('=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n')
    print('Accessing Storage Vault: ancient_fragment.txt')
    f = open("ancient_fragment.txt", "r")
    print('Connection established...\n')
    content = f.read()
    print('RECOVERED DATA:')
    print(content)
    f.close()
    print('\nData recovery complete. Storage unit disconnected.')

if __name__ == '__main__':
    ft_ancient_text()