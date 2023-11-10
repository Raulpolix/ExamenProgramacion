# Datos de temperatura para cada semana
temperatures = [[22, 24, 19, 21, 25, 23, 20],
                [20, 22, 21, 23, 24, 22, 21],
                [23, 21, 20, 22, 24, 25, 23]]

# Función que calcula la temperatura media de la semana
def temp_media(temp_semana):
    return sum(temp_semana) / len(temp_semana)

# Función que encuentra el día más caluroso de la semana
def dia_caluroso(temp_semana):
    maximo = max(temp_semana)
    dia_calor = temp_semana.index(maximo) + 1
    return dia_calor

# Función que dice si alguna semana ha estado entre 20 y 25 grados
def consistently_mill(temp_semana):
    return any(20 <= temp <= 25 for temp in temp_semana)

# Función que crea una lista de la variación día a día de la temperatura
def variacion_sem(temp_semana):
    cambios = [temp_semana[i] - temp_semana[i - 1] for i in range(1, len(temp_semana))]
    return cambios

# Calcular la media histórica de temperaturas
media_historica = [temp_media(semana) for semana in temperatures]

# Función que crea una lista de diferencias respecto a la media histórica
def diferencias_mh(temp_semana, media_semanal):
    diferencias = [temp - media_semanal for temp in temp_semana]
    return diferencias

# Calcular y mostrar los resultados
for semana, (temp_semana, media_smanal) in enumerate(zip(temperatures, media_historica), start=1):
    media = temp_media(temp_semana)
    dia_calor = dia_caluroso(temp_semana)
    temp_canario = consistently_mill(temp_semana)
    cambios = variacion_sem(temp_semana)
    diferencias_mh_semana = diferencias_mh(temp_semana, media_smanal)

    print(f"\nResultados para la Semana {semana}:")
    print(f"Temperatura Media: {media:.2f} grados")
    print(f"Día más caluroso: Día {dia_calor}")
    print(f"¿Estuvo en un clima similar al canario? (20/25 grados): {'Sí' if temp_canario else 'No'}")
    print(f"Variación de la temperatura a lo largo de la semana: {cambios}")
    print(f"Diferencias respecto a la media histórica: {diferencias_mh_semana}")
