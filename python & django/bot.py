from telebot import types
import telebot;
bot = telebot.TeleBot('1472019478:AAHP3GRfDKflub56T-s11pGIk8KI_knyAZ8');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	@bot.message_handler(content_types=['text', 'document', 'audio'])

if message.text == "Привет":
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши привет")
else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)

#стикер
@bot.message_handler(content_types=["text"])
def text(message):
    if message.text == 'sticker':
        bot.send_sticker(message.chat.id, 'CAADAgADsQADWQMDAAEJK1niI56hlhYE')

#как получить стикер
@bot.message_handler(content_types=["sticker"])
def handle_docs_audio(message):
    # Получим ID Стикера
    sticker_id = message.sticker.file_id
    # Нужно получить путь, где лежит файл стикера на Сервере Телеграмма
    file_info = bot.get_file(sticker_id)
    # Теперь формируем ссылку и скачивам файл
    urllib.request.urlretrieve(f'http://api.telegram.org/file/bot{config.token}/{file_info.file_path}', file_info.file_path)

#Кнопки и ветки сообщений
name = '';
surname = '';
age = 0;
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surnme);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message('Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);

def get_menu(message):
    global menu;
    menu = message.text;
    bot.send_message('Что вы хотите заказать из меню?');
    bot.register_next_step_handler(message, get_menu);

def get_age(message):
    global age;
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
      keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
      key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
      keyboard.add(key_yes); #добавляем кнопку в клавиатуру
      key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
      keyboard.add(key_no);
      question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+' и вы хотите заказать '+menu+'?';
      bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

#метод-обработчик
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        .... #код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Запомню : )');
    elif call.data == "no":
         ... #переспрашиваем

#получаем файл от пользователя
@bot.message_handler(content_types=["document"])
def handle_docs_audio(message):
    document_id = message.document.file_id
    file_info = bot.get_file(document_id)
    urllib.request.urlretrieve(f'http://api.telegram.org/file/bot{config.token}/{file_info.file_path}', file_info.file_path)

#олучаем музыку от пользователя
@bot.message_handler(content_types=["audio"])
def handle_docs_document(message):
    audio_id = message.audio.file_id
    file_info = bot.get_file(audio_id)
    urllib.request.urlretrieve(f'http://api.telegram.org/file/bot{config.token}/{file_info.file_path}', file_info.file_path)*

#методы для выбора валюты дл оплаты меню
@bot.message_handler(commands=['exchange'])  
def exchange_command(message):  
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.row(  
        telebot.types.InlineKeyboardButton('USD', callback_data='get-USD')  
    )  
    keyboard.row(  
        telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR'),  
        telebot.types.InlineKeyboardButton('RUR', callback_data='get-RUR')  
    )  
  
    bot.send_message(  
        message.chat.id,   
        'Click on the currency of choice:',  
        reply_markup=keyboard  
    )
