import json

FILE_PATH = "animals_data.json"
HTML_FILE_PATH = "animals_template.html"


def load_data(file_path):
    """
        Loads animal data from a specified JSON file.

        Args:
            file_path (str): The path to the JSON file to be read.

        Returns:
            list[dict]: A list of dictionaries where each dictionary represents
            an animal and its associated attributes.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """
    Convert an animal dictionary into an HTML list item.

    The function extracts relevant fields from the input dictionary and
    formats them into a structured HTML snippet.

    Args:
        animal_obj (dict): A dictionary containing animal information.
            Expected keys include:
                - "name" (str)
                - "characteristics" (dict) with keys:
                    "diet", "type", "skin_type", "lifespan"
                - "locations" (list[str])

    Returns:
        str: A string containing the formatted HTML representation
        of the animal.
    """
    html_part = '<li class="cards__item"><strong>title: </strong>content</li>'
    title_open_tag, title_closing_tag = html_part.split('title')
    content_open_tag, content_closing_tag = title_closing_tag.split('content')
    contents = {"Diet": animal_obj["characteristics"]["diet"],
                "Location": animal_obj["locations"][0],
                "Type": animal_obj["characteristics"]["type"],
                "Skin Type": animal_obj["characteristics"]["skin_type"],
                "Life expectancy": animal_obj["characteristics"]["lifespan"]}
    serialized_contents = [
        title_open_tag + title + content_open_tag + content +
        content_closing_tag
        for title, content in contents.items()]
    animal_detail = '\n'.join(serialized_contents)

    parts = [
        '<li class="cards__item">',
        f'<div class="card__title">{animal_obj["name"]}</div>',
        '<div class="card__text">',
        '<ul class="cards">',
        animal_detail,
        '</ul>',
        '</div>',
        '</li>',
    ]

    return ''.join(parts)


def write_html_file(result):
    """
        Generate an HTML file with the provided animal data.

        This function reads an HTML template file, replaces a placeholder
        string with the given content, and writes the result to a new file.

        Args:
            result (str): HTML string containing serialized animal data
            to insert into the template.
    """
    with open(HTML_FILE_PATH, "r") as read_file:
        read_html = read_file.read().replace("__REPLACE_ANIMALS_INFO__",
                                             result)

    with open("animals.html", "w") as write_file:
        write_file.write(read_html)


def filter_by_skin_type(animals_list, skin_type):
    """
       Filter animals by skin type and serialize them to HTML.

       The function validates required fields before including an animal
       in the output and ensures case-insensitive matching by normalizing
       the input skin type.

       Args:
           animals_list (list[dict]): List of animal dictionaries.
           skin_type (str): Skin type to filter by (e.g., "fur", "scales").

       Returns:
           list[str]: A list of HTML strings representing matching animals.
           If no animals match the criteria, a fallback HTML message is
           returned.
    """
    output = []
    for animal in animals_list:
        if (
                animal.get("characteristics", {}).get(
                    "skin_type") == skin_type.capitalize()
                and animal.get("name")
                and animal.get("characteristics", {}).get("diet")
                and animal.get("locations")
                and animal.get("locations")[0]
                and animal.get("characteristics", {}).get("type")
        ):
            output.append(serialize_animal(animal))

    if not output:
        return ['<div>Don\'t have that animal detail</div>']
    return output


def main():
    """
        Execute the main program workflow.

        Steps:
            1. Load animal data from a JSON file.
            2. Display available skin types.
            3. Prompt the user to input a skin type.
            4. Filter animals based on the selected skin type.
            5. Generate an HTML file with the filtered results.
    """
    animals_data = load_data(FILE_PATH)
    types_of_skin = set(
        [animal["characteristics"]["skin_type"] for animal in animals_data])
    print("Types of Skin Types")
    print('\n'.join(types_of_skin))
    skin_type = input("Enter Skin Type: ")
    output = filter_by_skin_type(animals_data, skin_type)
    write_html_file('\n'.join(output))


if __name__ == "__main__":
    main()
