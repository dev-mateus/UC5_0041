import random
import string


def gerador_senha(tamanho=4):
    caracteres = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits
    caracteres_obrigatorios = random.choices(string.ascii_uppercase) + random.choices(string.ascii_lowercase) + random.choices(string.punctuation) + random.choices(string.digits)
    senha = random.choices(caracteres, k=tamanho) + caracteres_obrigatorios
    random.shuffle(senha)
    senha = ''.join(senha)
    print(senha)


gerador_senha(8)
