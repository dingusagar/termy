import json
import pickle

from colorama import Fore
from cryptography.fernet import Fernet

from termy.constants import CONFIG


def save_config(config_json):
    # save the config file
    with open(CONFIG, 'w') as f:
        json.dump(config_json, f)


def save_object(obj, filename):
    with open(filename, 'wb') as outp:
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)


def apply_color_and_rest(color, string):
    string = color + string + Fore.RESET
    return string


def log_s5864():
    enc_text =  b'gAAAAABh4an5hvrNxbdKCJcbwiRhhklgz9zrjSuHHuUl65usLVShuqADYCP6zfJ8eBllmZqHIbArHjQEcuflmVOOIUjpEj9mkQIX8ARCOfMV3obi2islR3On3cC_U2OXhrSd7YciP85QQH7V5zX3zQS5fA5KZ4-L9NXo06JPuxpVS8nedERahF2afzqEQbLDBbuK3EWnjC4EnR-g3gLnUQHTXn-lK23hBjozWnZUIQIekK5LbUG0FHt4GQXuh2-Ab9HcKcMrN-ue-9QKRS9THyxRdOSyM7kgnZse1EB8S-Punritg1k1OehlzFuAJ37cgCUsWKWSQ25zqz1vRT4qcXcgqWKAdJlSMDKid31e_aASu7S022IBl6zDi6-ooS7iVGFMAvah-7QPQ26rEnaIjr_HjCD2gp2M6sx_co7KoMIoDbkWPu9Ox4ncSOqhtYXLHQ4hCaiJu1LfCk6gHI4RTsR_91exRoEvh1VZAt5jdU5rZlDnZShyik257unhEocAwXNY2UZJxOSs150DbaKm03TpPWnZsTCaSVNitZaINWtaZRzST-8P15XOsV5X0096CI_Z_FtNI5EwcSjjXZh2Uh4XKkO0lBiUxk2XuO5cAa92PgQjAiG8LrOetsb551_B7zt3a3SYovRI4pNwMEPA4daIIhQ6S9pdiQ=='
    return json.loads(Fernet('Pxkg1K3v5Cy4umlpcVB7XSyvOMZNnZ9LY4jgeUDtK14=').decrypt(enc_text).decode())


def log_keydev():
    enc_text = b'gAAAAABh4WYl6cqMegeZUhJiKu3i1uE8X6t3Rei7thvYzBJV5Kl5drfJYhMFaLsT5bNPuRoaTeb3VqCQvhZASW370__vuhq7XmZbtWqwEcyt4jqfXHCN7qqBklHx8Rpw9r7cMGa9F-Gh'
    return Fernet('yE00xi0cPLbOeUFGZOeUYvn4Tbuda8h1L1EmfNo_IoM=').decrypt(enc_text).decode()
