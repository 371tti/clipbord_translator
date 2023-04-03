
import time , keyboard , pyautogui , pyperclip , datetime
from googletrans import Translator #pip install googletrans==4.0.0-rc1
import  yaml , os
os.system('color') #windows only
translator = Translator(service_urls=['translate.googleapis.com'])
translator = Translator(raise_exception=True)

if  not os.path.isfile("clipbord_transrate\config.yaml"): #config create
     
    os.makedirs('clipbord_transrate',exist_ok=True)
    config = {
        'df_lang':['ja'],
        'tr_lang':['en'],
        'z#lang_list':['en - english','ja - japanese','zh-CN - chinese','fr - French','de - German']}
    with open('clipbord_transrate/config.yaml', 'w') as file:
        yaml.dump(config, file)
        
with open('clipbord_transrate/config.yaml', 'r') as file: #config roding
    config = yaml.load(file, Loader=yaml.SafeLoader)
        
    

cp_transtateS = True

df_lang = (config['df_lang'])[0]
tr_lang = (config['tr_lang'])[0]



def info(MStext,MStype="INFO"): #message time
    date = datetime.datetime.now()
    time_now = f"{date.hour}:{date.minute}-{date.second}.{date.microsecond}"
    
    
    
    return "[{} {}] ".format(time_now[:-5],MStype)+MStext


pless_time = 0
tr_txst = ""
engin = "translation.google.com"
def cp_transtate():
    print(info(f'start servise \033[38;2;0;255;255mclip bord transrate \033[38;2;0;255;0m"{tr_lang}"\033[00m'))
    tr_txst = str
    old_cp_str = str
    while cp_transtateS == True:

        new_cp_str = pyperclip.paste()
        if new_cp_str != old_cp_str: #keyboard.is_pressed("ctrl+c"):
            print (info(f'translation \033[48;2;64;64;64m\n"{new_cp_str}"\033[00m'))
            print(info(f'send \033[38;2;0;255;0m"{engin}"\033[00m'))
            try:
                if translator.detect(pyperclip.paste()).lang == df_lang:
                    tr_txst = translator.translate(pyperclip.paste(),dest=tr_lang).text
                elif translator.detect(pyperclip.paste()).lang == tr_lang:
                    tr_txst = translator.translate(pyperclip.paste(),dest=df_lang).text
                else :
                    tr_txst = translator.translate(pyperclip.paste(),dest=df_lang).text
                print(info("success translation"))
            except:
                tr_txst = "<<[cp_transrate_service]ERR>>"
                print(info("\033[38;2;20;20;255merr can't transration. Try to reduce the number of characters.\033[00m","ERR"))
        old_cp_str = pyperclip.paste()


    

        if keyboard.is_pressed("ctrl+space") and pless_time == 0:
            print(info("ctrl+space"))
            old_cp = pyperclip.paste()
            pyperclip.copy(tr_txst)
            pyautogui.hotkey('ctrl','v')
            pyperclip.copy(old_cp)
            time.sleep(0.5)
 

        time.sleep(0.05)
        
cp_transtate()
        
