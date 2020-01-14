import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Explore the structure of the data.
filename = 'data/world_fires_24_hr.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Automate indexes.
    lon_index = ''
    lat_index = ''
    bright_index = ''
    for index, column_value in enumerate(header_row):
        if column_value == 'longitude':
            lon_index = index
        elif column_value == 'latitude':
            lat_index = index
        elif column_value == 'brightness':
            bright_index = index

    # Get longitude, latitude, and brightness data.
    lons, lats, brights = [], [], []
    for row in reader:
        current_date = row[5]
        try:
            lon = float(row[lon_index])
            lat = float(row[lat_index])
            bright = float(row[bright_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            lons.append(lon)
            lats.append(lat)
            brights.append(bright)

# Map the fires.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [(1/20)*bright for bright in brights],
        'color': brights,
        'opacity': 0.5,
        'colorscale': 'Hot',
        'reversescale': False,
        'colorbar': {'title': 'Brightness'}
    },
}]

title = 'Global Fires - 24HR'
my_layout = Layout(title=title, title_x=0.5)


fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=f'{title}.html')
