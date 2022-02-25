def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    student_number = 0

    for index in permanence_period:
        try:
            if index[0] <= target_time and target_time <= index[1]:
                student_number += 1
        except (TypeError, ValueError):
            return None

    return student_number

# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5))
