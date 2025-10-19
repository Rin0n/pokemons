from random import randint
import requests
from datetime import datetime, timedelta
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
        self.hp = randint(50, 100)
        self.power = randint(10, 20)
        self.last_feed_time = datetime.now()
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
    def info(self):
        return f'''
        Имя твоего покемона: {self.name}
        Настроение твоего покемона: {self.mood}
        Способность твоего покемона: {self.ability}
        hp: {self.hp}
        power: {self.power}
        '''           
    def attack(self, enemy):
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!"
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time-delta_time}"

class Wizard(Pokemon):
    def feed(self):
        return super().feed(hp_increase=15)
class Fighter(Pokemon):
    def attack(self, enemy):
        sp = randint(5,15)
        self.power += sp
        результат = super().attack(enemy)
        self.power -= sp
        return результат + f"\nБоец применил супер-атаку силой:{sp} "
    def feed(self):
        return super().feed(hp_ncrease=15)

