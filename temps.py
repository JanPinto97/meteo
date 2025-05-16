import requests
import json
from datetime import datetime

# Coordenades del poble/ciutat (exemple: Barcelona)
latitude = 41.3851
longitude = 2.1734

# Data actual
today = datetime.now().strftime("%Y-%m-%d")

# Consulta a l'API d'Open-Meteo
url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}"
    f"&hourly=temperature_2m&timezone=auto&start_date={today}&end_date={today}"
)

response = requests.get(url)
data = response.json()

# Obtenir les temperatures horàries del dia
temperatures = data['hourly']['temperature_2m']

# Calcular màxima, mínima i mitjana
temp_max = max(temperatures)
temp_min = min(temperatures)
temp_avg = sum(temperatures) / len(temperatures)

# Dades a exportar
resultat = {
    "data": today,
    "temperatura_maxima": temp_max,
    "temperatura_minima": temp_min,
    "temperatura_mitjana": round(temp_avg, 2)
}

# Guardar en un fitxer JSON
nom_fitxer = f"temp_{today.replace('-', '')}.json"
with open(nom_fitxer, 'w', encoding='utf-8') as f:
    json.dump(resultat, f, ensure_ascii=False, indent=4)

print(f"Dades guardades a {nom_fitxer}")
