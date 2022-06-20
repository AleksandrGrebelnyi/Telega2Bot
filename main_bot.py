import telebot
from flask import Flask, request
import os
import messages
import emoji
from datetime import datetime

app = Flask(__name__)
TOKEN = os.environ.get('TOKEN')
MY_ID = os.environ.get('MY_ID')
time_now = datetime.now()
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')  # paste token using os
user_answers = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, messages.mes.get('GREETINGS'))
    sti_1 = open('pictures/mot_convince.webp', 'rb')
    bot.send_message(message.chat.id, '<u><b>Наше тело может всё,\nтолько поверь в это</b></u> 🧘‍')
    bot.send_sticker(message.chat.id, sti_1)
    bot.send_message(message.chat.id, messages.mes.get('FIO'))
    bot.register_next_step_handler(message, fio_step)

def fio_step(message):
    user_answers['Дата'] = time_now.strftime('%Y-%m-%d')
    user_answers['Имя'] = message.text
    bot.send_message(message.chat.id, '<u><b>Будь той энергией, которую ты хочешь привлекать в свою жизнь</b></u>')
    sti_2 = open('pictures/mot_energy.webp', 'rb')
    bot.send_sticker(message.chat.id, sti_2)
    bot.send_message(message.chat.id, messages.mes.get('PHONE'))
    bot.register_next_step_handler(message, phone_step)

def phone_step(message):
    user_answers['Номер телефона'] = message.text
    bot.send_message(message.chat.id, '<u><b>Помни, почему ты начала</b></u>')
    sti_3 = open('pictures/mot_rememeber.webp', 'rb')
    bot.send_sticker(message.chat.id, sti_3)
    bot.send_message(message.chat.id, messages.mes.get('GMAIL'))
    bot.register_next_step_handler(message, gmail_step)

def gmail_step(message):
    user_answers['Почта'] = message.text
    bot.send_message(message.chat.id, '<u><b>Мечты не начнут осуществляться, пока ты не начнешь над ними '
                                      'работать</b></u>')
    sti_4 = open('pictures/mot_work_dreams.webp', 'rb')
    bot.send_sticker(message.chat.id, sti_4)
    bot.send_message(message.chat.id, messages.mes.get('WEIGHT'))
    bot.register_next_step_handler(message, weight_step)

def weight_step(message):
    user_answers['Вес'] = message.text
    bot.send_message(message.chat.id, '<u><b>Приседания ниже, а стандарты выше</b></u>')
    sti_4 = open('pictures/mot_squats_low.webp', 'rb')
    bot.send_sticker(message.chat.id, sti_4)
    bot.send_message(message.chat.id, messages.mes.get('WAIST'))
    bot.register_next_step_handler(message, waist_step)

def waist_step(message):
    user_answers['Талия'] = message.text
    bot.send_message(message.chat.id, '<u><b>Каждое утро - это новая возможность, что бы сделать себя лучше</b></u>')
    sti_5 = open('pictures/mot_new_life.webp', 'rb')
    bot.send_sticker(message.chat.id, sti_5)
    bot.send_message(message.chat.id, messages.mes.get('BELLY'))
    bot.register_next_step_handler(message, belly_step)

def belly_step(message):
    user_answers['Живот'] = message.text
    bot.send_message(message.chat.id, '<u><b>Результат Олеси, онлайн подопечной Александра. У всех всё получается,'
                                      ' главное следуйте рекомендациям тренера😉</b></u>')
    sti_6 = open('pictures/mot_lesya.webp', 'rb')
    bot.send_sticker(message.chat.id, sti_6)
    bot.send_message(message.chat.id, messages.mes.get('UNDERBELLY'))
    bot.register_next_step_handler(message, underbelly_step)

def underbelly_step(message):
    user_answers['Низ живота'] = message.text
    bot.send_message(message.chat.id, '<u><b>Результат Светланы, онлайн тренировки + питание</b></u>')
    sti_7 = open('pictures/mot_sveta.webp', 'rb')
    bot.send_sticker(message.chat.id, sti_7)
    bot.send_message(message.chat.id, messages.mes.get('HIPS'))
    bot.register_next_step_handler(message, hips_step)

