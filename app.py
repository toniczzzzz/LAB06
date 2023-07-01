
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_info', methods=['POST'])
def get_info():

    pokemon_name = request.form['pokemon_name']
    pokemon_info = get_pokemon(pokemon_name)
    return render_template('result.html', pokemon_name=pokemon_name, pokemon_info=pokemon_info)


def get_pokemon(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}')
    if response.status_code == 200:
        pokemon_data = response.json()
        types = [t['type']['name'] for t in pokemon_data['types']]
        moves = [m['move']['name'] for m in pokemon_data['moves']]

        front_default = pokemon_data['sprites']['front_default']
        front_shiny = pokemon_data['sprites']['front_shiny']
        back_default = pokemon_data['sprites']['back_default']
        back_shiny = pokemon_data['sprites']['back_shiny']
  
        pokemon_info = {'types': types, 'moves': moves,'front_default': front_default,'front_shiny': front_shiny,'back_default': back_default,'back_shiny': back_shiny}
        return pokemon_info
    else:
        return None
    


if __name__ == '__main__':
    app.run(port=3000,debug=True)