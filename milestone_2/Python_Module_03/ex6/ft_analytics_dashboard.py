def ft_analytics_dashboard():
    print("=== Game Analytics Dashboard ===")
    print("\n=== List Comprehension Examples ===")

    players = [
        {
            "name": "alice",
            "score": 2300,
            "active": True
        },
        {
            "name": "bob",
            "score": 1800,
            "active": True
        },
        {
            "name": "charlie",
            "score": 2150,
            "active": True
        },
        {
            "name": "diana",
            "score": 2050,
            "active": False
        }
    ]
    high_scores = [player['name'] for player in players if player['score'] > 2000]
    scores_doubled = [player['score'] * 2 for player in players]
    active_players = [player['name'] for player in players if player['active']]

    print(f'High scorers (>2000): {high_scores}')
    print(f'Scores doubled: {scores_doubled}')
    print(f'Active players: {active_players}')
    print()

    print('=== Dict Comprehension Examples ===')
    players = [
        {
            "name": "alice",
            "score": 2300,
            "achievements": ['win', 'kill', 'quest', 'boss', 'treasure']
        },
        {
            "name": "bob",
            "score": 1800,
            "achievements": ['win', 'quest', 'boss']
        },
        {
            "name": "charlie",
            "score": 2150,
            "achievements": ['win', 'kill', 'quest', 'boss', 'treasure', 'level', 'arena']
        }
    ]
    players_scores = {player['name']: player['score'] for player in players}
    score_categories = {
        'high': sum(1 for player in players if player['score'] >= 1800),
        'medium': sum(1 for player in players if 1800 <= player['score'] < 2200),
        'low': sum(1 for player in players if player['score'] <= 1800)
    }
    Achievement_counts = {player['name']: len(player['achievements']) for player in players}
    print(f'Player scores: {players_scores}')
    print(f'Score categories: {score_categories}')
    print(f'Achievement counts: {Achievement_counts}')
    print()
    print(f'=== Set Comprehension Examples ===')
    players = [
        {
            "name": "alice",
            "achievements": {"first_kill", "level_10"},
            "region": "north"
        },
        {
            "name": "alice",
            "achievements": {"first_kill"},
            "region": "north"
        },
        {
            "name": "bob",
            "achievements": {"first_kill", "boss_slayer"},
            "region": "east"
        },
        {
            "name": "charlie",
            "achievements": {"first_kill", "level_10", "boss_slayer"},
            "region": "east"
        },
        {
            "name": "diana",
            "achievements": {"first_kill", "level_10"},
            "region": 'central'
        }
    ]
    unique_players = {player["name"] for player in players}
    unique_achievements = {
        ach
        for player in players
        for ach in player["achievements"]
    }
    active_regions = {player["region"] for player in players}
    print(
        f'Unique players: {unique_players}\n'
        f'Unique achievements: {unique_achievements}\n'
        f'Active regions: {active_regions}\n'
    )
    print(f'=== Combined Analysis ===')
    players = [
        {
            "name": "alice",
            "score": 2300,
            "achievements": {
                "first_kill",
                "level_5",
                "level_10",
                "boss_slayer",
                "treasure_hunter"
            }
        },
        {
            "name": "bob",
            "score": 1800,
            "achievements": {
                "first_kill",
                "level_5",
                "level_3",
                "arena_winner"
            }
        },
        {
            "name": "charlie",
            "score": 2000,
            "achievements": {
                "level_10",
                "sharpshooter",
                "explorer"
            }
        },
        {
            "name": "diana",
            "score": 2150,
            "achievements": {
                "boss_slayer",
                "speed_runner",
                "strategist",
                "collector"
            }
        }
    ]
    total_players = len(players)
    total_unique_achievements = len({achv for player in players for achv in player['achievements']})
    average_score = sum(player['score'] for player in players) / len(players)
    max_score = max(player['score'] for player in players)
    top_performer = [player for player in players if player['score'] == max_score][0]
    print(
        f'Total players: {total_players}\n'
        f'Total unique achievements: {total_unique_achievements}\n'
        f'Average score: {average_score}\n'
        f'Top performer: {top_performer['name']} ({top_performer['score']} points, '
        f'{len(top_performer['achievements'])} achievements)'
    )


if __name__ == '__main__':
    ft_analytics_dashboard()