import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

title = all_eq_data['metadata']['title']
all_eq_dicts = all_eq_data['features']

mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]
hover_texts = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Jet',
        'reversescale': False,
        'colorbar': {'title': 'Magnitude'}
    },
}]
my_layout = Layout(title=title, title_x=0.5)


fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=f'{title}.html')
