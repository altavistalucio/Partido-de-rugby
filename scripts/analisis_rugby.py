# =========================================
# Analisis de Resultados - Partido de Rugby
# Escenario D - Estadisticas Deportivas
# Trabajo Practico - TUP
# =========================================

# -- DATOS DEL PARTIDO --
# acá cargamos todos los datos del partido manualmente

# Tries (un try convertido vale 7 puntos, no convertido vale 5)
tries_conv_local = 4
tries_conv_visita = 3
tries_noconv_local = 1
tries_noconv_visita = 2

# Scrums (formacion fija donde empujan los forwards)
scrums_ganados_local = 7
scrums_ganados_visita = 5
scrums_perdidos_local = 3
scrums_perdidos_visita = 5

# Kickoff (patadas al inicio y reinicio del juego)
kickoff_ganados_local = 5
kickoff_ganados_visita = 4
kickoff_perdidos_local = 3
kickoff_perdidos_visita = 4

# -- CALCULOS --
# calculamos los puntos totales de cada equipo
puntos_local = (tries_conv_local * 7) + (tries_noconv_local * 5)
puntos_visita = (tries_conv_visita * 7) + (tries_noconv_visita * 5)

# -- MOSTRAMOS LOS RESULTADOS --
print("========================================")
print("   RESULTADOS DEL PARTIDO DE RUGBY")
print("========================================")

# mostramos quien gano
if puntos_local > puntos_visita:
    print("Ganador: LOCAL con", puntos_local, "puntos")
elif puntos_visita > puntos_local:
    print("Ganador: VISITA con", puntos_visita, "puntos")
else:
    print("Resultado: EMPATE")

print("\n=== TRIES ===")
print("Tries convertidos    -> Local:", tries_conv_local, "| Visitante:", tries_conv_visita)
print("Tries no convertidos -> Local:", tries_noconv_local, "| Visitante:", tries_noconv_visita)

print("\n=== FORMACIONES FIJAS - SCRUM ===")
print("Scrums ganados  -> Local:", scrums_ganados_local, "| Visitante:", scrums_ganados_visita)
print("Scrums perdidos -> Local:", scrums_perdidos_local, "| Visitante:", scrums_perdidos_visita)

print("\n=== FORMACIONES FIJAS - KICKOFF ===")
print("Kickoff ganados  -> Local:", kickoff_ganados_local, "| Visitante:", kickoff_ganados_visita)
print("Kickoff perdidos -> Local:", kickoff_perdidos_local, "| Visitante:", kickoff_perdidos_visita)
