def ft_vault_security():
    print('=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n')
    print('Initiating secure vault access...')
    print('Vault connection established with failsafe protocols\n')
    with open('classified_data.txt', 'r') as f:
        print('SECURE EXTRACTION:')
        print(f.read())
        print()

    with open('security_protocols.txt', 'w') as f2:
        print('SECURE PRESERVATION:')
        f2.write('[CLASSIFIED] New security protocols archived')
        print('[CLASSIFIED] New security protocols archived')
        print('Vault automatically sealed upon completion\n')
    
    print('All vault operations completed with maximum security.')


if __name__ == '__main__':
    ft_vault_security()