import requests
import json

query = {
    "query": "$GQLID{1f253903307a64977622dc155bd1dae5}",
    "variables": {
        "wizardInput": {
            "projectId": "vr",
            "pserviceId": 102,
            "answers": [],
            "profileIds": [],
            "wizardSession": "b4efec08-25d9-438c-85ce-5326d340"
        },
        "wizardSessionId": "b4efec08-25d9-438c-85ce-5326d340", "pageType": "order.seamless", "geoCityId": "kzn",
        "searchFilter": {"p": 1, "sort": "SEAMLESS"},
        "photoWidth": 1500
    }
}

headers = {
    "Content-Type": "application/json",
    "User-Agent": "PostmanRuntime/7.23.0",
    "Accept": "application/json",
    "Cache-Control": "no-cache",
    "Postman-Token": "45ec624f-4db2-479c-b834-0529cad0b4fc",
    "Host": "kzn.profi.ru",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Length": "354",
    "Connection": "keep-alive",
}

# api works

r = requests.get('https://kzn.profi.ru/graphql/?gqlid=%24GQLID%7B1f253903307a64977622dc155bd1dae5%7D', json=query,
                 headers=headers)

text_file = open("profi_api_data.json", "w")
json_data = json.dumps(r.text, ensure_ascii=False)
text_file.write(json_data)
text_file.close()
