import requests
from bs4 import BeautifulSoup
from slugify import slugify  # Import the slugify function from the python-slugify module
import json
import numpy as np

def greet(name):
    return "Hello, " + str(name) + "!"

url_count = 0

url = 'https://www.semanticscholar.org/api/1/search/paper/e3ea7015f69118d3ee9c2730f91dbdef1297f9de/citations'  # Replace with your actual API endpoint
params = {
    'authors': [],
    'citationType': 'citingPapers',
    'coAuthors': [],
    'cues': ["CitedByLibraryPaperCue", "CitesYourPaperCue", "CitesLibraryPaperCue"],
    'fieldsOfStudy': [],
    'includePdfVisibility': True,
    'page': 1,
    'pageSize': 1000,
    'requireViewablePdf': False,
    'sort': 'relevance',
    'venues': [],
    'yearFilter': None
}

response = requests.post(url, json=params)
soup = BeautifulSoup(response.content, 'html.parser')

# Save the response to a text file
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

python_object = json.loads(soup.prettify())
python_object['results'][0]['slug']

url = []
num_each_citations = len(python_object['results'])
for count in range(num_each_citations - 1):
    url.append("https://www.semanticscholar.org/paper/" + python_object['results'][count]['slug'] + "/" + python_object['results'][count]['id'])

url_count = url_count + 1


with open('output.txt', 'w', encoding='utf-8') as file:
    np.savetxt(file, url, fmt='%s')


# for item in result_data:
#     title = item.get('title', '')  # Replace 'title' with the actual field name
#     category = item.get('category', '')  # Replace 'category' with the actual field name
# if title and category:
#     combined_fields = f"{title} {category}"  # Combine the two fields
#     slug = slugify(combined_fields)  # Generate a slug from the combined fields using slugify
#     print(slug)  # Output the generated slug