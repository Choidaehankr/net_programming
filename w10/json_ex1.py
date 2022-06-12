import json

with open('ex.json', 'r') as f:
    data = f.read()
    json_data = json.loads(data)
    print(type(json_data))
    print(json_data)
    print(json_data['champion'])
    print(json_data['champion'][0]['name'],
            json_data['champion'][1]['skin'])