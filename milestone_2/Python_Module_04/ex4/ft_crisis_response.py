def ft_crisis_response(filename: str, mode: str, content: str | None) -> None:
    try:
        with open(filename, mode) as f:
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
            if mode == 'r':
                print(f"SUCCESS: Archive recovered - ``{f.read()}''")
            elif mode == 'w':
                f.write(content)
                print(f"SUCCESS: wrote content - ``{content}''")
    except FileNotFoundError as e:
        print(
            f"CRISIS ALERT: Attempting access to '{e.filename}'...\n"
            'RESPONSE: Archive not found in storage matrix\n'
            'STATUS: Crisis handled, system stable'
        )
    except PermissionError as e:
        print(
            f"CRISIS ALERT: Attempting access to '{e.filename}'...\n"
            'RESPONSE: Security protocols deny access\n'
            'STATUS: Crisis handled, security maintained'
        )
    else:
        print("STATUS: Normal operations resumed")
    print()
    

if __name__ == '__main__':
    print('=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n')
    ft_crisis_response('lost_archive.txt', 'r', None)
    ft_crisis_response('classified_vault.txt', 'w', 'content')
    ft_crisis_response('standard_archive.txt', 'r', None)
    print('All crisis scenarios handled successfully. Archives secure.')