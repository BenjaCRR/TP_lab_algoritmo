# TP_lab_algoritmo

Estos son las librerías que deberás instalar para poder correr correctamente el programa.

import pandas	,En consola: pip install pandas,	    Manejo de tablas de datos.
import plotly	,En consola: pip install plotly,	    Crear el mapa interactivo.
import requests	,En consola: pip install requests,	    Descargar los datos de internet.
import webview	,En consola: pip install pywebview,     Crear la ventana de aplicación.

bitácora:
08/04
Esta fué la primera clase, fue una clase donde me dediqué a investigar sobre cada trabajo, ver lo que se requería hacer para cada uno, evaluando la complejidad técnica y el alcance de cada una.
09/04
Continué con mi investigación, me decanté por iniciar el trabajo práctico N°3, el mapa del planeta donde se representen los últimos terremotos que ocurrieron en las últimas 24hs. Para eso, empecé a ver las librerías que iba a necesitar y buscar el json de información de los terremotos con sus respectivos datos. 
15/04
Importé Pandas, webview, ploty, request y tkinter
Continué aprendiendo sobre estas librerías, pude ver como crear el mapa y representar los terremotos en el propio mapa, pero no me había centrado en lo "lindo". Tenía un recuadro no convencional y los colores de la escala eran solamente para tenerlos.
16/04
Día tranquilo, realicé pruebas de manejo de excepciones para prevenir errores en caso de que la API de la USGS no responda o devuelva valores nulos, garantizando la estabilidad del programa. Investigando las capacidades de la librería webview y las limitantes de renderizado de HTML viendo opciones pero sin llegar a un resultado.
22/04
Último día, dediqué mas trabajo a lo visual, cambíe el estilo del mapa que no había podido hacer la clase pasada, cambiandolo a carto-darkmatter, la escala de color la cambie también, pude hacer el recuadro negro también para evitar un contraste con el mapa, puse título y pude hacer algo que no sé porqué no había hecho antes, pude lograr que la rueda funcionara para hacer zoom al mapa, aclaré esto debajo del mapa junto a un pequeño texto que tambien aclara la escala de colores.
