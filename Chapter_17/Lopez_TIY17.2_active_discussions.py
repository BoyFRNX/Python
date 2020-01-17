import requests
from operator import itemgetter
from plotly import offline


# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Make lists for titles, comments, and links.
titles = [submission_dict['title'] for submission_dict in submission_dicts]
comments = [submission_dict['comments'] for submission_dict in submission_dicts]
links = [submission_dict['hn_link'] for submission_dict in submission_dicts]
link_formatted = [f"<a href='{link}'>{title}</a>" for link in links for title in titles]

# Make a visualization.
data = [{
    'type': 'bar',
    'x': link_formatted,
    'y': comments,
    'hovertext': titles,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]

my_layout = {
    'title': f'Most Active Discussions on Hacker News',
    'title_x': 0.5,
    'xaxis': {
        'title': 'Article Title',
        'titlefont': {'size': 24},
        'tickfont': {'size': 10},
        'tickangle': 35
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
