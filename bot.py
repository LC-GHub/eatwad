from dataclasses import dataclass
import telebot
import os
from telegram import Bot, Update
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import psycopg2
#HELLO 
###################
API_KEY = '5376979755:AAHW7-u6ceSTFUXSDAKFzutKv_Nlhm2GaFo'
bot = telebot.TeleBot(API_KEY)
db_url = 'postgres://trfbygdjlzgylg:ba4770e7951333f228b1a3d5010c9b2a05b8068e656ab010ce9d60b0bb9755aa@ec2-3-229-252-6.compute-1.amazonaws.com:5432/d82285oehroe9v'
db_url_get = os.environ.get(db_url)
con = psycopg2.connect(db_url_get)
####################################
def kb_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Get meal recommendation", callback_data="cb_reco"))
    return markup

@bot.message_handler(commands=['start'])
def start(start):
    bot.send_message(start.chat.id, "Welcome to eatwad bot")
    bot.send_message(start.chat.id, "Food recommendations from a curated list created by aku")
    bot.send_message(start.chat.id, "Menu", reply_markup=kb_markup())


    

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_reco":
        bot.answer_callback_query(call.id, "Where are you at now? (Postal code of nearest known location)")
        cid = call.message.chat.id
        mid = call.message.message_id
        bot.send_message(cid,"Generating recommendation...")
        time.sleep(3)
        recommendation()
       
def recommendation():
    cur = con.cursor



def opendb():
    db = psycopg2.connect(database = "postgres", user = "")


@bot.message_handler(commands = ['help'])
def help(help):
    bot.send_message(help.chat.id,
    '''
    /cancel to cancel\n
/feedback to feedback\n
/new for new recommendation
    ''')



bot.polling()