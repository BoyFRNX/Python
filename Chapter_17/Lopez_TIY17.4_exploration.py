import requests
from plotly import offline


# Make an API call and store the response.
language = 'python'
url = f'https://api.github.com/search/repositories?q=language:{language}&sort=forks'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']

# Get number of forks, urls, descriptions, owners and names of repositories.
forks, urls, links, repo_names, labels = [], [], [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    links.append(repo_link)
    forks.append(repo_dict['forks'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# Make a visualization.
data = [{
    'type': 'bar',
    'x': links,
    'y': forks,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]

my_layout = {
    'title': 'Most-Forked Python Projects on Github',
    'title_x': 0.5,
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 10},
    },
    'yaxis': {
        'title': 'Forks',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')

