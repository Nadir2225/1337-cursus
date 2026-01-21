import sys

def ft_score_analytics():
    print('=== Player Score Analytics ===')
    if len(sys.argv) > 1:
        try:
            scores = []
            for score in sys.argv[1:]:
                scores.append(int(score))
            print('Scores processed: [', end='')
            i = 1
            for score in scores:
                print(f'{score}{", " if i != len(scores) else ""}', end='')
                i += 1
            print(']')
            print(f'Total players: {len(scores)}')
            print(f'Total score: {sum(scores)}')
            print(f'Average score: {sum(scores) / len(scores)}')
            print(f'High score: {max(scores)}')
            print(f'Low score: {min(scores)}')
            print(f'Score range: {max(scores) - min(scores)}\n')
        except ValueError as e:
            print('all arguments should be valid scores(a number)')
    else:
        print(
            'No scores provided. Usage: python3 '
            'ft_score_analytics.py <score1> <score2> ...'
        )

if __name__ == '__main__':
    ft_score_analytics()