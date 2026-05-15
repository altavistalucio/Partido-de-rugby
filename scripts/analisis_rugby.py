import pandas as pd
import matplotlib.pyplot as plt
import os

# Carga del dataset desde la carpeta /datos
df = pd.read_csv('../datos/resultados_rugby.csv')

print("Dataset cargado correctamente")
print(f"Cantidad de partidos: {len(df)}
")

# Partidos ganados por equipo
equipos = ['Los Pumas RC', 'Tigres Rugby', 'Cóndores RC', 'Dragones RC']

ganados      = {e: 0 for e in equipos}
perdidos     = {e: 0 for e in equipos}
puntos_favor = {e: 0 for e in equipos}

for _, fila in df.iterrows():
    local     = fila['equipo_local']
    visitante = fila['equipo_visitante']
    pts_l     = fila['puntos_local']
    pts_v     = fila['puntos_visitante']

    puntos_favor[local]     += pts_l
    puntos_favor[visitante] += pts_v

    if pts_l > pts_v:
        ganados[local]      += 1
        perdidos[visitante] += 1
    else:
        ganados[visitante]  += 1
        perdidos[local]     += 1

print("=== Partidos ganados por equipo ===")
for e in equipos:
    print(f"  {e}: {ganados[e]} ganados / {perdidos[e]} perdidos")

# Tabla de posiciones
tabla = pd.DataFrame({
    'Equipo':         equipos,
    'Ganados':        [ganados[e]      for e in equipos],
    'Perdidos':       [perdidos[e]     for e in equipos],
    'Puntos a favor': [puntos_favor[e] for e in equipos]
})
tabla = tabla.sort_values('Ganados', ascending=False).reset_index(drop=True)
tabla.index += 1

print("
=== Tabla de posiciones ===")
print(tabla.to_string())

# Promedio de puntos por partido
print("
=== Promedio de puntos por partido ===")
for e in equipos:
    print(f"  {e}: {puntos_favor[e] / 6:.1f} puntos/partido")

# Gráfico
nombres   = tabla['Equipo'].tolist()
victorias = tabla['Ganados'].tolist()
colores   = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

plt.figure(figsize=(8, 5))
plt.bar(nombres, victorias, color=colores)
plt.title('Partidos ganados por equipo – Torneo de Rugby 2026')
plt.ylabel('Victorias')
plt.xlabel('Equipo')
for i, v in enumerate(victorias):
    plt.text(i, v + 0.05, str(v), ha='center', fontweight='bold')
plt.tight_layout()

# Guardar resultados
os.makedirs('../resultados', exist_ok=True)
plt.savefig('../resultados/grafico_rendimiento.png', dpi=150)
tabla.to_csv('../resultados/tabla_posiciones.csv')

print("
Gráfico y tabla guardados en /resultados")
print("¡Análisis finalizado!")