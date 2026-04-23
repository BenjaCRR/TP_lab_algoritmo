import pandas as pd
import plotly.express as px
import requests # Pide info a una página web o API (en este caso al USGS)

import webview # Crea la ventana tipo app para ver el mapa
import os # Sirve para borrar el archivo temporal al final

# 1. Traer los datos de terremotos del USGS (datos de las últimas 24h)
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
data = requests.get(url).json() # Descarga el JSON y lo convierte en un diccionario

# Filtrar lo que nos sirve
quakes = []
for feature in data['features']:
    coords = feature['geometry']['coordinates'] # Saca las coordenadas [long, lat, prof]
    prop = feature['properties'] # Saca info como magnitud y lugar
    
    # Solo guardamos si tiene magnitud real
    if prop['mag'] is not None and prop['mag'] > 0:
        quakes.append({
            'Magnitud': prop['mag'], # q tan fuerte fue
            'Lugar': prop['place'], # Zona pais
            'Longitud': coords[0], # Eje X en el mapa
            'Latitud': coords[1]   # Eje Y en el mapa
        })

# Metemos la lista en una tabla DataFram para que Plotly la entienda fácil
df = pd.DataFrame(quakes)

#  Configurar el mapa con Plotly
fig = px.scatter_mapbox(
    df, lat="Latitud", lon="Longitud", size="Magnitud", # El tamaño del punto depende de la magnitud
    color="Magnitud", hover_name="Lugar", zoom=1, # El color también cambia según la fuerza
    mapbox_style="carto-darkmatter", # Estilo de mapa SIN TOKENSITO
    title="Terremotos - Últimas 24 Horas",
    color_continuous_scale="OrRd" # colores
)

#visual
fig.update_layout(
    margin={"r":0,"t":50,"l":0,"b":50}, # t:40 deja espacio solo para el título
    paper_bgcolor="black", # Fondo de la "ventana" en negro
    plot_bgcolor="black",
    font_color="white", # Letras blancas para que resalten
    title={
        'text': "MONITOR DE ACTIVIDAD SÍSMICA GLOBAL",
        'y':0.95, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top' # Centra el título
    },
    annotations=[{
        'text': "Usa la rueda del ratón para hacer Zoom • Los puntos más grandes y rojos indican mayor magnitud",
        'showarrow': False,
        'xref': "paper", 'yref': "paper",
        'x': 0.5, 'y': -0.06, # Posición abajo del mapa
        'font': {'size': 12, 'color': "gray"}
    }]
)

# 3. Guardar el mapa como un archivo HTML temporal
archivo_html = "Terremotos.html"
fig.write_html(archivo_html, config={'displayModeBar': False,'scrollZoom': True })

# Esto abre una ventana propia de Windows
webview.create_window('Visor de Terremotos', archivo_html, width=1000, height=740)
webview.start()

#borro todo cuando lo dejo de usar
if os.path.exists(archivo_html):
    os.remove(archivo_html)
