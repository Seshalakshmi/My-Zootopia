import json

FILE_PATH = "animals_data.json"
HTML_FILE_PATH = "animals_template.html"


def load_data(file_path):
    """
        Loads animal data from a specified JSON file.

        Args:
            file_path (str): The path to the JSON file to be read.

        Returns:
            list: A list of dictionaries containing animal information.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """
        Converts a single animal's data into an HTML list item string.

        Args:
            animal_obj (dict): A dictionary containing an animal's attributes
                (name, characteristics, locations).

        Returns:
            str: An HTML-formatted string representing the animal as a card.
    """
    output = ''
    output += f'<li class="cards__item">'
    output += f'<div class="card__title">{animal_obj['name']}</div>'
    output += f'<div class="card__text">'
    output += f'<ul class="cards">'
    output += (f'<li class="cards__item"><strong>Diet:</strong> '
               f'{animal_obj['characteristics']['diet']}</li>\n')
    output += (f'<li class="cards__item"><strong>Location'
               f':</strong> {animal_obj['locations'][0]}</li>\n')
    output += (f'<li class="cards__item"><strong>Type'
               f':</strong> {animal_obj['characteristics']['type']}</li>\n')
    output += (f'<li class="cards__item"><strong>Life expectancy'
               f':</strong> '
               f'{animal_obj['characteristics']['lifespan']}</li>\n')
    output += f'</ul>'
    output += f'</div>'
    output += f'</li>'
    return output


def write_html_file(result):
    """
        Reads the HTML template, replaces the animal info placeholder
        with the generated content, and saves the result to a new file.

        Args:
            result (str): The serialized HTML string containing animal data.
    """
    with open(HTML_FILE_PATH, "r") as read_file:
        read_html = read_file.read().replace("__REPLACE_ANIMALS_INFO__",
                                             result)

    with open("animals.html", "w") as write_file:
        write_file.write(read_html)


def main():
    """
        Executes the main application logic: loading data,
        filtering/serializing
        valid animal entries, and writing the final HTML output.
    """
    animals_data = load_data(FILE_PATH)
    output = ''
    for data in animals_data:
        try:
            if (data['name'] and data['characteristics']['diet']
                    and data['locations'][0] and data['characteristics'][
                        'type']):
                output += serialize_animal(data)
        except KeyError:
            continue
    write_html_file(output)


if __name__ == "__main__":
    main()
