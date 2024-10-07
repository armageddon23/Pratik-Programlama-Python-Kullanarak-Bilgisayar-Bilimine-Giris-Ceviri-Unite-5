def convert_to_celsius(t, source):
    if source == "Fahrenheit":
        return (t - 32) * 5.0 / 9.0
    elif source == "Kelvin":
        return t - 273.15
    elif source == "Rankine":
        return (t - 491.67) * 5.0 / 9.0
    elif source == "Delisle":
        return 100 - t * 2 / 3
    elif source == "Newton":
        return t * 100.0 / 33.0
    elif source == "Reaumur":
        return t * 5.0 / 4.0
    elif source == "Romer":
        return (t - 7.5) * 40.0 / 24.0
    elif source == "Celsius":
        return t  # Zaten Celsius ise direkt döner
    else:
        raise ValueError("Geçersiz kaynak birimi")

def convert_temperatures(t, source, target):
    # Önce Celsius'a dönüştür
    t_celsius = convert_to_celsius(t, source)
    
    # Celsius'tan hedef birime dönüştürme
    if target == "Fahrenheit":
        return t_celsius * 9.0 / 5.0 + 32
    elif target == "Kelvin":
        return t_celsius + 273.15
    elif target == "Rankine":
        return (t_celsius + 273.15) * 9.0 / 5.0
    elif target == "Delisle":
        return 100 - t_celsius * 3 / 2
    elif target == "Newton":
        return t_celsius * 33.0 / 100.0
    elif target == "Reaumur":
        return t_celsius * 4.0 / 5.0
    elif target == "Romer":
        return t_celsius * 24.0 / 40.0 + 7.5
    elif target == "Celsius":
        return t_celsius  # Zaten Celsius ise direkt döner
    else:
        raise ValueError("Geçersiz hedef birimi")

print(convert_temperatures(100, "Fahrenheit", "Celsius"))
print(convert_temperatures(0, "Kelvin", "Celsius"))
