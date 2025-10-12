import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
@bot.message_handler(commands=['go'])
def go(message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username

    # Упоминание пользователя: если есть username — используем @, иначе HTML-ссылку
    if username:
        mention = f"@{username}"
    else:
        mention = f"<a href='tg://user?id={user_id}'>{name}</a>"

    # Проверка по user_id, а не username (так надёжнее)
    if user_id not in Pokemon.pokemons.keys():
        pokemon = Pokemon(user_id)
        bot.send_message(
            message.chat.id,
            f"{mention}, вот твой покемон!\n{pokemon.info()}",
            parse_mode="HTML"  # <-- обязательно!
        )
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.send_message(
            message.chat.id,
            f"{mention}, ты уже создал себе покемона!",
            parse_mode="HTML"  # <-- и здесь тоже
        )


bot.infinity_polling(none_stop=True)

