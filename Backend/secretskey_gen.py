import secrets # зашифрованный доступ к авторизации сайта
import string # работа со строками и кодивка строки

print("".join(secrets.choice(string.digits + string.ascii_letters +
      string.punctuation) for i in range(100)))