def hips_step(message):
    user_answers['Бёдра'] = message.text
    bot.send_message(message.chat.id, '<u><b>Мотивация помогает начать, привычка помогает продолжать</b></u>')
    sti_8 = open('pictures/mot_habits.webp', 'rb')
    bot.send_sticker(message.chat.id, sti_8)
    bot.send_message(message.chat.id, messages.mes.get('HEALTH'))
    bot.register_next_step_handler(message, health_step)

def health_step(message):
    user_answers['Здоровье'] = message.text
    bot.send_message(message.chat.id, '<u><b>А накаченная попа может и решит проблему😜</b></u>')
    sti_9 = open('pictures/mot_2.webp', 'rb')
    bot.send_sticker(message.chat.id, sti_9)
    bot.send_message(message.chat.id, messages.mes.get('PLACE_OF_TRAININGS'))
    bot.register_next_step_handler(message, place_of_trainings_step)

def place_of_trainings_step(message):
    user_answers['Место тренировок'] = message.text
    bot.send_message(message.chat.id, '<u><b>Все победы начинаются с побед над собой</b></u>')
    sti_10 = open('pictures/motivation.webp', 'rb')
    bot.send_sticker(message.chat.id, sti_10)
    bot.send_message(message.chat.id, messages.mes.get('NOW_MANY_TRAININGS'))
    bot.register_next_step_handler(message, how_many_trainings_step)

def how_many_trainings_step(message):
    user_answers['Количество тренировок'] = message.text
    bot.send_message(message.chat.id, '<u><b>И бока уберём, и живот уберём, всё получится.</b></u>')
    sti_11 = open('pictures/mot.webp', 'rb')
    bot.send_sticker(message.chat.id, sti_11)
    bot.send_message(message.chat.id, messages.mes.get('DURATION_TRAINING'))
    bot.register_next_step_handler(message, duration_trainings_step)

def duration_trainings_step(message):
    user_answers['Продолжительность тренировки'] = message.text
    bot.send_message(message.chat.id, '<u><b>Немного юмора😁</b></u>')
    sti_12 = open('pictures/eat_joke_1.webp', 'rb')
    bot.send_sticker(message.chat.id, sti_12)
    bot.send_message(message.chat.id, messages.mes.get('TIME_FOOD_INTAKE'))
    bot.register_next_step_handler(message, times_food_intake_step)

def times_food_intake_step(message):
    user_answers['Количество приёмов пищи сейчас'] = message.text
    bot.send_message(message.chat.id, '<u><b>Питание будет вкусное и разнообразное</b></u>')
    sti_13 = open('pictures/food.webp', 'rb')
    bot.send_sticker(message.chat.id, sti_13)
    bot.send_message(message.chat.id, messages.mes.get('FAVORITE_FOOD'))
    bot.register_next_step_handler(message, favorite_food_step)

def favorite_food_step(message):
    user_answers['Любимая еда'] = message.text
    bot.send_message(message.chat.id, '<u><b>Немного примеров по еде</b></u>')
    sti_14 = open('pictures/food2.weebp', 'rb')
    bot.send_sticker(message.chat.id, sti_14)
    bot.send_message(message.chat.id, messages.mes.get('GOALS'))
    bot.register_next_step_handler(message, goals_step)

def goals_step(message):
    user_answers['Цели'] = message.text
    bot.send_message(message.chat.id, '<u><b>Если желание подкреплено действиями, обязательно всё получится </b></u>')
    sti_14 = open('pictures/do.webp', 'rb')
    bot.send_sticker(message.chat.id, sti_14)
    bot.send_message(message.chat.id, messages.mes.get('QUESTIONS'))
    bot.register_next_step_handler(message, final_step)

