from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):
        abilities = ["огненный шар", "водяной поток", "удар молнии", "ветер судьбы"]
        moods = ["счастлив", "зол", "сонный", "воодушевлён", "голоден"]
        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()


        self.mood = moods[randint(0, len(moods)-1)]

        self.ability = abilities[randint(0, len(abilities)-1)]
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "Pikachu"
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    
    def use_ability(self, other):
        dmg = randint(15, 40)
        other.hp -= dmg
        return f"{self.name} использует {self.ability} и наносит {dmg} урона!"

    # Метод класса для получения информации
    def info(self, mood):
        return f"Имя и настроение твоего покеомона: {self.name}, {self.mood}"
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img



