import json

FILE_PATH = "animals_data.json"
HTML_FILE_PATH = "animals_template.html"

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def serialize_animal(animal_obj):
    output = ''
    output += f'<li class="cards__item">'
    output += f'<div class="card__title">{animal_obj['name']}</div>'
    output += f'<div class="card__text">'
    output += f'<ul class="cards">'
    output += f'<li class="cards__item"><strong>Diet:</strong> {animal_obj['characteristics']['diet']}</li>\n'
    output += f'<li class="cards__item"><strong>Location:</strong> {animal_obj['locations'][0]}</li>\n'
    output += f'<li class="cards__item"><strong>Type:</strong> {animal_obj['characteristics']['type']}</li>\n'
    output += f'<li class="cards__item"><strong>Life expectancy:</strong> {animal_obj['characteristics']['lifespan']}</li>\n'
    output += f'</ul>'
    output += f'</div>'
    output += f'</li>'
    return output


def main():
    animals_data = load_data(FILE_PATH)
    output = ''
    for data in animals_data:
        try:
            if (data['name'] and data['characteristics']['diet']
                    and data['locations'][0] and data['characteristics']['type']):
                output += serialize_animal(data)
        except KeyError:
            continue

    with open(HTML_FILE_PATH, "r") as read_file:
        read_html = read_file.read().replace("__REPLACE_ANIMALS_INFO__",
                                             output)

    with open("animals.html", "w") as write_file:
        write_file.write(read_html)


if __name__ == "__main__":
    main()