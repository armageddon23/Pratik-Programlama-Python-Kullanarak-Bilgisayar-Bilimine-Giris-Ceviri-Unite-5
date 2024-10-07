def turn_camera_on():
    print("Kamera açıldı!")

light = 0.09
temperature = 0.1
if (light < 0.01) or (temperature > 0.0):
    if not ((light < 0.01) and (temperature > 0.0)):
        turn_camera_on()