from plotly.graph_objs import Scatter, Layout
from plotly import offline
from random_walk import RandomWalk


# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

trace = Scatter(x=rw.x_values, y=rw.y_values, mode='markers')

data = [trace]
x_axis_config = {'title': ''}
y_axis_config = {'title': ''}
my_layout = Layout(title='Random Walk',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='random_walk.html')
