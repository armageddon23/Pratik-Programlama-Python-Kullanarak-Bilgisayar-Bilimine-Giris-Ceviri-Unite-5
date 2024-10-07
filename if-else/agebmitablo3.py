age = # Yaş Tanımla
bmi = # Vücut kütle endeksi Tanımla
young = age < 45
slim = bmi < 22.0

if young and slim:
    risk = 'low'
elif young and not slim:
    risk = 'medium'
elif not young and slim:
    risk = 'medium'
elif not young and not slim:
    risk = 'high'

print(risk)
