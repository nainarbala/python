"""
Create a function called 'grade_calculator' that:
- Takes a score (integer) as input
- Returns the grade based on:
  * 90-100: 'A'
  * 80-89: 'B'
  * 70-79: 'C'
  * 60-69: 'D'
  * Below 60: 'F'
 
Test it with scores: 95, 75, 50
"""


def grade_calculator(score):
    if score <= 90 and score <= 100:
        return 'A'
    elif score <= 80 and score <= 89:
        return 'B'
    elif score <= 70 and score <= 79:
        return 'C'
    elif score <= 60 and score <= 69:
        return 'D'
    else:
        return 'F'
