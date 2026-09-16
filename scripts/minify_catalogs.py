import json
import sys
import os

def minify_json(input_path, output_path):
    if not os.path.exists(input_path):
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    items = []
    if isinstance(data, dict):
        if "peliculas" in data: items = data["peliculas"]
        elif "series" in data: items = data["series"]
        elif "animes" in data: items = data["animes"]
    elif isinstance(data, list):
        items = data
        
    for item in items:
        # Borramos lo que no sirve en la nueva app
        item.pop("sinopsis", None)
        item.pop("isSaved", None)
        item.pop("autoSearch", None)
        
        # Abreviamos las llaves
        if "_id" in item: item["i"] = item.pop("_id")
        if "titulo" in item: item["t"] = item.pop("titulo")
        if "año" in item: item["a"] = item.pop("año")
        if "genero" in item: item["g"] = item.pop("genero")
        if "imdb" in item: item["im"] = item.pop("imdb")
        elif "tmdb" in item: item["im"] = item.pop("tmdb")
        if "img" in item: item["p"] = item.pop("img")
        elif "poster" in item: item["p"] = item.pop("poster")
        if "servers" in item: item["s"] = item.pop("servers")
        elif "servidores" in item: item["s"] = item.pop("servidores")
            
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, separators=(',', ':'))

if __name__ == "__main__":
    minify_json(sys.argv[1], sys.argv[2])
