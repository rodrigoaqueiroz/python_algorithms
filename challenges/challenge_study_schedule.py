def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                count += 1
    except TypeError:
        return None
    return count
