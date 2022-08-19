

import os
import time
import telepot
from telepot.loop import MessageLoop
#from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import keyboards

import links_req

import sys
sys.path.append('../conn')
import user_sql



############################################################
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def on_chat_message(msg):
    users = []
    first_name = msg['from']['first_name']
   #  last_name = msg['from']['last_name']
    last_name = "noname"
    if  "last_name" in msg['from']:
        last_name = msg['from']['last_name']
    user_id = msg['from']['id']
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat Message:', last_name, first_name, chat_id)
    print(content_type)
    if content_type == 'text':
       if msg['text'] == '/start':
            keyboard = keyboards.getKeyboard()
            if user_sql.insertUser(user_id, first_name, last_name):
                bot.sendMessage(chat_id, 'Registrazione effettuata correttamente!', reply_markup=keyboard) 
                # bot.sendDocument(chat_id=chat_id, document=open("gifs/welcome.gif", 'rb'))
                bot.sendMessage(145645559, "Utente nuovo: [ " + str(user_id) + " " + first_name+ " "+ last_name + " ]")
            else:
                bot.sendMessage(chat_id, 'Sei nel menu principale', reply_markup=keyboard)  
            # keyboard = keyboards.getKeyboard()
            # bot.sendMessage(chat_id, 'Benvenuto', reply_markup=keyboard)   
       elif msg['text'] == '🖍 Tutti i saldi':
          keyboard = keyboards.getFilterKeyboard()
          links = user_sql.getLinks()
          for link in links:
            bot.sendMessage(chat_id, str(link),reply_markup=keyboard)  

       elif str(msg['text']).upper().startswith("MAXPRICE "):
          maxprice = int((str(msg['text'])[9:]).strip())
          user_sql.update_price(str(chat_id), str(maxprice))
          bot.sendMessage(chat_id, "Prezzo aggiornato con successo a: " + str(maxprice) + " Euro")  
      
      #  elif str(msg['text']).startswith("/Ticket_dettaglio_"): 🖍 Tutti i saldi
      #        ticketId = str(msg['text'])[18:] 
    
       else:
             bot.sendMessage(chat_id, 'Commando non riconosciuto! Premere /start per iniziare.') 

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
   # print('Callback Query:', query_id, from_id, query_data)
    bot.answerCallbackQuery(query_id, text='Got it')
   #  file="das/" + query_data
   # bot.sendDocument(chat_id=from_id, document=open(file, 'rb')) 
    print(query_data)


test = "5528961366:AAEiCxFr3VwObL3c1zzUXyTAZYRecBZMlWM"
prod = "5769294017:AAFRYsF0J_gupg8OD-7UD2N-eWTuhCN3bqQ"

bot = telepot.Bot(prod)

MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')
starttime = time.time()

while 1:
    print("\n tick ogni 10 sec \n")
    list_links = links_req.getLinks()
    users = user_sql.getUsers()

    for url in list_links:
      exsists = user_sql.link_present(url[0])
      if not exsists:
         for u in users:
            if float(url[1]) <= float(u[1]):
               bot.sendMessage(int(u[0]), url[0])  
            user_sql.insertLink(url[0])

    time.sleep(30)
    #time.sleep((60.0 * 1) - ((time.time() - starttime) % 60.ticketToday.getTicketToday(chat_id)ticketToday.getTicketToday(chat_id)0))