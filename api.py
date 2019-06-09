"""Playing around with WWC API."""
import json
from types import SimpleNamespace

import requests

API_URL_BASE = "https://www.worldwide-combos.com/api"


def get_sprint_rankings(count, start=None):
    """Get sprint rankings from WWC API."""
    sprint_rankings_url = f"{API_URL_BASE}/rankings?type=sprint&count={count}"
    if start:
        sprint_rankings_url = sprint_rankings_url + f"&start={start}"
    response = requests.get(sprint_rankings_url)

    if response.status_code == 200:
        return json.loads(
            response.content.decode("utf-8"), object_hook=lambda d: SimpleNamespace(**d)
        )
    # maybe should throw an exception?
    return None


if __name__ == "__main__":
    print(get_sprint_rankings(5, 2))
