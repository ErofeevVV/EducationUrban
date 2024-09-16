# использование %
print('В команде Мастера кода участников: %s!' % '5')
print('Итого сегодня участников: %s и %s!' % (5, 6))
print('В команде Мастера кода участников: %(team1_num)s!' % {'team1_num': 5})
print('Итого сегодня участников: %(team1_num)s и %(team2_num)s!' % {'team1_num': 5, 'team2_num': 6})

# использование format()
print('Команда Волшебники данных решила задач: {}'.format(42))
print('{team_name} решила задачи за: {team1_time} секунд'.format(team_name='Волшебники данных', team1_time=18015.2))

# использование f-строк
team_1_name = 'Мастера кода'
score_team_1 = 40
team_1_time = 18015.2
team_2_name = 'Волшебники данных'
score_team_2 = 42
team_2_time = 18116.4
tasks_total = score_team_1 + score_team_2
time_avg = (team_1_time + team_2_time) / tasks_total
print(f'Команды решили {score_team_1} и {score_team_2} задач!')
if score_team_1 > score_team_2:
    print(f'Со счетом {score_team_1} победила команда {team_1_name}!')
elif score_team_1 < score_team_2:
    print(f'Со счетом {score_team_2} победила команда {team_2_name}!')
else:
    print(f'С равным счетом {score_team_1} : {score_team_2} победила дружба!')
print(f'Сегодня было решено {tasks_total} задач, среднее время решения {round(time_avg, 2)}')
