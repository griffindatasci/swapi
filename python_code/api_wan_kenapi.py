# Scrape data from the swapi api ========================================
# - it will perform this for a single given resource (e.g. planets, starships ..)
import json
from math import ceil
import requests


def api_wan(resource, overwrite=False):

    # Get number of pages to scrape (ensures all data is scraped with minimal requests)
    api_return = requests.get(f"https://swapi.dev/api/{resource}", timeout=90)
    api_json = api_return.json()
    n_pages = ceil(api_json["count"]/len(api_json["results"]))
    resource_list = [item for item in api_json["results"]]

    # Scrape data from each (remaining) page
    if n_pages>1:
        for page in range(2, n_pages+1):
            api_return = requests.get(
                f"https://swapi.dev/api/{resource}/?page={page}", timeout=90)
            api_json = api_return.json()
            resource_list = resource_list + [item for item in api_json["results"]]

        #resource_json = json.dumps(resource_list)
        
    return resource_list
