#Content types:
# text , audio . document , photo , sticker ,video ,video_note ,voice , location ,
# contact , new_chat_members ,
# left_chat_members (пользователь вышел) , new_chat_title (новое название чата), new_chat_photo (новое фото чата), delete_chat_photo (удалено фото чата),
# group_chat_created (создан групповой чат), supergroup_chat_created , migrate_to_chat_id ,
# migrate_from_chat_id , pinned_message ._

import telebot
TOKEN = "6010978270:AAEt8ZC96cqDOxRQyaqGG3RIAB8VuYh4l14"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(content_types =['document','voice',])

def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id,'У тебя красивый голос')
def handle_docs_audio(message):("у тебя красивый голос")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    full_name = message.chat.first_name + ' ' + message.chat.last_name
    bot.send_message(message.chat.id, f"Welcome, {full_name}")

@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')





bot.polling(none_stop=True)


