import random
import string


letters = list(string.ascii_letters)
digits = list(string.digits)
specials = list(string.punctuation)



num_of_letters = int(raw_input("How many letters do you want in your password? Pick a number between 0 and 26."))
password_letters = random.sample(letters,num_of_letters)

num_of_numbers = int(raw_input("How many numbers do you want in your password? Pick a number between 0 and 10."))
password_numbers = random.sample(digits,num_of_numbers)

num_of_specials = int(raw_input("How many special characters do you want in your password? Pick a number between 0 and 32."))
password_specials = random.sample(specials,num_of_specials)

print password_letters
print password_numbers
print password_specials


password_order = password_letters + password_numbers + password_specials

print password_order

random.shuffle(password_order)

password_final = "".join(password_order)

print password_final