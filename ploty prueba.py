import pandas as pd
import plotly.express as px
import requests
import webview
import os
import tkinter as tk
from tkinter import messagebox

# --- FUNCIÓN PARA GENERAR EL MAPA ---
def generar_mapa(min_magnitud=0):
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
    try:
        data = requests.get(url).json()
        quakes = []
        for feature in data['features']:
            coords = feature['geometry']['coordinates']
            prop = feature['properties']
            # Filtramos por la magnitud elegida en el menú
            if prop['mag'] is not None and prop['mag'] >= min_magnitud:
                quakes.append({
                    'Magnitud': prop['mag'],
                    'Lugar': prop['place'],
                    'Longitud': coords[0],
                    'Latitud': coords[1]
                })

        if not quakes:
            messagebox.showinfo("Info", "No hay terremotos con esa magnitud en las últimas 24h.")
            return

        df = pd.DataFrame(quakes)
        fig = px.scatter_mapbox(
            df, lat="Latitud", lon="Longitud", size="Magnitud",
            color="Magnitud", hover_name="Lugar", zoom=1,
            mapbox_style="carto-positron",
            title=f"Terremotos >= {min_magnitud} (Últimas 24 Horas)"
        )

        archivo_html = "temp_mapa.html"
        fig.write_html(archivo_html)
        
        # Abrir visor
        ventana = webview.create_window('Visor de Terremotos', archivo_html, width=1000, height=700)
        webview.start()
        
        # Limpieza
        if os.path.exists(archivo_html):
            os.remove(archivo_html)
            
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar los datos: {e}")

# --- INTERFAZ DEL MENÚ (TKINTER) ---
def menu_principal():
    root = tk.Tk()
    root.title("Menú Sísmico")
    root.geometry("300x250")

    label = tk.Label(root, text="Seleccione una opción:", font=("Arial", 12, "bold"))
    label.pack(pady=10)

    # Botón 1: Ver todos
    btn_todos = tk.Button(root, text="Ver todos los sismos", width=25, 
                          command=lambda: generar_mapa(0))
    btn_todos.pack(pady=5)

    # Botón 2: Solo sismos fuertes
    btn_fuertes = tk.Button(root, text="Sismos Magnitud > 4.5", width=25, 
                            command=lambda: generar_mapa(4.5), fg="red")
    btn_fuertes.pack(pady=5)

    # Botón 3: Salir
    btn_salir = tk.Button(root, text="Salir", width=25, command=root.destroy)
    btn_salir.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    menu_principal()