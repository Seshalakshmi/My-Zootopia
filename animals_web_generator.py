import json
from idlelib.replace import replace

FILE_PATH = "animals_data.json"
HTML_FILE_PATH = "animals_template.html"

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data(FILE_PATH)
output = ''
for data in animals_data:
    try:
        if (data['name'] and data['characteristics']['diet']
                and data['locations'][0] and data['characteristics']['type']):
            output += f'<li class="cards__item">'
            output += f'<p class="card__text">'
            output += f'<div class="card__title">{data['name']}</div><br>'
            output += f"<strong>Diet:</strong> {data['characteristics']['diet']}<br><br>\n"
            output += f"<strong>Location:</strong> {data['locations'][0]}<br><br>\n"
            output += f"<strong>Type:</strong> {data['characteristics']['type']}<br>\n"
            output += f'</p>'
            output += f'</li>'
    except KeyError:
        continue

with open(HTML_FILE_PATH, "r") as read_file:
    read_html = read_file.read().replace("__REPLACE_ANIMALS_INFO__",
                                         output)

with open("animals.html", "w") as write_file:
    write_file.write(read_html)