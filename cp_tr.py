
import time , keyboard , pyautogui , pyperclip , datetime
from googletrans import Translator #pip install googletrans==4.0.0-rc1
import  yaml , os
 
translator = Translator(service_urls=['translate.googleapis.com'])
translator = Translator(raise_exception=True)

if  not os.path.isfile("clipbord_transrate\config.yaml"):
     
    os.makedirs('clipbord_transrate',exist_ok=True)
    config = {
        'df_lang':['ja'],
        'tr_lang':['en'],
        'z#lang_list':['en - english','ja - japanese','zh-CN - chinese','fr - French','de - German']}
    with open('clipbord_transrate/config.yaml', 'w') as file:
        yaml.dump(config, file)
        
with open('clipbord_transrate/config.yaml', 'r') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)
        
    

cp_transtateS = True

df_lang = (config['df_lang'])[0]
tr_lang = (config['tr_lang'])[0]

def Rprint(MStext,MStype="INFO"):
    date = datetime.datetime.now()
    time_now = f"{date.hour}:{date.minute}-{date.second}.{date.microsecond}"
    
    
    
    return "[{} {}] ".format(time_now[:-5],MStype)+MStext

print(tr_lang)
pless_time = 0
tr_txst = ""
def cp_transtate():
    print('start servise "clip bord transrate" ')
    tr_txst = str
    while cp_transtateS == True:
        pless_time = int()


        if keyboard.is_pressed("ctrl+c"):
            print("ctrl+c")
            print("send translation.google.com")
            try:
                if translator.detect(pyperclip.paste()).lang == df_lang:
                    tr_txst = translator.translate(pyperclip.paste(),dest=tr_lang).text
                elif translator.detect(pyperclip.paste()).lang == tr_lang:
                    tr_txst = translator.translate(pyperclip.paste(),dest=df_lang).text
                else :
                    tr_txst = translator.translate(pyperclip.paste(),dest=df_lang).text
            except:
                tr_txst = "<<[cp_transrate_service]ERR>>"
                print("err can't transration. Try to reduce the number of characters")



        if pless_time != 0 :
            pless_time -= 1

        if keyboard.is_pressed("ctrl+space") and pless_time == 0:
            print("ctrl+space")
            old_cp = pyperclip.paste()
            pyperclip.copy(tr_txst)
            pyautogui.hotkey('ctrl','v')
            pyperclip.copy(old_cp)
            pless_time = 100
        elif keyboard.is_pressed("ctrl+space") and pless_time == 1:
            print("ctrl+space")
            old_cp = pyperclip.paste()
            pyperclip.copy(tr_txst)
            pyautogui.hotkey('ctrl','v')
            pyperclip.copy(old_cp)
            pless_time += 1
        time.sleep(0.05)
        
cp_transtate()
        
