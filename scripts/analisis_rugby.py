# ============================================
# Análisis de Resultados - Partido de Rugby
# Equipo: Lucio (Hugo + Paco) | Lucia (Luis)
# ============================================
#Versión 2
# -- DATOS DEL PARTIDO --

# Tries
tries_conv_local = 4
tries_conv_visita = 3
tries_noconv_local = 1
tries_noconv_visita = 2

# Formaciones fijas - Scrum
scrums_ganados_local = 7
scrums_ganados_visita = 5
scrums_perdidos_local = 3
scrums_perdidos_visita = 5

# Formaciones fijas - Kickoff
kickoff_ganados_local = 5
kickoff_ganados_visita = 4
kickoff_perdidos_local = 3
kickoff_perdidos_visita = 4

# Formaciones fijas - Line
line_ganados_local = 8
line_ganados_visita = 6
line_perdidos_local = 2
line_perdidos_visita = 4

# Infracciones
penales_conv_local = 3
penales_conv_visita = 2
penales_errados_local = 1
penales_errados_visita = 2
freekick_local = 2
freekick_visita = 1

# -- MOSTRAR RESULTADOS --

print("=========================================")
print("   RESULTADOS DEL PARTIDO DE RUGBY")
print("=========================================")

print("\n=== TRIES ===")
print("Tries convertidos    -> Local:", tries_conv_local,   "| Visitante:", tries_conv_visita)
print("Tries no convertidos -> Local:", tries_noconv_local, "| Visitante:", tries_noconv_visita)

print("\n=== FORMACIONES FIJAS - SCRUM ===")
print("Scrums ganados       -> Local:", scrums_ganados_local,  "| Visitante:", scrums_ganados_visita)
print("Scrums perdidos      -> Local:", scrums_perdidos_local, "| Visitante:", scrums_perdidos_visita)

print("\n=== FORMACIONES FIJAS - KICKOFF ===")
print("Kickoff ganados      -> Local:", kickoff_ganados_local,  "| Visitante:", kickoff_ganados_visita)
print("Kickoff perdidos     -> Local:", kickoff_perdidos_local, "| Visit
