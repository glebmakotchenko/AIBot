import telebot
import openai
from settings import TG_TOKEN, AI_TOKEN

def createRequest(text):
  openai.api_key = AI_TOKEN
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": text}
    ]
  )
  return completion.choices[0].message.content

bot = telebot.TeleBot(TG_TOKEN)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, createRequest(message.text))

# Запускаем бота
bot.polling(none_stop=True, interval=0)


