import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton




def getKeyboard():
    keyboard = ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="🖍 Tutti i saldi")
            ]
                                    
                           
                                ]
                            )
    return keyboard  


def getFilterKeyboard():
    keyboard = ReplyKeyboardMarkup(
                                keyboard=[
                                
                                ]
                            )
    return keyboard  



     


     
        