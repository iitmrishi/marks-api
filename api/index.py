import json
from urllib.parse import parse_qs

def handler(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"

    query = parse_qs(request.query_string)
    names = query.get("name", [])

    # Load JSON data
    with open("marks.json") as f:
        marks_data = json.load(f)

    # Look up requested names
    result = [marks_data.get(name, None) for name in names]

    return response.json({"marks": result})
