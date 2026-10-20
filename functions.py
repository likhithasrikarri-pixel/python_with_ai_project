import numpy as np

def calculate_total(marks):
    return int(np.sum(marks))

def calculate_average(marks):
    return float(np.mean(marks))

def assign_grade(avg):
    if avg >= 90: return 'A'
    elif avg >= 80: return 'B'
    elif avg >= 70: return 'C'
    elif avg >= 60: return 'D'
    else: return 'F'

def check_pass_fail(avg, attendance):
    if avg >= 60 and attendance >= 65:
        return 'Pass'
    else:
        return 'Fail'