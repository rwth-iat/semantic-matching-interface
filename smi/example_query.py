import requests
import json


if __name__ == '__main__':
    response = requests.get(
        "http://localhost:8000/semantic_query",
        data=json.dumps(
            {
                "query_parameters": [
                    {"attribute_name": "idShort", "attribute_value": "testProperty"}
                ]
            }
        )
    )
    print(response)
    print(json.dumps(json.loads(response.json()), indent=2))
