import telebot
from telebot import types
from google_trans_new import LANGUAGES, google_translator

translator = google_translator()
lang = "en"

bot = telebot.TeleBot("1716068298:AAF_WQrVuYSVZUupw-T4GHZzhqIjQ_EhO5c", skip_pending=True)

@bot.message_handler(content_types=["text"])
def cevri(message):
    try:
        global lang
        dil = message.text.split(" ")[1]
        translator = google_translator()
        i = message.text
        s = translator.translate(i, lang_tgt= dil)
        bot.reply_to(message,s)
    except:
        global lang
        translator = google_translator()
        i = message.text
        s = translator.translate(i, lang_tgt= lang)
        bot.reply_to(message,s)
print("bot aktif")
if __name__=="__main__":
    bot.polling(none_stop=True)
