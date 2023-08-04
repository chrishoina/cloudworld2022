import folium
from folium import Tooltip, JavascriptLink
from flask import Flask
from flask import render_template, Request
import requests

app = Flask(__name__)

m = folium.Map(location=[36.085645468598855, -115.08441257156686], zoom_start=10, min_zoom=10, tiles="Stamen Terrain")

tooltip = "Click me!"

@app.route('/')
def index(): 
    response = requests.get("https://yfuxkbz2ls7taze-ordshandsonlabs.adb.us-phoenix-1.oraclecloudapps.com/ords/python/flask/museums/").json()

    for museums in response['items']:
        try: 
            museum_id = museums['museum_id']
            museum_lat = museums['museum_lat']     
            museum_long = museums['museum_long']
            museum_name = museums['museum_name']

        except: 
            continue

        folium.Marker(
            location=[museum_lat, museum_long],
            popup=folium.Popup("<i>{}</i>".format(museum_name), max_width=450), icon=folium.Icon(color="lightred", icon="info-sign"),
            tooltip=tooltip
            ).add_to(m)
    
    lvmap = m._repr_html_()
        
    return render_template('index.html', lvmap=lvmap)

if __name__ == '__main__':
    app.run(debug=True)