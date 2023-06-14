import requests

pokemon_name = input('Qual nome do pokemon queres informacao?')
pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'.strip().lower())

pokedados = pokemon.json()

if 'height' in pokedados:
    converter_decimetros = pokedados['height'] / 10
    print (f"ID: {pokedados['id']}\n"
           f"Altura: {converter_decimetros} metros\n"
           f"Numero Pokedex: {pokedados['order']}")