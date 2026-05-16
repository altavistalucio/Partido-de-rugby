
# Estas tres líneas traen herramientas externas que no vienen con Python
# Es como instalar una app: la descargás una vez y después la usás
# pandas  → nos deja trabajar con tablas (filas y columnas), como Excel
# pyplot  → nos deja hacer gráficos de barras, tortas, etc.
# os      → nos deja hablar con el sistema operativo (crear carpetas, etc.)
import pandas as pd
import matplotlib.pyplot as plt
import os

# pd.read_csv() lee un archivo .csv y lo convierte en una tabla (DataFrame)
# Usamos '../datos/' porque el script está en /scripts/ y el archivo en /datos/
# El '..' significa "subir una carpeta"
df = pd.read_csv('../datos/resultados_rugby.csv')

print("Dataset cargado correctamente")
print(f"Cantidad de partidos: {len(df)}\n")

# Lista con los 4 equipos — esto sí lo conocemos, es una lista normal
equipos = ['Los Pumas RC', 'Tigres Rugby', 'Cóndores RC', 'Dragones RC']

# Tres diccionarios para guardar los resultados de cada equipo
# La clave es el nombre del equipo y el valor arranca en 0
ganados      = {e: 0 for e in equipos}
perdidos     = {e: 0 for e in equipos}
puntos_favor = {e: 0 for e in equipos}

# df.iterrows() recorre el DataFrame fila por fila
# Es como un for normal, pero en vez de recorrer una lista,
# recorre cada partido del archivo CSV
for _, fila in df.iterrows():
    local     = fila['equipo_local']
    visitante = fila['equipo_visitante']
    pts_l     = fila['puntos_local']
    pts_v     = fila['puntos_visitante']

    # Sumamos los puntos de este partido al total de cada equipo
    # += es lo mismo que: puntos_favor[local] = puntos_favor[local] + pts_l
    puntos_favor[local]     += pts_l
    puntos_favor[visitante] += pts_v

    # If/else que ya conocemos: el que hizo más puntos gana
    if pts_l > pts_v:
        ganados[local]      += 1
        perdidos[visitante] += 1
    else:
        ganados[visitante]  += 1
        perdidos[local]     += 1

print("=== Partidos ganados por equipo ===")
for e in equipos:
    print(f"  {e}: {ganados[e]} ganados / {perdidos[e]} perdidos")

# pd.DataFrame() convierte nuestros diccionarios en una tabla visual
tabla = pd.DataFrame({
    'Equipo':         equipos,
    'Ganados':        [ganados[e]      for e in equipos],
    'Perdidos':       [perdidos[e]     for e in equipos],
    'Puntos a favor': [puntos_favor[e] for e in equipos]
})

# sort_values ordena la tabla de mayor a menor victorias
tabla = tabla.sort_values('Ganados', ascending=False).reset_index(drop=True)

# Por defecto Python numera desde 0, pero en deportes se cuenta desde 1
tabla.index += 1

print("\n=== Tabla de posiciones ===")
print(tabla.to_string())

# Calculamos promedio dividiendo puntos totales por 6 partidos jugados
print("\n=== Promedio de puntos por partido ===")
for e in equipos:
    print(f"  {e}: {puntos_favor[e] / 6:.1f} puntos/partido")

# Sacamos los datos de la tabla para usarlos en el gráfico
# .tolist() convierte una columna del DataFrame en una lista normal
nombres   = tabla['Equipo'].tolist()
victorias = tabla['Ganados'].tolist()

# Un color diferente para cada equipo en el gráfico
colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# plt.figure crea el lienzo donde va el gráfico
plt.figure(figsize=(8, 5))
plt.bar(nombres, victorias, color=colores)
plt.title('Partidos ganados por equipo – Torneo de Rugby 2026')
plt.ylabel('Victorias')
plt.xlabel('Equipo')

# Este for agrega el número encima de cada barra para leerlo más fácil
for i, v in enumerate(victorias):
    plt.text(i, v + 0.05, str(v), ha='center', fontweight='bold')

plt.tight_layout()

# Creamos la carpeta /resultados/ si todavía no existe
os.makedirs('../resultados', exist_ok=True)

# Guardamos el gráfico como imagen y la tabla como CSV
plt.savefig('../resultados/grafico_rendimiento.png', dpi=150)
tabla.to_csv('../resultados/tabla_posiciones.csv')

print("\nGráfico y tabla guardados en /resultados")
print("¡Análisis finalizado!")
