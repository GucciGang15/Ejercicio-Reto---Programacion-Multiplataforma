from datetime import datetime

EDAD_JUBILACION = 60

def calcular_edad_exacta(fecha_nacimiento, hoy):
    cumplio_anios = (hoy.month, hoy.day) >= (fecha_nacimiento.month, fecha_nacimiento.day)
    edad = hoy.year - fecha_nacimiento.year
    if not cumplio_anios:
        edad -= 1
    return edad

def evaluar_estado_jubilacion(fecha_texto):
    try:
        fecha_nacimiento = datetime.strptime(fecha_texto, "%d/%m/%Y").date()
    except ValueError:
        return "Estructura de fecha no válida. Utilice el formato dd/mm/aaaa.", True

    hoy = datetime.now().date()

    if fecha_nacimiento > hoy:
        return "La fecha ingresada es posterior a la fecha actual.", True

    edad = calcular_edad_exacta(fecha_nacimiento, hoy)

    if edad >= EDAD_JUBILACION:
        mensaje = f"Cuenta con {edad} años. Ya debería pensar en jubilarse."
    else:
        faltantes = EDAD_JUBILACION - edad
        mensaje = f"Cuenta con {edad} años. Le restan {faltantes} años para el retiro laboral."

    return mensaje, False