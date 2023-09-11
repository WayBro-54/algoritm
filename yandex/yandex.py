
# Чтение входных данных
start_date = list(map(int, input().split()))
end_date = list(map(int, input().split()))

# Количество дней в каждом месяце
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Распаковка дат
start_year, start_month, start_day, start_hour, start_minute, start_second = start_date
end_year, end_month, end_day, end_hour, end_minute, end_second = end_date

# Вычисление количества дней между датами
total_days = 0

for year in range(start_year, end_year + 1):
    max_month = 12 if year < end_year else end_month
    min_month = start_month if year == start_year else 1

    for month in range(min_month, max_month + 1):
        max_day = days_in_month[month - 1] if (year < end_year or month < end_month) else end_day
        min_day = start_day if (year == start_year and month == start_month) else 1

        for day in range(min_day, max_day + 1):
            total_days += 1

# Вычисление количества секунд в неполном дне
total_seconds = (end_hour * 3600 + end_minute * 60 + end_second) - (
            start_hour * 3600 + start_minute * 60 + start_second)

# Вывод результата
print(total_days - 1, total_seconds)