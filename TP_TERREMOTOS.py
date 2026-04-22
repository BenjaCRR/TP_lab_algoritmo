import pandas as pd
import plotly.express as px
import requests
import tkinter
import webview # La librería para la ventana tipo "app"
import os

# 1. Obtener y procesar los datos (igual que tu código original)
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
data = requests.get(url).json()

quakes = []
for feature in data['features']:
    coords = feature['geometry']['coordinates']
    prop = feature['properties']
    if prop['mag'] is not None and prop['mag'] > 0:
        quakes.append({
            'Magnitud': prop['mag'],
            'Lugar': prop['place'],
            'Longitud': coords[0],
            'Latitud': coords[1]
        })

df = pd.DataFrame(quakes)

# 2. Crear el mapa
fig = px.scatter_mapbox(
    df, lat="Latitud", lon="Longitud", size="Magnitud",
    color="Magnitud", hover_name="Lugar", zoom=1,
    mapbox_style="carto-darkmatter",
    title="Terremotos - Últimas 24 Horas"
)

# 3. Guardar el mapa como un archivo HTML temporal
archivo_html = "Terremotos.html"
fig.write_html(archivo_html)

# 4. Abrir el archivo en una ventana de escritorio independiente
# Esto crea una ventana real en VS Code, no abre el navegador
webview.create_window('Visor de Terremotos', archivo_html, width=1000, height=700)
webview.start()

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}) ##no aseguro

# Opcional: Borrar el archivo temporal al cerrar
if os.path.exists(archivo_html):
    os.remove(archivo_html)
