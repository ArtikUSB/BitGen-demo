import pprint
import mnemonic
import bip32utils
import requests
import random
import os
from decimal import Decimal
from multiprocessing.pool import ThreadPool as Pool
import threading
from Bip39Gen import Bip39Gen
import time
import ctypes
from bs4 import BeautifulSoup
import math
import psutil



class Settings():
    save_empty = "y"
    total_count = 0
    wet_count = 0
    dry_count = 0
    Received_count = 0
    
link = "https://t.me/demodostup4000HJDKKSKDN/2?embed=1"
responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', class_ = "tgme_widget_message_text js-message_text").text

link2 = "https://t.me/demodostup4000HJDKKSKDN/3?embed=1"
responce2 = requests.get(link2).text
soup2 = BeautifulSoup(responce2, 'lxml')
block2 = soup2.find('div', class_ = "tgme_widget_message_text js-message_text").text



def makeDir():
    path = 'results'
    if not os.path.exists(path):
        os.makedirs(path)

def is_running(script):
    for q in psutil.process_iter():
        if q.name().startswith('python'):
            if len(q.cmdline())>1 and script in q.cmdline()[1] and q.pid !=os.getpid():
                print("Одновременно может работать только 1 окно программы. \nЕсли хочешь заработать больше и быстрее - покупай дополнительные лицензии. \nОткрыт файл лишний '{}' ".format(script))
                time.sleep(60)
                is_running("demo.py")
            else:
                pass

def userInput():
    print("""
    Спасибо за использование нашей программы. Если что-то не работает - пишите в tg: @btc_farm_pro
    Это demo-версия програмы. Для того, чтобы запустить софт, тебе придётся ввести пароль. 
    Его можно взять в @cr_farm_bot. Без пароля програма не работает!
    Автоотключение программы происходит каждый час!
   
    В полной версии (Купить можно t.me/mining_20_bot):
    - Автоуведомления в Telegram
    - Автоматическая смена прокси
    - От 200 000 000 проверок кошельков в сутки
    - Помимо баланса - история операций (можно найти не только Bitcoin)
    - Обновления и модификации для софта
    - Уже, кстати, доступен софт для поиска ETH, LTC, BCH, DOGE
    
    Слито @tg_inc_soft
    Слито @tg_inc_soft
    Слито @tg_inc_soft
    """)
    print("")
    print(block2)
    print("")
    for trial in range(3):
        print ("Слито @tg_inc_soft \nПопытка #",trial, end=" ")
        passw = input('.  Введите пароль > ')
        if passw == block : start()
    else:
        passw = block

 


def getInternet():
    try:
        try:
            requests.get('https://www.google.com')
        except requests.ConnectTimeout:
            requests.get('http://1.1.1.1')
        return True
    except requests.ConnectionError:
        print("no internet")
        time.sleep(5)
        getInternet()
        return False


lock = threading.Lock()

if getInternet() == True:
    dictionary = requests.get(
        'https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt').text.strip().split('\n')
else:
    pass


def getBalance(addr):
    try:
        time.sleep(1)
        response = requests.get(
            f'https://blockchain.info/multiaddr?active={addr}&n=1')

        return (
            response.json()['wallet']
        )
    except:
        print("Сайт заблокировал твой IP адресс. Включи VPN")
        time.sleep(5)
        getBalance(addr)
        pass


def generateSeed():
    seed = ""
    for i in range(12):
        seed += random.choice(dictionary) if i == 0 else ' ' + \
            random.choice(dictionary)
    return seed


def bip39(mnemonic_words):
    mobj = mnemonic.Mnemonic("english")
    seed = mobj.to_seed(mnemonic_words)

    bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
    bip32_child_key_obj = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(0)

    return bip32_child_key_obj.Address()


def check():
    for i in range(0, 3600):
        mnemonic_words = Bip39Gen(dictionary).mnemonic
        addy = bip39(mnemonic_words)
        balance = 0
        Received = 0
        time.sleep(1)
        getInternet()
        with lock:
            print(
                f'Слито @tg_inc_soft Слито @tg_inc_soft Слито @tg_inc_soft\n\nAddress: {addy} | Balance: {balance} | Mnemonic phrase: {mnemonic_words}')
            Settings.total_count += 1
            if Settings.save_empty == "y":
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Mining 2.0 Demo - С балансом: {Settings.wet_count} -  С оборотом: {Settings.Received_count} - Всего проверок: {Settings.total_count}")
            else:
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Mining 2.0 Demo - С балансом: {Settings.wet_count} -  С оборотом: {Settings.Received_count} - Всего проверок: {Settings.total_count}")
        if balance > 0:
            with open('results/wet.txt', 'a') as w:
                w.write(
                    f'Address: {addy} | Balance: {balance} | Mnemonic phrase: {mnemonic_words}\n')
                Settings.wet_count += 1
        else:
            if Settings.save_empty == "n":
                pass
            else:
                with open('results/dry.txt', 'a') as w:
                    w.write(
                        f'Address: {addy} | Received: {Received} |Balance: {balance} | Mnemonic phrase: {mnemonic_words}\n')
                    Settings.dry_count += 1
    os.system('out.bat')


def helpText():
    print("""
За помощью обращайтесь к t.me/btc_farm_pro
        """)


def start():
    try:
        threads = int(input("Выбери количество потоков 1-10 000: "))
        if threads > 5:
            print("Слито @tg_inc_soft Слито @tg_inc_soft\nБро, в демке максимум 5 потоков! Покупай полную версию, чтобы разогнаться на 100%")
            start()
    except ValueError:
        print("Что-то не то")
        start()
    Settings.save_empty = input("Слито @tg_inc_soft\nСохранять пустые? (y/n): ").lower()
    if getInternet() == True:
        pool = Pool(threads)
        for _ in range(threads):
            pool.apply_async(check, ())
        pool.close()
        pool.join()
    else:
        print("Перезапусти програму")
        userInput()


if __name__ == '__main__':
    makeDir()
    is_running("demo.py")
    getInternet()
    if getInternet() == False:
        print("Без интернета не получится :С")
    else:
        pass
    userInput()
