age = # Yaş Tanımla
bmi = # Vücut kütle endeksi Tanımla
if age < 45:
    if bmi < 22.0:
        risk = 'low'
    else:
        risk = 'medium'
else:
    if bmi < 22.0:
        risk = 'medium'
    else:
        risk = 'high'
print (risk)