@bot.message_handler(type=['text'])
def final_step(message):
    user_answers['Вопросы'] = message.text
    name_user = message.from_user.username
    if name_user is None:
        name_user = 'Пользователь не указывал своё имя в телеграм'
    user_answers['Имя в телеграм'] = str(name_user)
    bot.send_message(message.chat.id, messages.mes.get('READ'))
    file = open('necessary_info_for_client/Прочитайте_меня.txt', 'rb')
    bot.send_document(message.chat.id, file)
    file2 = open('necessary_info_for_client/И_меня_прочти_обязательно.txt', 'rb')
    bot.send_document(message.chat.id, file2)
    file3 = open('necessary_info_for_client/Полезная_информация.txt', 'rb')
    bot.send_document(message.chat.id, file3)
    bot.send_message(message.chat.id, messages.mes.get('FINAL'))
    with open('users_excel_info.csv', 'w') as f:
        f.write(user_answers.get('Дата') + '\n')
        f.write(list(user_answers.keys())[1] + ',' + user_answers.get('Имя') + '\n')
        f.write(list(user_answers.keys())[2] + ',' + user_answers.get('Номер телефона') + '\n')
        f.write(list(user_answers.keys())[3] + ',' + user_answers.get('Почта') + '\n')
        f.write(list(user_answers.keys())[4] + ',' + user_answers.get('Вес') + '\n')
        f.write(list(user_answers.keys())[5] + ',' + user_answers.get('Талия') + '\n')
        f.write(list(user_answers.keys())[6] + ',' + user_answers.get('Живот') + '\n')
        f.write(list(user_answers.keys())[7] + ',' + user_answers.get('Низ живота') + '\n')
        f.write(list(user_answers.keys())[8] + ',' + user_answers.get('Бёдра') + '\n')
        f.write(list(user_answers.keys())[9] + ',' + user_answers.get('Здоровье') + '\n')
        f.write(list(user_answers.keys())[10] + ',' + user_answers.get('Место тренировок') + '\n')
        f.write(list(user_answers.keys())[11] + ',' + user_answers.get('Количество тренировок') + '\n')
        f.write(list(user_answers.keys())[12] + ',' + user_answers.get('Продолжительность тренировки') + '\n')
        f.write(list(user_answers.keys())[13] + ',' + user_answers.get('Количество приёмов пищи сейчас') + '\n')
        f.write(list(user_answers.keys())[14] + ',' + user_answers.get('Любимая еда') + '\n')
        f.write(list(user_answers.keys())[15] + ',' + user_answers.get('Цели') + '\n')
        f.write(list(user_answers.keys())[16] + ',' + user_answers.get('Вопросы') + '\n')
        f.write(list(user_answers.keys())[17] + ',' + user_answers.get('Имя в телеграм') + '\n')
    bot.send_message(MY_ID, f'{list(user_answers.keys())[0]} => {user_answers.get("Дата")}\n'
                            f'{list(user_answers.keys())[1]} => {user_answers.get("Имя")}\n'
                            f'{list(user_answers.keys())[2]} => {user_answers.get("Номер телефона")}\n'
                            f'{list(user_answers.keys())[3]} => {user_answers.get("Почта")}\n'
                            f'{list(user_answers.keys())[4]} => {user_answers.get("Вес")}\n'
                            f'{list(user_answers.keys())[5]} => {user_answers.get("Талия")}\n'
                            f'{list(user_answers.keys())[6]} => {user_answers.get("Живот")}\n'
                            f'{list(user_answers.keys())[7]} => {user_answers.get("Низ живота")}\n'
                            f'{list(user_answers.keys())[8]} => {user_answers.get("Бёдра")}\n'
                            f'{list(user_answers.keys())[9]} => {user_answers.get("Здоровье")}\n'
                            f'{list(user_answers.keys())[10]} => {user_answers.get("Место тренировок")}\n'
                            f'{list(user_answers.keys())[11]} => {user_answers.get("Количество тренировок")}\n'
                            f'{list(user_answers.keys())[12]} => {user_answers.get("Продолжительность тренировки")}\n'
                            f'{list(user_answers.keys())[13]} => {user_answers.get("Количество приёмов пищи сейчас")}\n'
                            f'{list(user_answers.keys())[14]} => {user_answers.get("Любимая еда")}\n'
                            f'{list(user_answers.keys())[15]} => {user_answers.get("Цели")}\n'
                            f'{list(user_answers.keys())[16]} => {user_answers.get("Вопросы")}\n'
                            f'{list(user_answers.keys())[17]} => {user_answers.get("Имя в телеграм")}\n')
    print(user_answers.items())


@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Python Telegram Bot", 200


@app.route('/')
def main():
    bot.remove_webhook()
    bot.set_webhook(url='https://telega2bot.herokuapp.com/' + TOKEN)
    return 'Python Telegram Bot', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))