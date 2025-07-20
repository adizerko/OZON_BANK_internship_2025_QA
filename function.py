import requests


def the_tallest_hero(gender: str, work: bool):
    if gender not in {"Male", "Female"}:
        raise ValueError("Пол должен быть Male или Female")

    if not isinstance(work, bool):
        raise TypeError("Аргумент work должен быть типа bool (True/False)")

    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Ошибка: код {response.status_code}")
        return None

    data = response.json()
    max_height = 0.0
    tallest_hero_data = None

    for hero in data:
        if gender != hero["appearance"]["gender"]:
            continue

        occupation = hero["work"]["occupation"] != '-'

        if occupation != work:
            continue

        hero_height = hero["appearance"]["height"][1]

        if 'meters' in hero_height:
            height = float(hero_height.split(" ")[0]) * 100
        elif 'cm' in hero_height:
            height = float(hero_height.split(" ")[0])
        else:
            continue

        if height > max_height:
            max_height = height
            tallest_hero_data = hero

    return tallest_hero_data
