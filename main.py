"""Playing around with WWC API."""
import json
import requests

API_URL_BASE = "https://www.worldwide-combos.com/api"


def get_sprint_rankings():
    """Get sprint rankings from WWC API."""
    sprint_rankings_endpoint = f"{API_URL_BASE}/rankings?type=sprint&count=5"
    response = requests.get(sprint_rankings_endpoint)

    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    # maybe should throw an exception?
    return None


if __name__ == "__main__":
    print(get_sprint_rankings())
