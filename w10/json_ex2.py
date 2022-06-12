import json

dict_data = {
    'Name': 'Choi', "Department": 'IoT', "University": "Soonchunhyang"
}

with open('data.json', 'w') as f:
    json.dump(dict_data, f)