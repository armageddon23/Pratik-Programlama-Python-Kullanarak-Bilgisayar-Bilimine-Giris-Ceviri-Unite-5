age = 22
bmi = 15

young = age < 45
heavy = bmi >= 22.0

if young and not heavy:
    risk = 'low'
elif young and heavy:
    risk = 'medium'

print(risk)