def calculate_fine(extra_days):
    fine = 0
    rate = 10
    week = 1

    while extra_days > 0:
        days_in_week = min(7, extra_days)
        fine += days_in_week * rate
        extra_days -= days_in_week

        week += 1
        rate *= week

    return fine
