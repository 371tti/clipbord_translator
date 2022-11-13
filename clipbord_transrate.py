import time , keyboard , pyautogui , pyperclip
from googletrans import Translator #pip install googletrans==4.0.0-rc1

translator = Translator(service_urls=['translate.googleapis.com'])
translator = Translator(raise_exception=True)

cp_transtateS = True

df_lang = 'ja'
tr_lang = 'en'

def cp_transtate():
    print('start servise "clip bord transrate" ')
    tr_txst = str
    cp_up = ""　# ..think???????
    while cp_transtateS == True:
        if keyboard.is_pressed("ctrl+c"):
            try:
                if translator.detect(pyperclip.paste()).lang == df_lang:
                    tr_txst = translator.translate(pyperclip.paste(),dest=tr_lang).text
                elif translator.detect(pyperclip.paste()).lang == tr_lang:
                    tr_txst = translator.translate(pyperclip.paste(),dest=df_lang).text
                else :
                    tr_txst = translator.translate(pyperclip.paste(),dest=df_lang).text
            except:
                tr_txst = "<<[cp_transrate_service]ERR　too long ? >>"

        
        if keyboard.is_pressed("ctrl+c+x"):
            old_cp = pyperclip.paste()
            pyperclip.copy(tr_txst)
            pyautogui.hotkey('ctrl','v')
            pyperclip.copy(old_cp)
        time.sleep(0.05)
