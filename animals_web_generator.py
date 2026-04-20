import json

FILE_PATH = "animals_data.json"

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data(FILE_PATH)
for data in animals_data:
    try:
        if (data['name'] and data['characteristics']['diet']
                and data['locations'][0] and data['characteristics']['type']):
            print(f"Name: {data['name']}\n"
                  f"Diet: {data['characteristics']['diet']}\n"
                  f"Location: {data['locations'][0]}\n"
                  f"Type: {data['characteristics']['type']}")
            print()
    except KeyError:
        continue
