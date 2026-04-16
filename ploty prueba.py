import pandas as pd
import plotly.express as px
import requests

#pip install ipykernel

# 1. Obtener los datos (Feed de las últimas 24 horas para todos los terremotos)
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
data = requests.get(url).json()

# 2. Extraer la información relevante a una lista
# El formato GeoJSON guarda los datos en 'features'
quakes = []
for feature in data['features']:
    coords = feature['geometry']['coordinates']
    prop = feature['properties']
    quakes.append({
        'Magnitud': prop['mag'],
        'Lugar': prop['place'],
        'Longitud': coords[0],
        'Latitud': coords[1]
    })

# 3. Convertir a un DataFrame de Pandas para Plotly
df = pd.DataFrame(quakes)
# 
# 4. Crear el mapa interactivo
fig = px.scatter_mapbox(
    df, 
    lat="Latitud", 
    lon="Longitud", 
    size="Magnitud",         # El punto es más grande si el sismo fue fuerte
    color="Magnitud",        # Cambia el color según la intensidad
    hover_name="Lugar",      # Muestra el nombre al pasar el mouse
    zoom=1, 
    mapbox_style="carto-positron",
    title="Terremotos en el Mundo - Últimas 24 Horas"
)

fig.show()
