from flask import Flask

import folium

app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (46.9540700, 142.7360300)
    folium_map = make_folium_map()
    return folium_map._repr_html_()


def make_folium_map():
    m = folium.Map(location = [-6.200000, 106.816666],
                zoom_start = 6,
                control_scale = True)

    # Atur marker (pin atau node) dan tooltip
    tooltip = "Klik!"

    folium.Marker(
        [-6.200000, 106.816666], popup="<b>Jakarta</b><br/>Ibu Kota Indonesia", tooltip=tooltip, icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

    folium.Marker(
        [-7.250445, 112.768845], popup="<b>Surabaya</b><br/>Terkenal akan sumuknya", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [-6.914864, 107.608238], popup="<b>Bandung</b><br/>Kota yang sejuk tapi (mulai) macet", tooltip=tooltip
    ).add_to(m)

    # Atur line (edge)

    # Menghubungkan JKT-BDG
    loc = [(-6.200000, 106.816666),
        (-6.914864, 107.608238)]

    folium.PolyLine(loc,
                    color = 'red',
                    weight = 8,
                    opacity = 0.8).add_to(m)

    # Menghubungkan BDG-TML
    loc = [(-6.914864, 107.608238),
        (-7.319563, 108.202972)]

    folium.PolyLine(loc,
                    color = 'blue',
                    weight = 5,
                    opacity = 0.8).add_to(m)

    # Menghubungkan JKT-SBY
    loc = [(-6.200000, 106.816666),
        (-7.250445, 112.768845)]

    folium.PolyLine(loc,
                    color = 'green',
                    weight = 2,
                    opacity = 0.8).add_to(m)
    
    return m

if __name__ == '__main__':
    app.run(port=8000, debug=True)