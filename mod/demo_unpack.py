from httpcore import ConnectTimeout
from mnemonic import Mnemonic
from bip32utils import BIP32Key, BIP32_HARDEN
from requests import get
import random
from os import path, makedirs
from multiprocessing.pool import ThreadPool as Pool
import threading
from Bip39Gen import Bip39Gen
from time import sleep
import ctypes


class Settings:
    save_empty = "y"
    total_count = 0
    wet_count = 0
    dry_count = 0
    Received_count = 0


def userinput():
    print(
        """
Спасибо за использование говна и палок (@cr_farm_bot).
Исходный код в гитхабе (https://github.com/ArtikUSB/BitGen-demo)
Это demo-версия програмы, которая вообще можно юзать. 
Без пароля програма прекрасно работает!
Автоотключения нет (Вырезано)!
"""
    )
    print("Удачи!")
    start()


def internet():
    try:
        get("https://www.google.com")
    except ConnectTimeout:
        return False


lock = threading.Lock()

if internet():
    dictionary = (
        get(
            "https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt"
        )
        .text.strip()
        .split("\n")
    )


def getBalance(addr):
    try:
        sleep(1)
        response = get(f"https://blockchain.info/multiaddr?active={addr}&n=1")
        return response.json()["wallet"]
    except:
        print("Сайт заблокировал твой IP адресс. Включи VPN")
        sleep(5)
        getBalance(addr)
        pass


def generateSeed():
    seed = ""
    for i in range(12):
        seed += random.choice(dictionary) if i == 0 else " " + random.choice(dictionary)
    return seed


def bip39(mnemonic_words):
    mobj = Mnemonic("english")
    seed = mobj.to_seed(mnemonic_words)
    bip32_root_key_obj = BIP32Key.fromEntropy(seed)
    bip32_child_key_obj = (
        bip32_root_key_obj.ChildKey(44 + BIP32_HARDEN)
        .ChildKey(0 + BIP32_HARDEN)
        .ChildKey(0 + BIP32_HARDEN)
        .ChildKey(0)
        .ChildKey(0)
    )
    return bip32_child_key_obj.Address()


def check():
    for _ in range(0, 3600):
        mnemonic_words = Bip39Gen(dictionary).mnemonic
        addy = bip39(mnemonic_words)
        balance = 0
        Received = 0
        sleep(1)
        internet()
        with lock:
            print(
                f"\nAddress: {addy} | Balance: {balance} | Mnemonic phrase: {mnemonic_words}"
            )
            Settings.total_count += 1
            if Settings.save_empty == "y":
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Mining 2.0 Demo - С балансом: {Settings.wet_count} -  С оборотом: {Settings.Received_count} - Всего проверок: {Settings.total_count}"
                )
            else:
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Mining 2.0 Demo - С балансом: {Settings.wet_count} -  С оборотом: {Settings.Received_count} - Всего проверок: {Settings.total_count}"
                )
        if balance > 0:
            with open("results/wet.txt", "a") as w:
                w.write(
                    f"Address: {addy} | Balance: {balance} | Mnemonic phrase: {mnemonic_words}\n"
                )
                Settings.wet_count += 1
        else:
            if Settings.save_empty == "n":
                pass
            else:
                with open("results/dry.txt", "a") as w:
                    w.write(
                        f"Address: {addy} | Received: {Received} |Balance: {balance} | Mnemonic phrase: {mnemonic_words}\n"
                    )
                    Settings.dry_count += 1


def start():
    try:
        threads = int(input("Выбери количество потоков от 1 до 10000: "))
    except ValueError:
        print("Что-то не так")
        start()
    Settings.save_empty = input("Сохранять пустые? (y/n): ").lower()
    if internet():
        pool = Pool(threads)
        for _ in range(threads):
            pool.apply_async(check, ())
        pool.close()
        pool.join()
    else:
        print("Перезапусти програму")
        userinput()


if __name__ == "__main__":
    path = "results"
    if not path.exists(path):
        makedirs(path)
    if not internet() is True:
        print("Без интернета не получится :С")
    userinput()
