import json
import pickle

from colorama import Fore
from cryptography.fernet import Fernet


def save_object(obj, filename):
    with open(filename, 'wb') as outp:
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)


def apply_color_and_rest(color, string):
    string = color + string + Fore.RESET
    return string


def log_s5864():
    enc_text = b'gAAAAABhvu91BuEypyHsKQgQDELqwlyMexg9RhvjZ6ooN6t203KPxlWRZKDY9DLnWAAop9JgBaNMIFUJStTNgWwEtpfMzDsXmUeuijxk3vYQkh12Ac1Z8a0kdWiYKF1zEA515U0Zu_NyxYkfGuqSwKvZ4dL6PiJ52ueXlQ-b_8Xwk2d2T2R7Ge8-8MB0Sz2aYl9APD-EynOQYtYdxJL9py6Cn3f7Pb4d6CC41GywsiL35u-pTu6EMQUpNQg7VvPH3q3-rwegqgsw5F_iYxWJ7yqICPbotXlRJQd9JaShgFawfBMbLrZeOEqQfBJa3LNf05iU93z-Y64ZafQ3fv8wEsFG3UbR3ygaRZ4OsnBOEyAYy9-ngEPRCceCkaQFFPQ6-nNOD6ZmTeNewFSyezLrjAb0kmD91x7WVfNAUXPfkznll7Rbd0zBE3Mo5n0q-W9lIiyUDUlOsE_p1SJLuyi5FqATV4dQe1DEpTIQQmISPuELVZYfE08MX0m7zliWwp0FWXER1CIRUrqJKoGkAURe4gtkV054wcByGPBVER4EcDyjKkFuCnfVTL-4d60sT9cqFaB39PZukMzXJYgRC-yGrgWCnDHPtraNYKt1fIqM4EujLjhGjJzAnpEpKlXAQKRiVMpE8iiGwVqW0ZBG-jAHOsWdzYlSRNg2IqFwG3l-_PiOZPg1f0uYcF4='
    return json.loads(Fernet('XkhcdzIQ-BwZT8-nyJ4n8c2-j_XODP6oGMGLcjWxuCU=').decrypt(enc_text).decode())
