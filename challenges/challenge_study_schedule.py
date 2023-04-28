def study_schedule(permanence_period: list[tuple], target_time: int) -> int:
    if not isinstance(target_time, int):
        return None
    
    if not all(isinstance(period[0], int) and isinstance(period[1], int) for period in permanence_period):
        return None
    
    people_counter = sum(1 for period in permanence_period if target_time in range(period[0], period[1] + 1))
    return people_counter


