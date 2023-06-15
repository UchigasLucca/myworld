import requests
import msvcrt
import sys

while True:
    pokemon_name = input('Qual pokemon quer informacao? Pode ser o numero da pokedex ou o nome :D ')
    pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'.strip().lower())
    
    if pokemon.status_code == 404:
        print('Pokemon nao encontrado, tente novamente')
        continue

    pokedados = pokemon.json()

    if 'height' in pokedados:
        converter_decimetros = pokedados['height'] / 10
        print(f"Nome: {pokedados['name']}\n"
              f"Altura: {converter_decimetros} metros\n"
              f"Numero Pokedex: {pokedados['id']}\n"
              f"ID: {pokedados['order']}")
    
    print("Pressione 1 para sair ou 2 para reiniciar...")
    while True:
        if msvcrt.kbhit():
            escolha = msvcrt.getch().decode('utf-8')
            break
    
    if escolha == '1':
        sys.exit()
