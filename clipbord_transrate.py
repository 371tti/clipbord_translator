import time , keyboard , pyautogui , pyperclip
from googletrans import Translator #pip install googletrans==4.0.0-rc1

translator = Translator(service_urls=['translate.googleapis.com'])
translator = Translator(raise_exception=True)

def cp_transtate():
    print('start servise "clip bord transrate" ')
    tr_txst = str
    cp_up = ""
    while cp_transtateS == True:
        if keyboard.is_pressed("ctrl+c"):
            try:
                if translator.detect(pyperclip.paste()).lang == 'ja':
                    tr_txst = translator.translate(pyperclip.paste(),dest='en').text
                elif translator.detect(pyperclip.paste()).lang == 'en':
                    tr_txst = translator.translate(pyperclip.paste(),dest='ja').text
                else :
                    tr_txst = translator.translate(pyperclip.paste(),dest='ja').text
            except:
                tr_txst = "<<[cp_transrate_service]ERR文字数が長すぎる場合があります。分けてみて、、>>"

        
        if keyboard.is_pressed("ctrl+c+x"):
            old_cp = pyperclip.paste()
            pyperclip.copy(tr_txst)
            pyautogui.hotkey('ctrl','v')
            pyperclip.copy(old_cp)
        time.sleep(0.05)
