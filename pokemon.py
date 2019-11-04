"""
    ejemplo consumir una api
    uso pokemon.py -n #numeroPokedex
"""



import requests
import json
import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], "../"))

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon/'

    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-n", type=str, help="Numero Pokedex")
    args = parser.parse_args()

    form = args.n
    fin = url + form

    response = requests.get(fin)  #creamos un objeto llamado repon
    print(response.url)
    
    if response.status_code == 200:
        """
        response_json = response.json() #Diccionario
        origin = response_json['origin']
        print(origin)
        """
       # response_json = json.loads(response.text)
       # origin = response_json['origin']
        content = response.content
        print(content)
