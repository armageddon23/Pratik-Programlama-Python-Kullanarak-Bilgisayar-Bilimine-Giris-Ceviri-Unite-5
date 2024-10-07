age = # Yaş Tanımla
bmi = # Vücut kütle endeksi Tanımla
young = age < 45
slim = bmi < 22.0
if young:
    if slim:
        risk = 'low'
    else:
        risk = 'medium'
else:
    if slim:
        risk = 'medium'
    else:
        risk = 'high'
print (risk)
