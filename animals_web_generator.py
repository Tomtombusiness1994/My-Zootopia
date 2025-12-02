import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')
output = ''
animal_html = ''

output += '<ul class="cards">'
for animal in animals_data:
    output += '<li class="cards__item">'
    output += f"Name: {animal['name']}<br/>"
    output += f"Diet: {animal['characteristics']['diet']}<br/>"
    output += f"Location: {animal['locations'][0]}<br/>"
    if "type" in animal["characteristics"]:
        output += f"Type: {animal['characteristics']["type"]}<br/>"
    output += '</li>'
output += '</ul>'

with open('animals_template.html', "r") as handle:
    animal_html = handle.read()

with open('animals.html', "w") as handle:
    handle.write(animal_html.replace("__REPLACE_ANIMALS_INFO__", output))