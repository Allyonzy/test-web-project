import secrets
import string
print("".join(secrets.choice(string.digits + string.ascii_letters +
      string.punctuation) for i in range(100)))
