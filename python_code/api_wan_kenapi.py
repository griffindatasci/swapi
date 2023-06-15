# Scrape data from the swapi api ========================================
# - it will perform this for a single given resource (e.g. planets, starships ..)
# - it will output as a json unless the file exists OR overwrite=True

# Example usage 1:
# planets = api_wan("planets")

# Example usage 2:
# starships = api_wan("starships")
# for starship in starships:
#     print(starship["name"])
# =======================================================================
import json
from math import ceil
from pathlib import Path
import requests


def api_wan(resource, overwrite=False):
    path = Path(f"{resource}.json")
    if not path.is_file() or overwrite:
        print(f"Scraping {resource}...")

        # Get number of pages to scrape (ensures all data is scraped with minimal requests)
        api_return = requests.get(f"https://swapi.dev/api/{resource}", timeout=90)
        api_json = api_return.json()
        n_pages = ceil(api_json["count"]/len(api_json["results"]))
        resource_list = [item for item in api_json["results"]]

        # Scrape data from each (remaining) page
        if n_pages>1:
            for page in range(2, n_pages+1):
                print(f"Scraping {resource} page {page} of {n_pages}")
                api_return = requests.get(
                    f"https://swapi.dev/api/{resource}/?page={page}", timeout=90)
                api_json = api_return.json()
                resource_list = resource_list + [item for item in api_json["results"]]

            resource_json = json.dumps(resource_list)
            Path(f"{resource}.json").write_text(resource_json, encoding="UTF8")
            print(f"Saved data to {resource}.json")
        else:
            print(f"Loaded from existing {resource}.json file!")
        
    data = path.read_text(encoding="UTF8")
    output = json.loads(data)
    return output

