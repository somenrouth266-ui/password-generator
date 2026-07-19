#project #4
#password generator

import random
import string
characters=int(input("Enter character length:"))
huggingface=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(characters):
    password+=random.choice(huggingface)
print("Generated password:",password)