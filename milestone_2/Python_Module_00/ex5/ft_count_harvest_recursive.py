def ft_count_harvest_recursive():
    days = int(input('Days until harvest: '))

    def ft_count(day: int, days: int) -> None:
        if day > 1:
            ft_count(day - 1, days)
        if (day == days):
            print(f'Day {day}')
            print('Harvest time!')
        else:
            print(f'Day {day}')

    ft_count(days, days)
